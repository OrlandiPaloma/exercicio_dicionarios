perguntas = {
    'Pergunta 1' : {
        'pergunta': "Quanto é 2+2? ",
        'respostas': {'a': '1', 'b': '4', 'c': '3', 'd': '5'},
        'resposta_certa': 'b',
    },
     'Pergunta 2' : {
        'pergunta': "Quanto é 3*2? ",
        'respostas': {'a': '2', 'b': '4', 'c': '6', 'd': '12'},
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0 #será usado como contador a cada acerto e após usando na porcetagem.

for cp, cr in perguntas.items():
    print(f'{cp}: {cr["pergunta"]}')

    print('Respostas: ')
    for rk, rv in cr['respostas'].items():
        print(f'[{rk}]: {rv}')


    print()
    resposta_usuario = input("Digite sua resposta: ")


    if resposta_usuario == cr['resposta_certa']:
        print("Voce acertou")
        respostas_certas += 1
    else:
        print("voce errou")

    print()

qtd_pergunta = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_pergunta * 100
print(f'Você acertou {porcentagem_acerto}%')