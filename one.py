import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC26fdf9585b0554c110810eae1ab123e3"
# Your Auth Token from twilio.com/console
auth_token = "bf618a9253894eb725a656b64d9774d6"

client = Client(account_sid, auth_token)
# Minhas primeiras linhas em python
# Em uma empesa de vendas o dono quer aumentar as vendas e colocou um bonus com o primeiro vendedor que atingir 55.000 reais em vendas ganha uma frias no final do ano com tudo pago e pdiu para o time dev mandar uma mensagem no seu celular quando um vendedor atingir 55.000
# Lógica do sistema
# 1- abrir os 6 arquivos em excel com a base de dados do ultimos 6 meses
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# 2- verificar se algum valor e maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'No mês {mes}  alguém bateu a meta. vendedor: {vendedor},vendas: {vendas}')
# 3- se for maior que 55.000 -> envia um sms , com o nome ,mes e as vendas do vededor
        message = client.messages.create(
            to="+5571986820140",
            from_="+19362515357",
            body=f'No mês {mes}  alguém bateu a meta. vendedor: {vendedor},vendas: {vendas}')
        print(message.sid)
