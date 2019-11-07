from django.shortcuts import render
from django.db import connections, Error


def painel_monitoramento(request):

    # def teste():
    #     with connections['BaseMediar'].cursor() as cursor:
    #         try:
    #             cursor.execute('''select * from monitoring_logportal a
    #                             inner join [dbo].[auth_user] b
    #                             on a.fk_usuario_id = b.id
    #                             where is_superuser = 0
    #                             and username not in('demo_brasil', 'CONTROLE', 'Mediar_Testes', 'Mediar_Ingles')''')
    #             rows = cursor.fetchall()
    #             return rows
    #         except Error as e:
    #             sqlstate = e.args[0]
    #             if sqlstate == '28000':
    #                 print('Erro de senha !')

    with connections['BaseMediar'].cursor() as cursor:
        cursor.execute('''select * from monitoring_logportal a 
                                inner join [dbo].[auth_user] b  
                                on a.fk_usuario_id = b.id
                                where is_superuser = 0
                                and username not in('demo_brasil', 'CONTROLE', 'Mediar_Testes', 'Mediar_Ingles')''')
        resultado = cursor.fetchall()
        data = [dict((cursor.description[i][0], value) for i, value in enumerate(rows))for rows in resultado]

        for alias in connections:
            print(alias)

        return data

    context = {
        'base': data
    }

    template_name = 'mediar/monitoramento.html'
    return render(request, template_name, context)
