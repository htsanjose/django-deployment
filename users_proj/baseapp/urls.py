from django.conf.urls import url
from baseapp import views

# Template urls
app_name = 'baseapp'

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'user_login/',views.user_login,name='user_login'),
]
