from .models import Game, Rating
from .serializers import GameSerializer, RatingSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class GameViewSet(viewsets.ModelViewSet):
  serializer_class = GameSerializer
  queryset = Game.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['igdbid']
  
  # def get_queryset(self):
  #   igdbid = self.request.query_params.get('igdbid', None)
  #   if igdbid is not None:
  #     igdbid = int(igdbid)
  #     queryset = Game.objects.filter(igdb_id=igdbid)
  #     return queryset

class RatingViewSet(viewsets.ModelViewSet):
  serializer_class = RatingSerializer
  queryset = Rating.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['game', 'author']

  # def get_queryset(self):
  #   current_user = self.request.user
  #   return Rating.objects.filter(author=current_user)
