from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as octo_models

from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='password', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        Activity.objects.create(user=clark, type='Yoga', duration=20, calories=100)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=1000)
        Leaderboard.objects.create(user=steve, score=900)
        Leaderboard.objects.create(user=bruce, score=950)
        Leaderboard.objects.create(user=clark, score=980)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (to be created in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
# class Activity(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     calories = models.IntegerField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     duration = models.IntegerField()
#
# class Leaderboard(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     score = models.IntegerField()
