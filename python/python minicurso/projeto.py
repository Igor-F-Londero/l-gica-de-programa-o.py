#Base de dados
import os
import pandas as pd

# Caminho do diretório onde o script está
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio_script, "Vendas.xlsx")

# Ler o arquivo
tabela_vendas = pd.read_excel(caminho_arquivo)
#Visualizar dados
#pd.set_option('display.max_columns',None)
#print(tabela_vendas)

# Faturamento por loja
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()#filtra a tabela para aparecer somente o nome da loja e o valor final
print(faturamento)
print('-' * 20)
#Quantidade vendida por loja
Quantidade_vendida = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(Quantidade_vendida)
print('-' * 20)
#Ticket médio por produto em cada loja (faturamento / quantidade)
ticket_medio = (faturamento['Valor Final'] / Quantidade_vendida['Quantidade']).to_frame()
print(ticket_medio)


#Enviar e-mail com relatorio
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = ''
mail.subject = 'Teste'
mail.HTMLBody = '''
Prezados, segue o relatorio de vendas por cada loja.

Faturamento:
{faturamento}

Quantidade vendida:
{Quantidade_vendida}

Ticket médio:
{ticket_medio}

att...

'''