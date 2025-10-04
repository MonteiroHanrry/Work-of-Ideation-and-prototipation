fila =[]
while True:
    print('\n--- Sistema de Fila de Atendimento---')
    print('1 - Adicionar Padawan na fila')
    print('2 - Chamar próximo padawan')
    print('3 - ver fila atual')
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
            print('Nenhum Debiloide na fila para chamar.')
    elif opcao == '3':
        print('Fila atual de padawans:', fila)
    elif opcao == '4':
        print('''⠀
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
              até mais!''')
        break
    else:
        print('Opção inválida, tente novamente.')
