#Importando bibliotecas necessarias 
import urllib
import urllib.request
try:
#tentando acessar o site
    resposta = urllib.request.urlopen('https://pudim.com.br/')
#Retornando as informacoes (conforme o sucesso ou  a falha) 
except Exception as erro:
    print(f'\033[31mO site do Pudim não esta acessivel no momento\033[m')

else:
    print('\033[32mConsegui acessar o site do Pudim\033[m')
