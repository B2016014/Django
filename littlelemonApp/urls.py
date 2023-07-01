from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('menu/', views.Menu,name='menu'),
    path('menu/<int:id>', views.MenuItem,name='menuitem'),
    path('about/', views.about,name='about'),
    path('book/', views.book,name='book'),
]
