# -*- coding: utf-8 -*-
pessoa = dict()
pessoas = list()
while True:
    pessoa['Nome'] = str(input("Nome: "))
    pessoa['Idade'] = int(input("Idade: "))
    pessoa['CPF'] = int(input("CPF (somente números): "))
    opcao = str(input("Quer continuar [s/n]? "))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    if (opcao == 'n'):
        break
print("-=" * 30)
media = 0
for p in pessoas:
    media += p['Idade']
media /= len(pessoas)
print("- O grupo tem {} pessoas;".format(len(pessoas)))
print("- A média da idade é de {} anos;".format(media))
print("- Lista das pessoas acima da idade média: ")
for p in pessoas:
    print("")
    if p['Idade'] > media:
        for k, v in p.items():
            print(f"{k}: {v}")
        print("")
