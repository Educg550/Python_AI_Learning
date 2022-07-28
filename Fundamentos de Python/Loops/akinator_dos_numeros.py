# -*- coding: utf-8 -*-
print("Sou seu computador...")
print("Tentarei adivinhar o número que você está pensando (entre 1 e 100)")
ini, meio, fim = 1, 50, 100
tentativas = 1
achou = bool(int(input("Seu número é {}? (Digite 0 ou 1) ".format(meio))))
while(not achou):
    tentativas += 1
    opcao = str(input('Ele é "maior" ou "menor"? '))
    if opcao == "maior":
        ini = meio
        meio = (ini + fim) // 2
    elif opcao == "menor":
        fim = meio
        meio = (ini + fim) // 2
    achou = bool(int(input("Seu número é {}? (Digite 0 ou 1) ".format(meio))))

print("Adivinhei! Seu número é {}".format(meio))
print("Levei {} tentativas para descobrir!".format(tentativas))