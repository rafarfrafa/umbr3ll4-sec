from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import Registro_Usuario
from django.contrib.auth.hashers import make_password
from .models import PerfilUsuario

def Index(request):
    return render(request, 'Sitezinho/index.html')

def login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login com sucesso!')
            return redirect('Index')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'Sitezinho/Login.html')

def admin_login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            auth_login(request, user)
            messages.success(request, 'Login admin com sucesso!')
            return redirect('painel_admin')
        else:
            messages.error(request, 'Credenciais de administrador inválidas.')
    return render(request, 'Sitezinho/admin_login.html')

def logout_View(request):
    auth_logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('Login')

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@login_required
@admin_required
def painel_admin(request):
    usuarios = User.objects.all()
    return render(request, 'Sitezinho/painel_admin.html', {'usuarios': usuarios})

@login_required
@admin_required
def editar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(request, 'Usuário atualizado com sucesso!')
        return redirect('painel_admin')
    return render(request, 'Sitezinho/editar_usuario.html', {'user': user})


@login_required
@admin_required
def deletar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        try:
            # Remove APENAS o que você criou (PerfilUsuario)
            PerfilUsuario.objects.filter(user=usuario).delete()
            usuario.delete()
            messages.success(request, 'Usuário deletado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao deletar usuário: {str(e)}')
        return redirect('painel_admin')
    return render(request, 'Sitezinho/confirmar_deletar_usuario.html', {'usuario': usuario})

def Register_View(request):
    if request.method == 'POST':
        form = Registro_Usuario(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            
            # Certificando-se de que a senha será hashada antes de salvar no banco
            senha_hash = make_password(form.cleaned_data['senha'])
            usuario.senha = senha_hash
            
            usuario.save()
            
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('Login')  # Redireciona para a página de login após o cadastro
    else:
        form = Registro_Usuario()  # Formulário vazio para o GET

    return render(request, 'Sitezinho/Registro.html', {'form': form})