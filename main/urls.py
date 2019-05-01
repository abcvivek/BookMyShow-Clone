from django.urls import path,include,re_path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.user_signup,name="signup"),
    path('movies/', views.movies.as_view(), name='movies'),
    re_path(r'^accounts/(?P<pk>\d+)/(?P<user>\w+)/',views.account.as_view(),name="accounts"),
    re_path(r'^accounts-update/(?P<pk>\d+)/',views.account_update.as_view(),name="accounts-update"),
    re_path(r'^accounts-delete/(?P<pk>\d+)/',views.account_delete.as_view(),name="accounts-delete"),
    re_path(r'^movie-detail/(?P<pk>\d+)/',views.movie_detail_view.as_view(),name="movie-detail-view"),
    re_path(r'^theatre-list/(?P<pk>\d+)/',views.movie_booking_theatre.as_view(),name="movie-booking-theatre"),
    re_path(r'^booking/(?P<pk>\d+)/',views.booking.as_view(),name="booking"),
]