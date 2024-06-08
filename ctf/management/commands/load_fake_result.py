from django.core.management.base import BaseCommand
from tqdm import tqdm
from ctf.models import Flag, Team
from random import randint
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        flags = Flag.objects.all()
        for team in tqdm(Team.objects.all(), 'Assign fake results to all teams'):
            if randint(0,1):
                team.flag_found.add(*flags[:randint(1,len(flags)-1)])
                team.save()