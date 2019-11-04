from django.urls import path
from . import views


app_name = 'usercontrol'
urlpatterns = [
    path('', views.sign_in, name="sign_in"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('sign_out/', views.sign_out, name="sign_out"),
    path('account/', views.account, name="account"),
    path('edit_infos/', views.edit_user_infos, name="edit_user_infos"),
    path('change_pwd/', views.change_passwd, name="change_pwd"),
    path('manage_sms/', views.manage_sms, name="manage_sms"),
]
