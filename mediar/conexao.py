from django.db import connections, Error
import pyodbc
#
# def conexaoSQLServer(driver, server, db, user, pwd):
#     conexao = pyodbc.connect(
#         r'DRIVER={' + driver + '};'
#         r'SERVER=' + server + ';'
#         r'DATABASE=' + db + ';'
#         r'UID=' + user + ';'
#         r'PWD=' + pwd + ';'
#         r'Trusted_Connection=yes;',
#        autocommit=True
#     )
#
#     return conexao
# def mediar_data(self):
#     with connections['BaseMediar'].cursor() as cursor:
#         try:
#             cursor.execute('''select * from monitoring_logportal a
#                             inner join [dbo].[auth_user] b
#                             on a.fk_usuario_id = b.id
#                             where is_superuser = 0
#                             and username not in('demo_brasil', 'CONTROLE', 'Mediar_Testes', 'Mediar_Ingles')''')
#             rows = cursor.fetchall()
#             return rows
#
#
#         except Error as e:
#             sqlstate = e.args[0]
#             if sqlstate == '28000':
#                 print('Erro de senha !')

# def conexao():
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

cursor.close()
for row in cursor:
    print(row)


# conexao = conexaoSQLServer('ODBC Driver 13 for SQL Server',
#                            '10.177.51.52',
#                            'PortalMediar',
#                            'sa',
#                            'jm#srv@1!')





