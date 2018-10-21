from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='accounts/login.html'))
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]