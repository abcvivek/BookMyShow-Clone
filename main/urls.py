from django.urls import path,include,re_path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.user_signup,name="signup"),
    path('movies/', views.movies.as_view(), name='movies'),
    path('search/', views.search, name='search'),
    re_path(r'^accounts/(?P<pk>\d+)/(?P<user>\w+)/',views.account.as_view(),name="accounts"),
    re_path(r'^accounts-update/(?P<pk>\d+)/',views.account_update.as_view(),name="accounts-update"),
    re_path(r'^accounts-delete/(?P<pk>\d+)/',views.account_delete.as_view(),name="accounts-delete"),
    re_path(r'^movie-detail/(?P<pk>\d+)/',views.movie_detail_view.as_view(),name="movie-detail-view"),
    re_path(r'^theatre-list/(?P<pk>\d+)/',views.movie_booking_theatre.as_view(),name="movie-booking-theatre"),
    re_path(r'^booking/(?P<pk>\d+)/',views.show_details.as_view(),name="movie-booking"),
    # re_path(r'^booking/(?P<pk>\d+)/',views.booking,name="booking"),
    re_path(r'^book-ticket/(?P<pk>\d+)/(?P<id>\d+)',views.book_ticket,name="book-ticket"),
    re_path(r'^booked/(?P<pk>\d+)/',views.booked.as_view(),name="booked"),
    re_path(r'^cancel/(?P<pk>\d+)/',views.cancel_ticket,name="cancel_ticket"),
]