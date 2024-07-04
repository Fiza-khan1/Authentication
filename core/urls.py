from django.urls import path,include
from . import views

urlpatterns = [
#    path('',views.page),


   path('register/',views.register,name="register"),
   path('',views.LOGIN,name="login"),
   path('profile/',views.profile,name="profile"),
   path('logout/',views.logout_user,name="logout"),
   path('changePass/',views.changePass,name="changePass"),
   path('changePass1/',views.changeWO,name='changePass1'),
   path('userInfo/',views.userInfo,name="userinfo"),
   path('AdminProfile/',views.AdminProfile,name="adminPro")
]