from django.urls import path
from . import views

app_name='ctf'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('leaderboard/', views.Leaderboard.as_view(), name='leaderboard'),
    path('submit-flag/', views.submit_flag, name='submit-flag'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]

handler404 = 'ctf.views.handle404'
handler500 = 'ctf.views.handle500'