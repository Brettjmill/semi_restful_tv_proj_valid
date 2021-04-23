from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows', views.all_shows),
    path('shows/<int:show_id>', views.show_detail),
    path('shows/<int:show_id>/edit', views.show_edit),
    path('shows/<int:show_id>/update', views.show_update),
    path('shows/<int:show_id>/delete', views.show_delete)
]