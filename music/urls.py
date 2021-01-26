from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),

    path("<int:pk>/", views.DetailView.as_view(), name='detail'),

    #path("<int:id>/favourite/", views.favourite, name ='favourite'),

    # /music/album/add/
    path("album/add/", views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/
    path("album/<int:pk>/", views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    path("album/<int:pk>/delete/", views.AlbumDelete.as_view(), name='album-delete'),
]