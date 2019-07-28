from rest_framework import serializers
from .models import Game, Rating, Cluster

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ('id', 'name', 'genres', 'critic_score', 'platforms', 'igdbid')

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id', 'author', 'game', 'rating', 'title', 'comment', 'published_date', 'username')

class ClusterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cluster
    fields = ('id', 'name', 'users')
