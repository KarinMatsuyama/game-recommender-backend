from .models import Game, Rating, Cluster
from .serializers import GameSerializer, RatingSerializer, ClusterSerializer
from .recommendations import update_clusters
from django.contrib.auth.models import User
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import numpy as np

class GameViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticatedOrReadOnly]
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

  # Temporary game apis for dummy igdmAPI response
  @action(methods=['get'], detail=False, url_path='cover-games', url_name='cover-games')
  def cover_games(self, request, pk=None):
    cover = [
      {
        "id": 76781,
        "url": "//images.igdb.com/igdb/image/upload/t_thumb/co1n8t.jpg"
      }
    ]
    return Response(cover)
  
  # Temporary game apis for dummy igdmAPI response
  @action(methods=['get'], detail=False, url_path='genres', url_name='genres')
  def genres(self, request, pk=None):
    genre = [{'name':['RPG']}]
    return Response(genre)
  
  # Temporary game apis for dummy igdmAPI response
  @action(methods=['get'], detail=False, url_path='platforms', url_name='platforms')
  def platforms(self, request, pk=None):
    platform = [{"name": ['PS4', 'PC']}]
    return Response(platform)

  # Temporary game apis for dummy igdmAPI response
  @action(methods=['get'], detail=False, url_path='game-by-id', url_name='game-by-id')
  def id_games(self, request, pk=None):
    game = [
    {
        "id": 26845,
        "aggregated_rating": 93.3333333333333,
        "cover": 76781,
        "first_release_date": 1564099200,
        "genres": [
            12,
            16,
            24,
            31
        ],
        "name": "Fire Emblem: Three Houses",
        "platforms": [
            130
        ],
        "similar_games": [
            7615,
            13196,
            18398,
            19404,
            22387,
            26765,
            26951,
            55038,
            55199,
            106987
        ],
        "summary": "Fire Emblem: Three Houses is being developed for the Nintendo Switch that is planned for release in summer 2019."
    },
    {
        "id": 115276,
        "aggregated_rating": 87.1666666666667,
        "cover": 71673,
        "first_release_date": 1561680000,
        "genres": [
            8
        ],
        "name": "Super Mario Maker 2",
        "platforms": [
            130
        ],
        "similar_games": [
            1070,
            1071,
            1073,
            1188,
            1191,
            96452,
            103301,
            113895,
            116589,
            120184
        ],
        "summary": "Build and play the Super Mario courses of your dreams! This sequel features a host of new tools and features—like slopes!"
    },
    {
        "id": 103301,
        "aggregated_rating": 76,
        "cover": 72683,
        "first_release_date": 1564099200,
        "genres": [
            5
        ],
        "name": "Wolfenstein: Youngblood",
        "platforms": [
            6,
            48,
            49,
            130
        ],
        "similar_games": [
            520,
            27270,
            27476,
            32902,
            43367,
            103281,
            103292,
            103298,
            106805,
            116191
        ],
        "summary": "Wolfenstein: Youngblood is a brand-new co-op experience from MachineGames, the award-winning studio that developed the critically acclaimed Wolfenstein II: The New Colossus. \n \nSet in 1980, 19 years after BJ Blazkowicz ignited the second American Revolution, Wolfenstein: Youngblood introduces the next Blazkowicz generation to the fight against the Nazis. Play as one of BJ’s twin daughters, Jess and Soph, as you search for your missing father in Nazi-occupied Paris."
    },
    {
        "id": 5867,
        "aggregated_rating": 82.5,
        "cover": 76623,
        "first_release_date": 1113264000,
        "genres": [
            12
        ],
        "name": "Jade Empire",
        "platforms": [
            6,
            11,
            12,
            14
        ],
        "similar_games": [
            41,
            116,
            660,
            832,
            1593,
            1887,
            1942,
            3025,
            3812,
            9938
        ],
        "summary": "Set in an ancient world inspired by mythical China, Jade Empire lets you train under your master's watchful eye as you learn powerful martial arts and mystical powers. When danger threatens, you'll travel across the world, from the harsh mountains of the Land of Howling Spirits to the lush gardens of the Imperial City. In your adventures, you must face powerful human and supernatural foes, learn the exotic and magical martial arts, and discover the darkest secrets of the world. Practice the greatest fighting styles and defeat the most powerful enemies to become a master of martial arts. \n \nAlso Available \nJade Empire: Limited Edition"
    },
    {
        "id": 80916,
        "aggregated_rating": 78.75,
        "cover": 67256,
        "first_release_date": 1526342400,
        "genres": [
            12,
            31,
            32
        ],
        "name": "Omensight",
        "platforms": [
            6,
            48,
            130
        ],
        "similar_games": [
            25311,
            28309,
            30245,
            36198,
            37419,
            47823,
            55199,
            68582,
            81680,
            96217
        ],
        "summary": "You are the Harbinger, a skilled warrior who exists outside of time. You have foreseen the annihilation of the land known as Urralia and have been summoned to rewrite its fate. With the power to witness and alter the last moments of Urralia’s inhabitants, it’s up to you to weave a new narrative, pave the way to a brighter future, and give the world of Urralia a second chance."
    },
    {
        "id": 1942,
        "aggregated_rating": 91.72,
        "cover": 20471,
        "first_release_date": 1431993600,
        "genres": [
            12,
            31
        ],
        "name": "The Witcher 3: Wild Hunt",
        "platforms": [
            6,
            48,
            49
        ],
        "similar_games": [
            121,
            472,
            533,
            1593,
            1887,
            3025,
            3812,
            5867,
            11118,
            15409
        ],
        "summary": "The Witcher: Wild Hunt is a story-driven, next-generation open world role-playing game set in a visually stunning fantasy universe full of meaningful choices and impactful consequences. In The Witcher you play as the professional monster hunter, Geralt of Rivia, tasked with finding a child of prophecy in a vast open world rich with merchant cities, viking pirate islands, dangerous mountain passes, and forgotten caverns to explore."
    },
    {
        "id": 41,
        "aggregated_rating": 90.5,
        "cover": 65807,
        "first_release_date": 961977600,
        "genres": [
            5,
            12
        ],
        "name": "Deus Ex",
        "platforms": [
            6,
            8,
            14,
            45
        ],
        "similar_games": [
            16,
            21,
            43,
            533,
            2031,
            3996,
            9498,
            9727,
            11270,
            19531
        ],
        "summary": "In this philosophical first-person Western RPG set in a dystopian 2052, JC Denton, a nano-augmented agent for the anti-terrorist organization UNATCO, is tasked with stopping the invasion of Liberty Island by the terrorist group NSF. As events unfold, Denton finds that he plays a large part in a world-spanning conspiracy which forces him to ponder his allegiances, beliefs, morality, and view of right and wrong."
    },
    {
        "id": 24426,
        "aggregated_rating": 80,
        "cover": 68139,
        "first_release_date": 1526342400,
        "genres": [
            8,
            9,
            31,
            32
        ],
        "name": "Forgotton Anne",
        "platforms": [
            6,
            14,
            39,
            48,
            49,
            130
        ],
        "similar_games": [
            19150,
            20342,
            25222,
            28070,
            33269,
            55173,
            55190,
            56033,
            96217,
            116681
        ],
        "summary": "Forgotton Anne is a 2d cinematic adventure game combining puzzle platforming with adventure game elements. You play as Anne, the enforcer keeping order in the Forgotton Realm, as she sets out to squash a rebellion that might prevent her master, Bonku, and herself from returning to the human world. \n \nThe World of Forgotton Anne: Imagine a place where everything that is lost and forgotten goes; old toys, letters, single socks. The Forgotten Realm is a magical world inhabited by Forgotlings, creatures composed of mislaid objects longing to be remembered again."
    },
    {
        "id": 55036,
        "aggregated_rating": 82.8,
        "cover": 69280,
        "first_release_date": 1555372800,
        "genres": [
            13,
            15
        ],
        "name": "Anno 1800",
        "platforms": [
            6
        ],
        "similar_games": [
            17613,
            18623,
            23345,
            29173,
            31515,
            36346,
            36553,
            55590,
            79134,
            102163
        ],
        "summary": "Welcome to the dawn of the industrial age. The path you choose will define your world. Are you renovator or exploiter? Suppressor or liberator? It's up to you how the world will remember your name. \n \nIn Anno 1800, players will take charge of their own fortune as they navigate the rapidly evolving technological and malicious political landscape of the 19th century in their quest to build an empire that will stand the test of time. \n \nCombining beloved features with innovative gameplay in a memorable new setting, Anno 1800 marks the beginning of a new era for the Anno franchise."
    },
    {
        "id": 1020,
        "aggregated_rating": 95.84,
        "cover": 58397,
        "first_release_date": 1379376000,
        "genres": [
            5,
            10,
            14,
            31
        ],
        "name": "Grand Theft Auto V",
        "platforms": [
            6,
            9,
            12,
            48,
            49
        ],
        "similar_games": [
            40,
            109,
            538,
            732,
            733,
            960,
            1082,
            1121,
            9498,
            19441
        ],
        "summary": "The biggest, most dynamic and most diverse open world ever created, Grand Theft Auto V blends storytelling and gameplay in new ways as players repeatedly jump in and out of the lives of the game’s three lead characters, playing all sides of the game’s interwoven story."
    }
]
    return Response(game)

  # Temporary game apis for dummy igdmAPI response
  @action(methods=['get'], detail=False, url_path='popular-games', url_name='popular-games')
  def popular_games(self, request, pk=None):
    games = [
    {
        "id": 26845,
        "aggregated_rating": 93.3333333333333,
        "cover": 76781,
        "first_release_date": 1564099200,
        "genres": [
            12,
            16,
            24,
            31
        ],
        "name": "Fire Emblem: Three Houses",
        "platforms": [
            130
        ],
        "similar_games": [
            7615,
            13196,
            18398,
            19404,
            22387,
            26765,
            26951,
            55038,
            55199,
            106987
        ],
        "summary": "Fire Emblem: Three Houses is being developed for the Nintendo Switch that is planned for release in summer 2019."
    },
    {
        "id": 115276,
        "aggregated_rating": 87.1666666666667,
        "cover": 71673,
        "first_release_date": 1561680000,
        "genres": [
            8
        ],
        "name": "Super Mario Maker 2",
        "platforms": [
            130
        ],
        "similar_games": [
            1070,
            1071,
            1073,
            1188,
            1191,
            96452,
            103301,
            113895,
            116589,
            120184
        ],
        "summary": "Build and play the Super Mario courses of your dreams! This sequel features a host of new tools and features—like slopes!"
    },
    {
        "id": 103301,
        "aggregated_rating": 76,
        "cover": 72683,
        "first_release_date": 1564099200,
        "genres": [
            5
        ],
        "name": "Wolfenstein: Youngblood",
        "platforms": [
            6,
            48,
            49,
            130
        ],
        "similar_games": [
            520,
            27270,
            27476,
            32902,
            43367,
            103281,
            103292,
            103298,
            106805,
            116191
        ],
        "summary": "Wolfenstein: Youngblood is a brand-new co-op experience from MachineGames, the award-winning studio that developed the critically acclaimed Wolfenstein II: The New Colossus. \n \nSet in 1980, 19 years after BJ Blazkowicz ignited the second American Revolution, Wolfenstein: Youngblood introduces the next Blazkowicz generation to the fight against the Nazis. Play as one of BJ’s twin daughters, Jess and Soph, as you search for your missing father in Nazi-occupied Paris."
    },
    {
        "id": 5867,
        "aggregated_rating": 82.5,
        "cover": 76623,
        "first_release_date": 1113264000,
        "genres": [
            12
        ],
        "name": "Jade Empire",
        "platforms": [
            6,
            11,
            12,
            14
        ],
        "similar_games": [
            41,
            116,
            660,
            832,
            1593,
            1887,
            1942,
            3025,
            3812,
            9938
        ],
        "summary": "Set in an ancient world inspired by mythical China, Jade Empire lets you train under your master's watchful eye as you learn powerful martial arts and mystical powers. When danger threatens, you'll travel across the world, from the harsh mountains of the Land of Howling Spirits to the lush gardens of the Imperial City. In your adventures, you must face powerful human and supernatural foes, learn the exotic and magical martial arts, and discover the darkest secrets of the world. Practice the greatest fighting styles and defeat the most powerful enemies to become a master of martial arts. \n \nAlso Available \nJade Empire: Limited Edition"
    },
    {
        "id": 80916,
        "aggregated_rating": 78.75,
        "cover": 67256,
        "first_release_date": 1526342400,
        "genres": [
            12,
            31,
            32
        ],
        "name": "Omensight",
        "platforms": [
            6,
            48,
            130
        ],
        "similar_games": [
            25311,
            28309,
            30245,
            36198,
            37419,
            47823,
            55199,
            68582,
            81680,
            96217
        ],
        "summary": "You are the Harbinger, a skilled warrior who exists outside of time. You have foreseen the annihilation of the land known as Urralia and have been summoned to rewrite its fate. With the power to witness and alter the last moments of Urralia’s inhabitants, it’s up to you to weave a new narrative, pave the way to a brighter future, and give the world of Urralia a second chance."
    },
    {
        "id": 1942,
        "aggregated_rating": 91.72,
        "cover": 20471,
        "first_release_date": 1431993600,
        "genres": [
            12,
            31
        ],
        "name": "The Witcher 3: Wild Hunt",
        "platforms": [
            6,
            48,
            49
        ],
        "similar_games": [
            121,
            472,
            533,
            1593,
            1887,
            3025,
            3812,
            5867,
            11118,
            15409
        ],
        "summary": "The Witcher: Wild Hunt is a story-driven, next-generation open world role-playing game set in a visually stunning fantasy universe full of meaningful choices and impactful consequences. In The Witcher you play as the professional monster hunter, Geralt of Rivia, tasked with finding a child of prophecy in a vast open world rich with merchant cities, viking pirate islands, dangerous mountain passes, and forgotten caverns to explore."
    },
    {
        "id": 41,
        "aggregated_rating": 90.5,
        "cover": 65807,
        "first_release_date": 961977600,
        "genres": [
            5,
            12
        ],
        "name": "Deus Ex",
        "platforms": [
            6,
            8,
            14,
            45
        ],
        "similar_games": [
            16,
            21,
            43,
            533,
            2031,
            3996,
            9498,
            9727,
            11270,
            19531
        ],
        "summary": "In this philosophical first-person Western RPG set in a dystopian 2052, JC Denton, a nano-augmented agent for the anti-terrorist organization UNATCO, is tasked with stopping the invasion of Liberty Island by the terrorist group NSF. As events unfold, Denton finds that he plays a large part in a world-spanning conspiracy which forces him to ponder his allegiances, beliefs, morality, and view of right and wrong."
    },
    {
        "id": 24426,
        "aggregated_rating": 80,
        "cover": 68139,
        "first_release_date": 1526342400,
        "genres": [
            8,
            9,
            31,
            32
        ],
        "name": "Forgotton Anne",
        "platforms": [
            6,
            14,
            39,
            48,
            49,
            130
        ],
        "similar_games": [
            19150,
            20342,
            25222,
            28070,
            33269,
            55173,
            55190,
            56033,
            96217,
            116681
        ],
        "summary": "Forgotton Anne is a 2d cinematic adventure game combining puzzle platforming with adventure game elements. You play as Anne, the enforcer keeping order in the Forgotton Realm, as she sets out to squash a rebellion that might prevent her master, Bonku, and herself from returning to the human world. \n \nThe World of Forgotton Anne: Imagine a place where everything that is lost and forgotten goes; old toys, letters, single socks. The Forgotten Realm is a magical world inhabited by Forgotlings, creatures composed of mislaid objects longing to be remembered again."
    },
    {
        "id": 55036,
        "aggregated_rating": 82.8,
        "cover": 69280,
        "first_release_date": 1555372800,
        "genres": [
            13,
            15
        ],
        "name": "Anno 1800",
        "platforms": [
            6
        ],
        "similar_games": [
            17613,
            18623,
            23345,
            29173,
            31515,
            36346,
            36553,
            55590,
            79134,
            102163
        ],
        "summary": "Welcome to the dawn of the industrial age. The path you choose will define your world. Are you renovator or exploiter? Suppressor or liberator? It's up to you how the world will remember your name. \n \nIn Anno 1800, players will take charge of their own fortune as they navigate the rapidly evolving technological and malicious political landscape of the 19th century in their quest to build an empire that will stand the test of time. \n \nCombining beloved features with innovative gameplay in a memorable new setting, Anno 1800 marks the beginning of a new era for the Anno franchise."
    },
    {
        "id": 1020,
        "aggregated_rating": 95.84,
        "cover": 58397,
        "first_release_date": 1379376000,
        "genres": [
            5,
            10,
            14,
            31
        ],
        "name": "Grand Theft Auto V",
        "platforms": [
            6,
            9,
            12,
            48,
            49
        ],
        "similar_games": [
            40,
            109,
            538,
            732,
            733,
            960,
            1082,
            1121,
            9498,
            19441
        ],
        "summary": "The biggest, most dynamic and most diverse open world ever created, Grand Theft Auto V blends storytelling and gameplay in new ways as players repeatedly jump in and out of the lives of the game’s three lead characters, playing all sides of the game’s interwoven story."
    }
]
    return Response(games)


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
