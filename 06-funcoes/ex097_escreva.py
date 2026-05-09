# 097
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(mensagem):
    print('=' * (len(mensagem) + 4))
    print(f"{mensagem:^{(len(mensagem) + 4)}}")
    print('=' * (len(mensagem) + 4))


escreva("Consegui fazer essa!")
escreva("Estou aprenedendo e me aprofundando")