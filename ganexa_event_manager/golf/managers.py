from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class GolfClubManager(models.Manager):

    def create_golf_clubs(self, player: User) -> int:
        if player.golf_clubs.count() == 0:
            for i, golf_club in enumerate(settings.STANDARD_GOLF_GLUBS, 1):
                self.create(player=player, name=golf_club, order=i)
            return i
        else:
            return 0
