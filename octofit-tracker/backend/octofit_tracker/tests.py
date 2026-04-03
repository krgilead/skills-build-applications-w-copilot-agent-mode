from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        self.assertEqual(str(user), 'testuser')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, distance=5)
        self.assertEqual(str(activity), 'test@example.com - run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        workout = Workout.objects.create(user=user, name='Morning', description='Cardio')
        self.assertEqual(str(workout), 'Morning (test@example.com)')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(str(leaderboard), 'Test Team: 50')
