# Importa path
from django.urls import path

# Importa views
from . import views


# Lista URLs
urlpatterns = [

    # Página inicial
    path(
        '',
        views.home_view,
        name='home'
    ),

    # Login aluno
    path(
        'login/aluno/',
        views.student_login_view,
        name='student_login'
    ),

    # Login professor
    path(
        'login/professor/',
        views.teacher_login_view,
        name='teacher_login'
    ),
    
    #logout
    path(
    'logout/',
    views.logout_view,
    name='logout'
),
    
    path(
    'dashboard/professor/',
    views.teacher_dashboard_view,
    name='teacher_dashboard'
),

]