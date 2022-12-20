from django.views.generic import TemplateView, ListView, FormView
from .models import Professor
from .models import Curso
from .models import Disciplina
from .models import Aluno
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import ContatoForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?').all()
        return context

class SobreView(TemplateView):
    template_name = 'about-us.html'


class ProfessoresView(TemplateView):
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super(ProfessoresView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('nome').all()
        return context


class CursoDetalheView(ListView):
    template_name = 'course-detail.html'
    paginate_by = 5
    ordering = 'nome'
    model = Disciplina

    def get_context_data(self, **kwargs):
        context = super(CursoDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs.get('id')
        context['curso'] = Curso.objects.filter(id=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Disciplina.objects.filter(curso_id=id)

class DadosGraficoAlunosView(BaseLineChartView):

    def get_labels(self):
        labels = []
        queryset = Curso.objects.order_by('id')
        for curso in queryset:
            labels.append(curso.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Curso.objects.order_by('id').annotate(total=Count('aluno'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado

class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'), extra_tags='success')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Falha ao enviar e-mail'), extra_tags='danger')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)