from django.urls import path

from . import views

# Namespace (para identificar o 'name' do path() quando houver múltiplos apps, e eventualmente houver path() com mesmo nome). Agora, a URL, ao invés de ser chamada por >>> url 'detail' <<<, deverá ser chamada por >>> url 'polls:detail' <<<
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]