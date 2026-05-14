# 114
# Crie um código em python que teste se o site pudim.com.br está acessível pelo computador usado
import requests

try:
    site =  requests.get('http://www.pudim.com')
except requests.exceptions.ConnectionError:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')

