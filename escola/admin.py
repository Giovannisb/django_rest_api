from django.contrib import admin
from escola.models import *

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_link = ('id', 'nome')
    search_field = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_link = ('id', 'codigo_curso')
    search_field = ('codigo_curso',)
    
admin.site.register(Curso, Cursos)
