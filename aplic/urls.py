from django.urls import path
from .views import IndexView, SobreView, ProfessoresView, CursoDetalheView, DadosGraficoAlunosView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('professores/', ProfessoresView.as_view(), name='professores'),
    path('curso-detalhe/<int:id>/', CursoDetalheView.as_view(), name='curso-detalhe'),
    path('dados-graficos-alunos/', DadosGraficoAlunosView.as_view(), name='dados-graficos-alunos'),
]