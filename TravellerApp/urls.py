from . import views
from django.urls import path
from multiurl import multiurl

urlpatterns = [multiurl(
    path('search/', views.SearchResults.as_view(), name='search_results'),
    path('add_trip/', views.AddTrip.as_view(), name='add_trip'),
    path('<slug:slug>/', views.TripDetail.as_view(), name='post_detail'),
    path('<slug:slug>/edit', views.EditTrip.as_view(), name='edit_trip'),
    path('<slug:slug>/delete', views.delete_trip, name='delete_trip'),
    path("", views.TripList.as_view(), name="home"),
    path('like/<slug:slug>', views.TripLike.as_view(), name='post_like'),
    path('browse/<slug:slug>', views.BrowseByTag.as_view(), name='browse'),
    path(
        'delete_comment/<comment_id>',
        views.delete_comment,
        name='delete_comment'
        ),
)]