from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]