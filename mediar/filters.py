import pyodbc
import datetime
from itertools import groupby
from collections import Counter, OrderedDict

data = []

def mediar_data():
    conn = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};' \
        'Server=10.177.51.52,49318;' \
        'Database=PortalMediar;' \
        'Uid=sa;' \
        'Pwd=jm#srv@1!v2;'
    )

    cursor = conn.cursor()
    cursor.execute('''select * from monitoring_logportal a
                                 inner join [dbo].[auth_user] b
                                 on a.fk_usuario_id = b.id
                                 where is_superuser = 0
                                 and username not in('demo_brasil', 'CONTROLE', 'Mediar_Testes', 'Mediar_Ingles')''')

    result = cursor.fetchall()

    data = [dict((cursor.description[i][0], value) for i, value in enumerate(row))for row in result]

    cursor.close()

    return data
#
#
# def tabela_graph():
#
#     total= []
#     acessos = mediar_data()
#     while True:
#         objetos = [dict(nome=acesso['first_name'], sobrenome=acesso['last_name'], ultimo_acesso=acesso['last_login']) for acesso in acessos]
#         count = [len(list(group)) for key, group in groupby(objetos)]
#
#         # for obj in zip(objetos, count):
#         #     return obj
#         total = list(zip(objetos, count))
#         return total
#
# def graphQntUsuario():
#
#     acessos = mediar_data()
#     nomes = [acesso["first_name"] for acesso in acessos]
#     countnomes = Counter(nomes)
#
#     # s = [(k, countnomes[k]) for k in sorted(countnomes, key=countnomes.get, reverse=True)]
#
#     # for k, v in s:
#     #     count = zip(k,v)
#
#     total = sum(countnomes.values())
#
#     return countnomes, total
#
# def graphQntHora():
#
#     data = mediar_data()
#     horas = [acesso['last_login'] for acesso in data]
#     formated = sorted([hora.strftime("%H:%M") for hora in horas])
#
#     return formated

def graphAcessoPeriodo():
    data = mediar_data()




    print(data)

nomes = graphAcessoPeriodo()
print(nomes)

