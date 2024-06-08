from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CITIES = [
    ("Diana","Diana"),
    ("Sava","Sava"),
    ("Itasy","Itasy"),
    ("Analamanga","Analamanga"),
    ("Vakinankaratra","Vakinankaratra"),
    ("Bongolava","Bongolava"),
    ("Sofia","Sofia"),
    ("Boeny","Boeny"),
    ("Betsiboka","Betsiboka"),
    ("Melaky","Melaky"),
    ("Alaotra-Mangoro","Alaotra-Mangoro"),
    ("Atsinanana","Atsinanana"),
    ("Analanjirofo","Analanjirofo"),
    ("Amoron'i Mania","Amoron'i Mania"),
    ("Vatovavy","Vatovavy"),
    ("Haute Matsiatra","Haute Matsiatra"),
    ("Fitovinany","Fitovinany"),
    ("Atsimo-Atsinanana","Atsimo-Atsinanana"),
    ("Ihorombe","Ihorombe"),
    ("Menabe","Menabe"),
    ("Atsimo-Andrefana","Atsimo-Andrefana"),
    ("Androy","Androy"),
    ("Anôsy","Anôsy"),
]

class Flag(models.Model):
    value = models.CharField(max_length=100)
    description = models.TextField()

class Hint(models.Model):
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    
class Team(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=CITIES)
    last_flag_found = models.DateTimeField(null=True, blank=True)
    flag_found = models.ManyToManyField(Flag, related_name='flag_found', blank=True)
    current_flag = models.ForeignKey(Flag, on_delete=models.SET_NULL, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.current_flag:
            self.current_flag = Flag.objects.first()
        if self.id and self.flag_found.count() and not self.last_flag_found:
            self.last_flag_found = timezone.now()
        return super(Team,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    def found_flag(self):
        if self.current_flag:
            self.flag_found.set([*self.flag_found.all(), self.current_flag], clear=False)
            self.current_flag = Flag.objects.get(pk = self.current_flag.id + 1)
            self.last_flag_found = timezone.now()
            self.save()

    def flag_validated(self):
        return self.flag_found.count()