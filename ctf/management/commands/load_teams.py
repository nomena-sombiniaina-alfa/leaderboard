from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from random import randint, choice
from tqdm import tqdm
from ctf.models import Team,CITIES

class Command(BaseCommand):
    def clean_db(self):
        teams = Team.objects.all()
        for team in tqdm(teams, 'Clearing all teams'):
            team.delete()
    
    def handle(self, *args, **options):
        self.clean_db()
        faker = Faker()
        for i in tqdm(range(1,randint(20,40)), 'Creating new teams'):
            # Creating new username
            username = ''
            while User.objects.filter(username=username):
                username = faker.user_name()
            # Creating new email address
            email = ''
            while User.objects.filter(email=email):
                email = faker.email()                        
            user = User.objects.create(
                username = username,
                email = email,
                first_name = faker.first_name(),
                last_name = faker.last_name(),
            )
            user.set_password("password")
            user.save()
            Team.objects.create(
                profile = user,
                name = username,
                city = choice(CITIES)[0],
            )