from django.urls import path, include
from .views import MovieListView
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('api/movies/', MovieListView.as_view(), name='movie_list'),
    path('movie_add', views.add_movie, name='movie_add'),
    path('', views.movie_list, name='movie_list'),
    path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie_delete/<int:movie_id>/delete/', views.movie_delete, name='movie_delete')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
