from django.db import models
from django.contrib.auth.models import User

class Cluster(models.Model):
  name = models.CharField(max_length=100)
  users = models.ManyToManyField(User)

  def __str__(self):
    return f'id: {self.id} name: {self.name}'

  def get_members(self):
    return '\n'.join([user.username for user in self.users.all()])
