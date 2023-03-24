from django.urls import path

from . import views

urlpatterns = [
    #ex: localhost8080/polls/
    path('', views.index, name='index'),
    #ex: localhost8080/polls/5/
    path('<int:pregunta_id>/',views.detalle, name='detalle'),
    #ex: localhost8080/polls/5/results/
    path('<int:pregunta_id>/results/',views.resultados, name='results'),
    #ex: localhost8080/polls/5/vote/
    path('<int:pregunta_id>/vote/',views.votar, name='vote'),
       
    #ex: localhost8080/polls/5/#/
    path('<int:pregunta_id>/<int:pregunta2_id>/',views.suma, name='suma')
]
