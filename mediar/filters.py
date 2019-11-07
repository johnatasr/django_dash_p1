import pyodbc

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


def tabela_graph():

    total= []
    acessos = mediar_data()
    while True:
        objetos = [dict(nome=acesso['first_name'], sobrenome=acesso['last_name'], ultimo_acesso=acesso['last_login']) for acesso in acessos]

        for nome in objetos['nome']:
            aux = ''

            sorted(dicionario, key=lambda k: k['nome_da_coluna'])



        return objetos


nomes = tabela_graph()
print(nomes)

