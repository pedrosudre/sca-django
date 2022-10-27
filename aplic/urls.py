from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]


from .views import ProfessoresView

path('professores/', ProfessoresView.as_view(), name='professores'),

