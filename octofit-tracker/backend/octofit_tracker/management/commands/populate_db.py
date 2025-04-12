from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='john.doe@example.com', name='John Doe', password='password123'),
            User(email='jane.smith@example.com', name='Jane Smith', password='password123'),
            User(email='alice.wonderland@example.com', name='Alice Wonderland', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(users[0], users[1])
        team2.members.add(users[2])

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Running', duration=30, date=date(2025, 4, 10)),
            Activity(user=users[1], activity_type='Cycling', duration=45, date=date(2025, 4, 11)),
            Activity(user=users[2], activity_type='Swimming', duration=60, date=date(2025, 4, 12)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, score=100),
            Leaderboard(team=team2, score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='A quick morning run to start the day'),
            Workout(name='Evening Yoga', description='Relaxing yoga session in the evening'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
