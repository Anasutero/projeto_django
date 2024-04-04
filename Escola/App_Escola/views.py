from django.shortcuts import render
from hashlib import sha256
from .models import Professor,Turma,Atividade
from django.db import connection, transaction
from django.contrib import messages

def abre_index(request):
    return render(request, 'login.html')


def initial_population():
    print("Vou popular")

    cursor = connection.cursor()

    #tabela professor
    senha= "123456" #senha inicial para todos usuarios
    senha_armazenar = sha256(senha.encode()).hexdigest()

    #montagm da instrução do sql
    insert_sql_professor = "INSERT INTO App_Escola_professor (nome, email,senha) VALUES"
    insert_sql_professor = insert_sql_professor + "('Prof. Barak Obama', 'barak.obama@gmail.com', '" + senha_armazenar +"'),"
    insert_sql_professor = insert_sql_professor + "('Profa. Angela Merkel', 'angela.merkel@gmail.com', '" + senha_armazenar +"'),"
    insert_sql_professor = insert_sql_professor + "('Prof. Xi Jinping', 'xi.jinping@gmail.com', '" + senha_armazenar +"')"

    cursor.execute(insert_sql_professor)
    transaction.atomic()#nrecessario commit para insert e update
    #fim da tabela professor


    #tabela turma
    #inserir dados
