import mysql.connector # importando conector SQL/python
import pandas as pd # importando biblioteca pandas para tratar os  dados

""" ESTABELECENDO CONEXÃO """
con = mysql.connector.connect (host="localhost", 
                               database="pokedex",
                               user="root", 
                               password="123123")

cursor = con.cursor

""" VERIFICANDO CONEXÃO """
if con.is_connected():
    print("conexão efetuada ;)")
else:
    print("Tente outra vez como diria raul")

# ATRIBUINDO UMA REQUISIÇÃO NA LINGUAGEM SQL
requisicao = f"select pokemon_number as'No #',pokemon_name as'Name',classfication as'Description', type1 as'type',type2 as'type2'from pokemon;"

# UTILIZANDO A BILIOTECA PANDAS PARA LER OS DADOS
leitura = pd.read_sql(requisicao, con)

# CRIANDO UMA TABELA PARA EXIBIÇÃO NO TERMINAL USANDO
# OS DADOS QUE A BIBLIOTECA MANIPULOU
tabela_linda = pd.DataFrame(leitura)

# POR FIM PRINTAMOS A TABELA
# POR PADRÃO A BIBLIOTECA MOSTRA UM INDICE DO VALOR
# MASCAREI ESSES DAS DOS COM O .to_string(index=False)
print(f""" Esta é sua tabela com dados tratadinhos:
      {'='*50}\n
      {tabela_linda.to_string(index=False)}
      \n{'='*50}\n""")

'''
O resultado esperado para este codigo é uma conexão a um banco de dados chamado
pokedex e extração de uma tabela organizada com os dados 
'''
