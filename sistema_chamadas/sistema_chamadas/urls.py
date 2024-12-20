from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from alunos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/', include('alunos.urls')),
    path('api/materias/', include('materias.urls')),
    path('api/professores/', include('professores.urls')),
    path('api/presencas/', include('presencas.urls')),
    
    # Views HTML para o CRUD dos alunos
    path('alunos/', views.alunos_index, name='alunos_index'),
    path('alunos/create/', views.alunos_create, name='alunos_create'),
    path('alunos/edit/<int:id>/', views.alunos_edit, name='alunos_edit'),
    
    # Views para user
    path('api/users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
