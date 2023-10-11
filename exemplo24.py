
import random as rnd

def calcula_media(v):
    if len(v)>0:
        return sum(v)/len(v)
    else:
        return 0    
def inicializa_lista(quantidade = 5):
    lista=[]
    for _ in range(quantidade):
        valor = rnd.randint(0,100)
        lista.append(valor)
    return lista    
def pesquisar_valor(v, valor_pesquisa):
    indices = []
    for i, item in enumerate(v):
        if item == valor_pesquisa:
            indices.append(i)
    return indices
def menu():
    print('='*10)
    print('1- iniciar lista aleatório')
    print('2- calcular media')    
    print('3- pesquisar valor')
    print('4- sair')
    return int(input('Digite sua opção: '))
#main
if __name__=='__main__':
    v = [10,20,30,40]
    op = 0
    while op !=4:
        op = menu()
        if op==1:
            v = inicializa_lista()  
            print(v)  
        elif op == 2:
            media = calcula_media(v)
            print(f'a média é {media:.2f}')
        elif op == 3:
            pesquisa_valor = int(input('Digite o valor a ser pesquisado: '))
            indices = pesquisar_valor(v, pesquisa_valor)
            if indices:
                print(f'O valor {pesquisa_valor} foi encontrado nas posições:{indices}')
            else:
                print(f'O valor {pesquisa_valor} não foi encontrado na lista.')
    else:
        print('saindo...')    
    #media = calcula_media(v)
    #print(v)
    #print(f'a média é {media}')