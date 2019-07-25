from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Game(models.Model):
  name = models.CharField(max_length=200)
  genres = models.CharField(max_length=100, null=True)
  critic_score = models.IntegerField(null=True)
  platforms = models.CharField(max_length=100, null=True)
  igdbid = models.IntegerField()

  def __str__(self):
    return f'id: {self.id} name: {self.name}'

class Rating(models.Model):
  rating_choices = [(i, i) for i in range(1, 6)]
  game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='ratings')
  title = models.CharField(max_length=100, null=True, blank=True)
  comment = models.TextField(max_length=500, null=True, blank=True)
  rating = models.IntegerField(choices=rating_choices)
  published_date = models.DateTimeField(default=timezone.now())
  username = models.CharField(max_length=100)

  def __str__(self):
    return f'id: {self.id} game: {self.game} title: {self.title}'
