from django.shortcuts import render
from django.views.generic import ListView
from .models import Team
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.db import models


def home(request):
    return render(request, 'ctf/home.html')

def about(request):
    return render(request, 'ctf/about.html')

def rules(request):
    return render(request, 'ctf/rules.html')

@login_required
def submit_flag(request):
    team = Team.objects.get(profile = request.user.id)
    if request.method =='POST':
        flag_value = request.POST.get('flag')
        if flag_value and team.current_flag.value == flag_value:
            team.found_flag()
            
    context = {
        'team': team
    }
    return render(request, 'ctf/submit-flag.html', context)


class Leaderboard(ListView):
    model = Team
    template_name = 'ctf/leaderboard.html'
    def get_context_data(self, **kwargs):        
        all_teams = Team.objects.all().annotate(count_flag_found=models.Count('flag_found')).order_by('-count_flag_found','last_flag_found')
        top_teams = all_teams.exclude(last_flag_found__isnull=True)[:18]
        teams =  all_teams.exclude(pk__in=top_teams.values_list('pk', flat=True))
        context = {
            'top_teams': top_teams,
            'teams': teams
        }
        return context
    

class UserLoginView(LoginView):
    template_name = 'ctf/login.html'
    success_url = reverse_lazy('ctf:home')
    redirect_authenticated_user = True
    
class UserLogoutView(LogoutView):
    pass

# Errors : 
def handle404(request, exception=None):
    return render(request, '404.html', {})


def handle500(request, exception=None):
    return render(request, '500.html', {})