from .models import Game, Rating, Cluster
from django.contrib.auth.models import User
from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np 

def update_clusters():
  all_user_names = list(map(lambda x: x.username, User.objects.only("username")))
  all_game_ids = set(map(lambda x: x.game.id, Rating.objects.only("game")))
  num_users = len(all_user_names)
  ratings_matrix = dok_matrix((num_users, max(all_game_ids)+1), dtype=np.float32)
  for i in range(num_users):
    user_ratings = Rating.objects.filter(username=all_user_names[i])
    for user_rating in user_ratings:
      ratings_matrix[i,user_rating.game.id] = user_rating.rating
  
  k = int(num_users / 10) + 2
  kmeans = KMeans(n_clusters=k)
  clustering = kmeans.fit(ratings_matrix.tocsr())

  Cluster.objects.all().delete()
  new_clusters = {i: Cluster(name=i) for i in range(k)}
  for cluster in new_clusters.values():
    cluster.save()
  for i,cluster_label in enumerate(clustering.labels_):
    new_clusters[cluster_label].users.add(User.objects.get(username=all_user_names[i]))
