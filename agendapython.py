#!/bin/python3

# este comentário visa testar a pipeline

import mysql.connector

# Declaração de funções para manipulação por menu

# Adicionar pessoa
def add_someone(): 
    print("   Inclusão de novo Contato   \n")

    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    db_connection = mysql.connector.connect(host="localhost",
                                            user="root", 
                                            passwd="123123", 
                                            database="agendamuitoshow")
    
    cursor = db_connection.cursor() #define a adição de dados
    sql = "INSERT INTO contatos (nome, telefone,email) VALUES (%s, %s, %s)"
    valores = (nome, telefone, email)
    cursor.execute(sql, valores)
    print(f"\n O contato {nome} foi inserido com sucesso. \n")
    cursor.close()
    db_connection.commit()
    db_connection.close()


# Editar dados de um usuário
def edit_some():
    print("\n  --- Edição de Contato ---  \n")

# solicita o nome da pessoa que terá dados alterados
    nome_alt = input("Digite o nome para edição: ")
    db_connection = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="123123", 
                                            database="agendamuitoshow")
    
    cursor = db_connection.cursor()

    sql = "SELECT pid FROM contatos WHERE nome = %s"
    cursor.execute(sql, (nome_alt,))
    linhas = cursor.fetchall()
    resultados = cursor.rowcount
    for i in linhas:
        identif = i[0]

    if resultados > 0:
        print(f"Contato encontrado:  {nome_alt} \n")
        nome_mod = input("Digite o novo nome: ")
        tel_mod = input("Digite o novo telefone: ")
        mail_mod = input("Digite o novo email: ")

        cursorup = db_connection.cursor()
        sqlup = """
        UPDATE contatos SET nome = %s, #altera de fato os dados
        telefone = %s, email = %s WHERE pid = %s;
        """
        valoresup = (nome_mod, tel_mod, mail_mod, identif)
        cursorup.execute(sqlup, valoresup)
        db_connection.commit()
        cursorup.close()

        db_connection.close()
        print("  ")
        print("Usuário alterado com sucesso!!!")
        print("  ")

    else:
        print("Usuário digitado não encontrado.")

# função para deletar pessoa da lista
def delete_some():
    print("   Exclusão de Contatos   ")
    print("  ")

# solicita o nome da pessoa a ser removida
    nome = input("Digite o nome do contato para excluir: ")
    db_connection = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="123123", 
                                            database="agendamuitoshow")
    cursor = db_connection.cursor()

    sql = "SELECT pid FROM contatos WHERE nome = %s;"
    cursor.execute(sql, (nome,)) #compara o nome aos existentes no banco
    linhas = cursor.fetchall()
    resultados = cursor.rowcount
    for i in linhas:
        identif = i[0]

    if resultados > 0:

        print(" ")

        cursorup = db_connection.cursor()
        sqldel = "DELETE FROM contatos WHERE pid = %s;"
        valoresdel = (identif,)
        cursorup.execute(sqldel, valoresdel)
        db_connection.commit()
        cursorup.close()

        db_connection.close()
        print(f"\n Contato {nome}, REMOVIDO com sucesso!!! \n")

    else:
        print("Usuário digitado não encontrado.")


def list_all():
    
    print("Lista de todos os contatos da agenda \n")

    db_connection = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="123123", 
                                            database="agendamuitoshow")
   
    cursor = db_connection.cursor()
    sql = "SELECT nome,telefone,email, pid FROM contatos ORDER BY nome ASC;"
    cursor.execute(sql)
    linhas = cursor.fetchall()
    resultados = cursor.rowcount
    
    for i in linhas:
        print(f"""
        Nome:  {i[0]} \n
        Telefone:  {i[1]} \n
        E-mail:  {i[2]} \n
        PID: {i[3]}
        """)

    cursor.close()
    db_connection.commit()
    db_connection.close()


def search_some():
    print("   Busca por dados de um contato na Agenda   \n")

    nome = input("Digite o nome do contato para exibir: ")
    db_connection = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="123123",
                                            database="agendamuitoshow")
    cursor = db_connection.cursor()

    sql = "SELECT nome,telefone,email, pid FROM contatos WHERE nome = %s;"
    cursor.execute(sql, (nome,))
    linhas = cursor.fetchall()
    resultados = cursor.rowcount

    if resultados > 0:
        for i in linhas:
            print(f"""
            Nome:   {i[0]} \n
            Telefone: {i[1]} \n
            Email: {i[2]} \n
            PID:   {i[3]} \n
            """)

        cursor.close()
        db_connection.commit()
        db_connection.close()

    else:
        print("Usuário digitado não encontrado.")


def delete_all():
    print("   VOCÊ VAI EXCLUIR TODOS OS CONTATOS   ")

    confirma = input("DIGITE 1 PARA CONFIRMAR: ")
    db_connection = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="123123",
                                            database="agendamuitoshow")

    if confirma == "1":
        cursor = db_connection.cursor()
        cursorup = db_connection.cursor()
        sqldel = "TRUNCATE TABLE contatos"
        cursorup.execute(sqldel)
        db_connection.commit()
        cursorup.close()

        db_connection.close()
        print("  ")
        print("Todos os usuários da tabela foram removidos.")
        print("  ")
    else:
        print("OK! Nada foi excluido.")


def iniciar_menu_principal():
    while True:
        print(f""" {'-' * 30}
        \n Bem vindo à Agenda de Contatos
        \n {'-' * 30}
        \n Digite a opção desejada:
        \n 1 Incluir um contato
        \n 2 Editar um contato
        \n 3 Excluir um contato
        \n 4 Listar todos os contatos
        \n 5 Buscar um contato
        \n 6 Excluir todos os contatos
        \n 7 Sair da Agenda 
        \n"""
        )
        
        opcao = int(input("Insira a opcao desejada:   "))

        if opcao == 1:
            add_someone()
        elif opcao == 2:
            edit_some()
        elif opcao == 3:
            delete_some()
        elif opcao == 4:
            list_all()
        elif opcao == 5:
            search_some()
        elif opcao == 6:
            delete_all()
        elif opcao == 7:
            print("""
                  Encerrando a agenda, volte sempre :D
                  """)
            break
        else:
            print("Por favor, informe apenas opções no menu")


iniciar_menu_principal()
