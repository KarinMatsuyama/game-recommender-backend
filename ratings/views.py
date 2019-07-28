from .models import Game, Rating, Cluster
from .serializers import GameSerializer, RatingSerializer, ClusterSerializer
from .recommendations import update_clusters
from django.contrib.auth.models import User
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
import numpy as np

class GameViewSet(viewsets.ModelViewSet):
  serializer_class = GameSerializer
  queryset = Game.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['igdbid']

  @action(methods=['get'], detail=True, url_path='average-rating', url_name='average-rating')
  def average_rating(self, request, pk=None):
    if pk.isdigit():
      game = self.get_object()
      average = game.average_rating()
      return Response(average)


class RatingViewSet(viewsets.ModelViewSet):
  serializer_class = RatingSerializer
  queryset = Rating.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['game', 'author']


class ClusterViewSet(viewsets.ModelViewSet):
  serializer_class = ClusterSerializer
  
  @action(methods=['get'], detail=False, url_path='recommendations', url_name='recommendations')
  def recommendations(self, request):
    current_user = self.request.user
    user_ratings = Rating.objects.filter(author=current_user)
    user_ratings_game_ids = set(map(lambda x: x.game.id, user_ratings))

    try:
      # if no cluster has been assigned for a user, update clusters
      user_cluster_name = User.objects.get(id=current_user.id).cluster_set.first().name
    except:
      update_clusters()
      user_cluster_name = User.objects.get(id=current_user.id).cluster_set.first().name
      
    user_cluster_other_members = Cluster.objects.get(name=user_cluster_name).users.exclude(id=current_user.id).all()
    other_members_user_ids = set(map(lambda x: x.id, user_cluster_other_members))

    other_user_ratings = Rating.objects.filter(author__in=other_members_user_ids).exclude(game__id__in=user_ratings_game_ids)
    other_users_ratings_game_ids = set(map(lambda x: x.game.id, other_user_ratings))

    game_recommendations_list = sorted(
      list(Game.objects.filter(id__in=other_users_ratings_game_ids)),
      key=lambda x: x.average_rating(),
      reverse = True
    )

    game_serializer = GameSerializer(game_recommendations_list, many=True)

    return Response(game_serializer.data)
