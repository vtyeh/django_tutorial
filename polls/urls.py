from django.urls import path

from . import views

# In most cases, there may be many different apps within a project that have similar view names
# Add the app name so Django knows which app view to use
app_name = 'polls'

urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/2
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/2/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/2/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]