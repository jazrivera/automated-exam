from . import views
from django.conf.urls import url, include


urlpatterns = [
    url(r'^users/$', views.UserListApiView.as_view(), name='users'),
    url(r'^users/register/$', views.UserRegisterView.as_view(), name='register'),
    url(r'^exams/$', views.ExamApiView.as_view(), name='exams'),
    url(r'^exams/answers/$', views.ExamAnswerApiView.as_view(), name='answers'),
]
