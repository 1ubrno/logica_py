    #Função : Algoritmo para ler largura e altura de uma parede, caucular a área a ser pintada e a quantidade de  tinta nescessária.
    #Cada litro de tinta pinta uma área de 2mts²
    #Autor : Bruno
    #Data : 9/7/25
    #Lista de Exercícios do Curso Em Video - Prof: Gustavo Guanabara

altura = float(input('Qual a altura da parede em metros?'))
largura = float(input('Qual a largura da parede em metros?'))
tinta =  (altura * largura) / 2

print(f'Sua parede tem {altura} Metros de altura e {largura} metros de largura')
print(f'Voce precisara de {tinta}L de tinta')
