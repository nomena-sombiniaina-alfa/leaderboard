from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
import secrets
from tqdm import tqdm
from ctf.models import Flag, Hint

class Command(BaseCommand):
    def clean_db(self):
        flags = Flag.objects.all()
        for flag in tqdm(flags, 'Clearing all flags'):
            flag.delete()
    
    def handle(self, *args, **options):
        self.clean_db()
        faker = Faker()
        for i in tqdm(range(1,randint(50,100)), 'Creating new flags'):
            flag = Flag.objects.create(
                value = secrets.token_hex(randint(30,50)),
                description = faker.text()
            )                     
            for i in range(1, randint(1,4)):
                Hint.objects.create(
                    value = faker.text(100),
                    flag = flag
                )