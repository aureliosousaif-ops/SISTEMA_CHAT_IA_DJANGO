from django.shortcuts import render, redirect

from .models import Student, Teacher


# =========================
# HOME
# =========================
def home_view(request):

    return render(
        request,
        'users/home.html'
    )


# =========================
# LOGIN ALUNO
# =========================
def student_login_view(request):

    # Mensagem erro
    error = None

    # Verifica POST
    if request.method == 'POST':

        # Pega dados formulário
        registration = request.POST.get('registration')

        birth_date = request.POST.get('birth_date')

        try:

            # Busca aluno
            student = Student.objects.get(

                registration=registration,

                birth_date=birth_date

            )

            # Cria sessão aluno
            request.session['student_id'] = student.id

            request.session['student_name'] = student.name

            # Redireciona chat
            return redirect('/chat/')

        except Student.DoesNotExist:

            error = 'Matrícula ou nascimento inválidos'

    return render(

        request,

        'users/login_student.html',

        {

            'error': error

        }

    )


# =========================
# LOGIN PROFESSOR
# =========================
def teacher_login_view(request):

    # Mensagem erro
    error = None

    # Verifica formulário
    if request.method == 'POST':

        # Dados formulário
        ceap = request.POST.get('ceap')

        birth_date = request.POST.get(
            'birth_date'
        )

        try:

            # Busca professor
            teacher = Teacher.objects.get(

                ceap=ceap,

                birth_date=birth_date

            )

            # Cria sessão professor
            request.session['teacher_id'] = teacher.id

            request.session['teacher_name'] = teacher.name

            # Redireciona dashboard
            return redirect(
                '/dashboard/professor/'
            )

        except Teacher.DoesNotExist:

            error = 'CEAP ou nascimento inválidos'

    return render(

        request,

        'users/login_teacher.html',

        {

            'error': error

        }

    )
    # =========================
# LOGOUT
# =========================
def logout_view(request):

    # Remove sessão
    request.session.flush()

    # Volta home
    return redirect('/')

# =========================
# DASHBOARD PROFESSOR
# =========================
def teacher_dashboard_view(request):

    # Verifica login professor
    if 'teacher_id' not in request.session:

        return redirect(
            '/login/professor/'
        )

    return render(

        request,

        'users/dashboard_teacher.html',

        {

            'teacher_name': request.session.get(
                'teacher_name'
            )

        }

    )