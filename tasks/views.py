from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, User
from django.contrib import messages


def task_list(request):
    print("User:", request.user)  # Ajoutez ceci pour déboguer
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'tasks/task_list.html', {'tasks': tasks, 'user': request.user})

    return redirect('login')



@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date', None)

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            user=request.user  # Associe la tâche à l'utilisateur connecté
        )
        return redirect('task_list')

    return render(request, 'tasks/add_task.html')


@login_required
def edit_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)

        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.due_date = request.POST.get('due_date', None)
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    elif request.method == 'GET':
        task_id = request.GET.get('task_id')
        if not task_id:
            return redirect('task_list')

        task = get_object_or_404(Task, id=task_id)
        return render(request, 'tasks/edit_task.html', {'task': task})


@login_required
def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('task_list')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']

        hashed_password = make_password(password)

        User.objects.create(name=name, email=email, password=hashed_password)
        messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter.")
        return redirect('login')
    return render(request, 'tasks/register.html')


def login(request):
    if request.method == 'POST':
        input_email = request.POST['email']
        input_password = request.POST['password']

        print("Session before login:", request.session)  # Pour vérifier l'état de la session

        try:
            registered_user = User.objects.get(email=input_email)
            if check_password(input_password, registered_user.password):
                request.session['email'] = registered_user.email
                messages.success(request, "Vous êtes bien connecté!")
                return redirect('task_list')
            else:
                messages.error(request, "Votre identifiant ou mot de passe est incorrect")
        except User.DoesNotExist:
            messages.error(request, "Votre identifiant ou mot de passe est incorrect")

    return render(request, 'tasks/login.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        messages.success(request, "Vous êtes déconnecté avec succès.")
    return redirect('login')
