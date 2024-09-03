from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage,name="home-page"),
    path('register',views.Register,name="register"),
    path('login',views.UserLogin,name="login"),
    path('dashboard',views.Dashboard,name="dashboard"),
    path('create-record',views.CreateRecord,name="create-record"),
    path('update-record/<int:pk>',views.UpdateRecord,name="update-record"),
    path('view-record/<int:pk>',views.ViewRecord,name="view-record"),
    path('delete-record/<int:pk>',views.DeleteRecord,name="delete-record"),
    path('logout',views.UserLogout,name="logout"),
    
]