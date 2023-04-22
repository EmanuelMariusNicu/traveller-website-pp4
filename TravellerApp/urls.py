from . import views
from django.urls import path

urlpatterns = [
    path('add_trip/', views.AddTrip.as_view(), name='add_trip'),
    path("", views.TripList.as_view(), name="home"),
    path('search/', views.SearchResults.as_view(), name='search_results'),
    path('<slug:slug>/', views.TripDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.TripLike.as_view(), name='post_like'),
    path('browse/<slug:slug>', views.BrowseByTag.as_view(), name='browse'),
    
]