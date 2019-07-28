from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, RatingViewSet, ClusterViewSet

router = DefaultRouter()
router.register('games', GameViewSet, base_name='game')
router.register('ratings', RatingViewSet, base_name='rating')
router.register('clusters', ClusterViewSet, base_name='cluster')
urlpatterns = router.urls
