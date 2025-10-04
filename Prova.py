import time

art = '''
⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠤⠤⠴⠶⠶⠶⠶⠦⠤⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠖⢛⣩⣤⠂⠀⠀⠀⣶⡀⢀⣶⠀⠀⠀⠐⣤⣍⡛⠲⣄⠀⠀⠀⠀
⢀⡴⢋⣴⣾⣿⣿⣿⠀⠀⠀ ⣿⣿⣿⣿⠀ ⠀⠀⣿⣿⣿⣷⣦⡙⢦⡀⠀
⡞⢠⣿⣿⣿⣿⣿⣿⣷⣤⣤⣴⣿⣿⣿⣿⣦⣤⣤⣾⣿⣿⣿⣿⣿⣿⡆⢳⠀
⡁⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢈⠆
⢧⡈⢿⣿⣿⣿⠿⠿⣿⡿⠿⠿⣿⣿⣿⣿⠿⠿⢿⣿⠿⠿⣿⣿⣿⡿⢁⡼⠀
⠀⠳⢄⡙⠿⣇⠀⠀⠈⠁⠀⠀⠈⢿⡿⠁⠀⠀⠈⠁⠀⠀⣸⠿⢋⡠⠞⠀⠀
⠀⠀⠀⠉⠲⢤⣀⡀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⢀⣀⡤⠗⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠐⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠁
'''
for linha in art.splitlines():
    print(linha)
    time.sleep(0.2) 

#LOGIN 
usuario_correto = "Carlos Gustavo"
senha_correta = "ideação123"

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print('É isso! Você entrou, cuidado com o que você faz.')

    #EXERCÍCIO 1: Números menores que 20 
    numeros = []
    for i in range(10):
        n = int(input(f'Digite o {i+1}º número: '))
        numeros.append(n)

    print('Números menores que 20:')
    for n in numeros:
        if  n< 20:
            print(n)
# --- EXERCÍCIO 2: Lista de produtos do supermercado ---
    produtos = ["arroz", "feijão", "macarrão", "açúcar", "café", "leite", "pão", "óleo"]

    produto = input("\nDigite o nome do produto que deseja buscar: ").lower()

    if produto in produtos:
        print(f"O produto '{produto}' está disponível na lista.")
    else:
        print(f"O produto '{produto}' NÃO está disponível na lista.")
    #EXERCÍCIO 3: Sistema de fila
    fila = []
    while True:
        print('\n--- Sistema de Fila de Atendimento ---')
        print('1 - Adicionar Padawan na fila')
        print('2 - Chamar próximo padawan')
        print('3 - Ver fila atual')
        print('4 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome do padawan: ')
            fila.append(nome)
            print(f'{nome} adicionado à fila.')
        elif opcao == '2':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'{atendido} foi chamado para atendimento.')
            else:
                print('Nenhum padawan na fila para chamar.')
        elif opcao == '3':
            print('Fila atual de padawans:', fila)
        elif opcao == '4':
            arte = '''⠀
           ⡀⠐⠉⠁⠀⠉⠉⢻⣶⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀ ⢀⠎⠀⠀⢀⣀⣤⣤⣀⣘⣿⣿⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣏⡀⠀⠀⠈⣉⣻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⠂⠀⠏⣀⡀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣤⣴⠞⢻⣿⠛⢿⣆⠀⠀⣿⣠⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⠟⠀⡘⠋⠉⣙⣻⣇⠀⢹⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⣿⣡⡄⠚⠻⢿⣿⣿⠿⣿⡆⢻⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀
⠀⠀⠀⣿⡿⢿⢆⠀⠀⠥⣖⣿⣿⣿⡈⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠤⠁⠤⢤⣦⣶⣿⣿⣿⣿⣿⣿⣷⣬⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⡿⢿⣿⠿⠛⢻⠛⢿⣿⣿⣿⣿⣿⡿⠿⠛⠀
⠀⠀⠀⠀⠀⣀⡀⢀⣪⣀⣀⠀⣀⣠⣤⣷⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀
⠀⠀⣐⣋⣿⣿⣿⠿⡿⠁⢠⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣠⣾⣿⣿⣿⠁⠀⢠⠁⢠⠏⣿⡿⠁⣸⡝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
Bem vindo ao lado sombrio da força,
              até mais!'''

            for linha in arte.splitlines():
                print(linha)
                time.sleep(0.2)  # controla a velocidade da transição
            break
        else:
            print('Opção inválida, tente novamente.')

else:
    print('Usuário ou senha incorretos. Tente novamente.')
