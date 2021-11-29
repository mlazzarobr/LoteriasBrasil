from random import randint
lista = []
espelho = []
num = vmax = tamlista = tipo = qtjogos = i = tc = a = b = 0

listatimes = ['ABC-RN', 'América-MG', 'América-RJ', 'América-RN', 'Americano-RJ', 'Atlético-GO', 'Atlético-MG',
              'Atlético-PR', 'Avai-SC', 'Bahia-BA', 'Bangu-RJ', 'Barueri-SP', 'Botafogo-PB', 'Botafogo-RJ',
              'Bragantino-SP', 'Brasiliense-DF', 'Ceará-CE', 'Corinthians-SP', 'Coritiba-PR', 'CRB-AL', 'Criciúma-SC',
              'Cruzeiro-MG', 'CSA-AL', 'Desportiva-ES', 'Figueirense-SC', 'Flamengo-RJ', 'Fluminense-RJ',
              'Fortaleza-CE', 'Gama-DF', 'Goiás-GO', 'Grêmio-RS', 'Guarani-SP', 'Inter Limeira-SP', 'Internacional-RS',
              'Ipatinga-MG', 'Ituano-SP', 'Ji-Paraná-RO', 'Joinville-SC', 'Juventude-RS', 'Juventus-SP', 'Londrina-PR',
              'Marília-SP', 'Mixto-MT', 'Moto Clube-MA', 'Nacional-AM', 'Náutico-PE', 'Olaria-RJ', 'Operário-MS',
              'Palmas-TO', 'Palmeiras-SP', 'Paraná-PR', 'Paulista-SP', 'Paysandu-PA', 'Ponte Preta-SP', 'Portuguesa-SP',
              'Remo-PA', 'Rio Branco-AC', 'Rio Branco-ES', 'River-PI', 'Roraima-RR', 'Samp Correa-MA', 'Santa Cruz-PE',
              'Santo André-SP', 'Santos-SP', 'São Caetano-SP', 'São Paulo-SP', 'S. Raimundo-AM', 'Sergipe-SE',
              'Sport-PE', 'Treze-PB', 'Tuna Luso-PA', 'U. Barbarense-SP', 'Uberlândia-MG', 'União São João-SP',
              'Vasco-RJ', 'Vila Nova-GO', 'Villa Nova-MG', 'Vitória-BA', 'XV Piracicaba-SP', 'Ypiranga-AP']

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n
        
def randomize(vmax, tamlista):

    while len(lista) < tamlista:
        num = int(randint(1, vmax))
        if num not in lista:
            lista.append(num)
    arruma = sorted(lista)
    n = 0
    while n < (tamlista-1):
        print(f'{arruma[n]} - ', end='')
        n += 1
    print(f'{arruma[n]}')
    for v in range(1, 101):
        if v not in lista:
            espelho.append(v)
    lista.clear()
    

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Loterias Brasil Python.')
    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
