from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User = get_user_model()
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        users = [
            User(email='ironman@marvel.com', username='ironman', team=marvel),
            User(email='captain@marvel.com', username='captain', team=marvel),
            User(email='batman@dc.com', username='batman', team=dc),
            User(email='superman@dc.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password')
            user.save()

        # Create Activities
        activities = [
            Activity(user=users[0], type='run', duration=30, distance=5),
            Activity(user=users[1], type='cycle', duration=45, distance=15),
            Activity(user=users[2], type='swim', duration=60, distance=2),
            Activity(user=users[3], type='run', duration=25, distance=4),
        ]
        for activity in activities:
            activity.save()

        # Create Workouts
        workouts = [
            Workout(user=users[0], name='Morning Cardio', description='Run and cycle'),
            Workout(user=users[1], name='Strength', description='Weights and pushups'),
            Workout(user=users[2], name='Swim Session', description='Long swim'),
            Workout(user=users[3], name='Speed Run', description='Short fast run'),
        ]
        for workout in workouts:
            workout.save()

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
