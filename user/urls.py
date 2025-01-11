from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('account/', account, name='account'),
    path('change-password/', change_password, name='change-password'),
    path('payment/', payment, name='payment'),
    path('send-email-code/', send_email_code, name='send-email-code'),
    path('six-digit-password/', six_digit_password, name='six-digit-password'),
]