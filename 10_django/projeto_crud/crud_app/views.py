from django.shortcuts import render, redirect
from .models import Pessoa

# Página inicial: lista todas as pessoas
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {"pessoas": pessoas})


# Página de cadastro de pessoa
def cadastro_pessoa(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")

        Pessoa.objects.create(
            nome=nome,
            email=email,
            cpf=cpf
        )

        return redirect("home")  # volta pra home depois de cadastrar

    return render(request, "cadastrar.html")
