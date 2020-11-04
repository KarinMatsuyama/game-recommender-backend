from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, RatingViewSet, ClusterViewSet, TwitchViewSet

router = DefaultRouter()
router.register('games', GameViewSet, basename='game')
router.register('ratings', RatingViewSet, basename='rating')
router.register('clusters', ClusterViewSet, basename='cluster')
router.register('twitch-oauth', TwitchViewSet, basename='twitch-oauth')

urlpatterns = router.urls
