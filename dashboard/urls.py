from django.urls import path,include,re_path
from dashboard import views
app_name = 'dashboard'

urlpatterns = [
    path('', views.theatre_manager_view.as_view(), name='theatre-manager-view'),
    path('theatre-view/',views.theatre_view.as_view(),name="theatre-view"),
    path('screen-view/',views.screen_view.as_view(),name="screen-view"),
    path('show-view/',views.show_view.as_view(),name="show-view"),
    path('movie-view/',views.movie_view.as_view(),name="movie-view"),
    path('theatre-manager-create/',views.theatre_manager_create.as_view(),name="theatre-manager-create"),
    path('theatre-create/',views.theatre_create.as_view(),name="theatre-create"),
    path('screen-create/',views.screen_create.as_view(),name="screen-create"),
    path('show-create/',views.show_create.as_view(),name="show-create"),
    path('movie-create/',views.movie_create.as_view(),name="movie-create"),
    re_path(r'^theatre-manager-update/(?P<pk>\d+)/$',views.theatre_manager_update_view.as_view(),name="theatre-manager-update-view"),
    re_path(r'^theatre-update/(?P<pk>\d+)/$',views.theatre_update_view.as_view(),name="theatre-update-view"),
    re_path(r'^screen-update/(?P<pk>\d+)/$',views.screen_update_view.as_view(),name="screen-update-view"),
    re_path(r'^show-update/(?P<pk>\d+)/$',views.show_update_view.as_view(),name="show-update-view"),
    re_path(r'^movie-update/(?P<pk>\d+)/$',views.movie_update_view.as_view(),name="movie-update-view"),
    re_path(r'^theatre-manager-delete/(?P<pk>\d+)/$',views.theatre_manager_delete_view.as_view(),name="theatre-manager-delete-view"),
    re_path(r'^theatre-delete/(?P<pk>\d+)/$',views.theatre_delete_view.as_view(),name="theatre-delete-view"),
    re_path(r'^screen-delete/(?P<pk>\d+)/$',views.screen_delete_view.as_view(),name="screen-delete-view"),
    re_path(r'^show-delete/(?P<pk>\d+)/$',views.show_delete_view.as_view(),name="show-delete-view"),
    re_path(r'^movie-delete/(?P<pk>\d+)/$',views.movie_delete_view.as_view(),name="movie-delete-view"),
    re_path(r'^theatre-manager-detail/(?P<pk>\d+)/',views.theatre_manager_detail_view.as_view(),name="theatre-manager-detail-view"),
    re_path(r'^theatre-detail/(?P<pk>\d+)/',views.theatre_detail_view.as_view(),name="theatre-detail-view"),  
    re_path(r'^screen-detail/(?P<pk>\d+)/',views.screen_detail_view.as_view(),name="screen-detail-view"), 
    re_path(r'^show-detail/(?P<pk>\d+)/',views.show_detail_view.as_view(),name="show-detail-view"), 
    re_path(r'^movie-detail/(?P<pk>\d+)/',views.movie_detail_view.as_view(),name="movie-detail-view"),   
]

