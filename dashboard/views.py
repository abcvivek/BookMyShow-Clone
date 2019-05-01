from django.shortcuts import render
from django.views.generic import ListView,TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


# Create your views here.

# CRUD for Theatre Manager

class theatre_manager_create(LoginRequiredMixin,PermissionRequiredMixin,CreateView) :
    fields = '__all__'
    model = models.theatre_manager
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre_manager.can_add_theatre_manager'
    

class theatre_manager_view(LoginRequiredMixin,PermissionRequiredMixin,ListView) :
    context_object_name = 'theatre_managers'
    model = models.theatre_manager
    template_name = 'dashboard/theatre_manager_view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre_manager.can_view_theatre_manager'

class theatre_manager_detail_view(LoginRequiredMixin,PermissionRequiredMixin,DetailView) :
    context_object_name = 'theatre_managers'
    model = models.theatre_manager
    template_name = 'dashboard/theatre_manager_detail_view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre_manager.can_view_theatre_manager'

class theatre_manager_update_view(LoginRequiredMixin,PermissionRequiredMixin,UpdateView) :
    fields = ['name','email','phone','address']
    model = models.theatre_manager
    template_name = 'dashboard/theatre_manager_form.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre_manager.can_change_theatre_manager'

class theatre_manager_delete_view(LoginRequiredMixin,PermissionRequiredMixin,DeleteView) :
    context_object_name = 'theatre_managers'
    model = models.theatre_manager
    success_url = reverse_lazy("dashboard:theatre-manager-view")
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre_manager.can_delete_theatre_manager'

# CRUD for Theatre

class theatre_create(LoginRequiredMixin,PermissionRequiredMixin,CreateView) :
    fields = '__all__'
    model = models.theatre
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre.can_add_theatre'

class theatre_view(LoginRequiredMixin,PermissionRequiredMixin,ListView) :
    context_object_name = 'theatre'
    model = models.theatre
    template_name = 'dashboard/theatre_view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre.can_view_theatre'

class theatre_detail_view(LoginRequiredMixin,PermissionRequiredMixin,DetailView) :
    context_object_name = 'theatre'
    model = models.theatre
    template_name = 'dashboard/theatre-detail-view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre.can_view_theatre'

class theatre_update_view(LoginRequiredMixin,PermissionRequiredMixin,UpdateView) :
    fields = '__all__'
    model = models.theatre
    template_name = 'dashboard/theatre_form.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre.can_change_theatre'

class theatre_delete_view(LoginRequiredMixin,PermissionRequiredMixin,DeleteView) :
    context_object_name = 'theatre'
    model = models.theatre
    success_url = reverse_lazy("dashboard:theatre-view")
    login_url = 'login:user_login'
    permission_required = 'dashboard.theatre.can_delete_theatre'
    

# CRUD for screen

class screen_create(LoginRequiredMixin,PermissionRequiredMixin,CreateView) :
    fields = '__all__'
    model = models.screen
    login_url = 'login:user_login'
    permission_required = 'dashboard.screen.can_add_screen'

class screen_view(LoginRequiredMixin,PermissionRequiredMixin,ListView) :
    context_object_name = 'screen'
    model = models.screen
    template_name = 'dashboard/screen_view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.screen.can_view_screen'

class screen_detail_view(LoginRequiredMixin,PermissionRequiredMixin,DetailView) :
    context_object_name = 'screen'
    model = models.screen
    template_name = 'dashboard/screen-detail-view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.screen.can_view_screen'

class screen_update_view(LoginRequiredMixin,PermissionRequiredMixin,UpdateView) :
    fields = '__all__'
    model = models.screen
    template_name = 'dashboard/screen_form.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.screen.can_change_screen'

class screen_delete_view(LoginRequiredMixin,PermissionRequiredMixin,DeleteView) :
    context_object_name = 'screen'
    model = models.screen
    success_url = reverse_lazy("dashboard:screen-view")
    login_url = 'login:user_login'
    permission_required = 'dashboard.screen.can_delete_screen'

# CRUD for show

class show_create(LoginRequiredMixin,PermissionRequiredMixin,CreateView) :
    fields = '__all__'
    model = models.show
    login_url = 'login:user_login'
    permission_required = 'dashboard.show.can_add_show'

class show_view(LoginRequiredMixin,PermissionRequiredMixin,ListView) :
    context_object_name = 'show'
    model = models.show
    template_name = 'dashboard/show_view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.show.can_view_show'

class show_detail_view(LoginRequiredMixin,DetailView) :
    context_object_name = 'show'
    model = models.show
    template_name = 'dashboard/show-detail-view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.show.can_view_show'

class show_update_view(LoginRequiredMixin,PermissionRequiredMixin,UpdateView) :
    fields = '__all__'
    model = models.show
    template_name = 'dashboard/show_form.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.show.can_change_show'

class show_delete_view(LoginRequiredMixin,PermissionRequiredMixin,DeleteView) :
    context_object_name = 'show'
    model = models.show
    success_url = reverse_lazy("dashboard:show-view")
    login_url = 'login:user_login'
    permission_required = 'dashboard.show.can_delete_show'

# CRUD for Movie

class movie_create(LoginRequiredMixin,PermissionRequiredMixin,CreateView) :
    fields = '__all__'
    model = models.movie
    login_url = 'login:user_login'
    permission_required = 'dashboard.movie.can_add_movie'

class movie_view(LoginRequiredMixin,PermissionRequiredMixin,ListView) :
    context_object_name = 'movie'
    model = models.movie
    template_name = 'dashboard/movie_view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.movie.can_view_movie'

class movie_detail_view(LoginRequiredMixin,PermissionRequiredMixin,DetailView) :
    context_object_name = 'movie'
    model = models.movie
    template_name = 'dashboard/movie-detail-view.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.movie.can_view_movie'

class movie_update_view(LoginRequiredMixin,PermissionRequiredMixin,UpdateView) :
    fields = '__all__'
    model = models.movie
    template_name = 'dashboard/movie_form.html'
    login_url = 'login:user_login'
    permission_required = 'dashboard.movie.can_update_movie'

class movie_delete_view(LoginRequiredMixin,PermissionRequiredMixin,DeleteView) :
    context_object_name = 'movie'
    model = models.movie
    success_url = reverse_lazy("dashboard:movie-view")
    login_url = 'login:user_login'
    permission_required = 'dashboard.movie.can_delete_movie'