entrada = input().split('-')
entrada.remove(entrada[0])
lista = [x.split() for x in entrada]
contador = 0
for i in range(len(entrada)):
	entrada[i] = entrada[i].replace(" ","")
for i in range(len(lista)):
    if '1' in lista[i]:
        novaPilha = lista[i]
        posicao = novaPilha.index('1')+1
        if lista[i] == lista[-1]:
            pilhaLateral = lista[i-1]
        elif len(lista[i+1])<= len(lista[i-1]):
                 pilhaLateral = lista[i+1]
        else:
            pilhaLateral = entrada[i-1]


for i in range(len(novaPilha)-posicao):
    contador +=1
    novaPilha = novaPilha[:-1]

for i in range(len(pilhaLateral)-posicao+1):
    contador+=1
    pilhaLateral = pilhaLateral[:-1]
print(contador)
               
