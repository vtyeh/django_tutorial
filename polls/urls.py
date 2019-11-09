from django.urls import path

from . import views

# In most cases, there may be many different apps within a project that have similar view names
# Add the app name so Django knows which app view to use
app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/2
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # /polls/2/results
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/2/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]