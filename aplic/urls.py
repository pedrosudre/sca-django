from django.urls import path
from .views import IndexView, SobreView, ProfessoresView, CursoDetalheView, DadosGraficoAlunosView, ContatoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('professores/', ProfessoresView.as_view(), name='professores'),
    path('curso-detalhe/<int:id>/', CursoDetalheView.as_view(), name='curso-detalhe'),
    path('dados-graficos-alunos/', DadosGraficoAlunosView.as_view(), name='dados-graficos-alunos'),
]