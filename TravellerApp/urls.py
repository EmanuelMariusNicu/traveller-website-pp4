from . import views
from django.urls import path

urlpatterns = [
    path("", views.TripList.as_view(), name="home"),
    path('<slug:slug>/', views.TripDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.TripLike.as_view(), name='post_like'),
]