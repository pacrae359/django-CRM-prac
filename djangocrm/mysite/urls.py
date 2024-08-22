from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('individual_record/<int:pk>', views.individual_record, name="individual_record"),
    path('add_record/', views.add_record, name="add_record"),
    path('edit_record/<int:pk>', views.edit_record, name="edit_record"),
    path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
]
