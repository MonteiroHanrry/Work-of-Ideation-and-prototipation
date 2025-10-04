numeros = []
for i in range(10):
    n = int(input(f'Digite o {i+1}º número: '))
    numeros.append(n)
    print('Números menores que 20:')
    for n in numeros:
        if n < 20:
            print(n)
