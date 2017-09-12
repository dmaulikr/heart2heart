from django.conf.urls import url
import h2hmainsite.views as views
from heartuser.forms import MyAuthenticationForm, SignupForm
from django.contrib.auth import views as auth_views

login_form = MyAuthenticationForm()
signup_form = SignupForm()
login_extra_context = {"login_form":login_form}

urlpatterns = [
    url(r'^$', auth_views.login, {'authentication_form':MyAuthenticationForm, 'extra_context':login_extra_context}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^dashboard/$', views.dashboard_view, name='dashboard' ),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^search/$', views.search_view, name='search'),
    url(r'^settings/$', views.settings_view, name='settings'),
    url(r'^inbox/$', views.inbox, name='inbox')
]