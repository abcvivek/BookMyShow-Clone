from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from dashboard import models
from dashboard.models import movie,show,theatre,screen,User
from django.views.generic import DetailView,ListView,TemplateView,UpdateView,DeleteView
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q
from django.contrib import messages


# Create your views here.

def index(request) :

    slider_images = movie.objects.raw('SELECT id,slideshow_image FROM dashboard_movie ORDER BY id DESC LIMIT 4')

    thumbnail_images = movie.objects.raw('SELECT id,thumbnail_image FROM dashboard_movie ORDER BY id DESC LIMIT 8')

    trailer = movie.objects.raw('SELECT id,trailer FROM dashboard_movie ORDER BY id DESC LIMIT 6')

    return render(request,'main/index.html',{ 'slider_images':slider_images,'thumbnail_images' : thumbnail_images,'trailer' : trailer })

class movies(ListView) :
    context_object_name = 'movie'
    model = models.movie
    template_name = 'main/movie-view.html'

class movie_detail_view(DetailView) :
    context_object_name = 'movie'
    model = models.movie
    template_name = 'main/movie-detail-view.html'

class movie_booking_theatre(DetailView) :
    context_object_name = 'movie'
    model = models.movie
    template_name = 'main/movie-booking-theatre.html'

# login required
class booking(DetailView) :
    context_object_name = 'show'
    model = models.show
    template_name = 'main/booking-page.html'

class account(LoginRequiredMixin,DetailView) :
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['pk']
        username = self.kwargs['user']
        u = User.objects.get(pk=user_id)
        if u.username == username :
            context['test'] = username
            return context
    context_object_name = 'user'
    model = models.User
    template_name = 'main/account.html'


class account_update(LoginRequiredMixin,UpdateView) :
    context_object_name = 'user'
    model = models.User
    fields = ['username','first_name','last_name','email',]
    template_name = 'main/account_form.html'
    success_url = reverse_lazy('main:index')

class account_delete(LoginRequiredMixin,DeleteView) :
    context_object_name = 'user'
    model = models.User
    template_name = 'main/user_confirm_delete.html'
    success_url = reverse_lazy('main:index')

def user_signup(request) :
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() : 
            user = form.save()
            return redirect('main:index')
    else :
        form = UserCreationForm()
    return render(request,'main/signup.html',{'form':form})


def search(request) :
    if request.method == 'POST' :
        search_query = request.POST['search']

        if search_query :
            result = movie.objects.filter(Q(name__icontains=search_query) | Q(hero__icontains=search_query) | Q(heroine__icontains=search_query))

            if result :
                return render(request,'main/search.html',{'results':result,'search_query' : search_query})
            else :
                messages.error(request,'Sorry no results found')
        else :
            return HttpResponseRedirect('/')

    return render(request,'main/search.html')


   





        