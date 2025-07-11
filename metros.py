#  Função :  Algoritmo que lê uma distância em metros e mostra em outras medidas relativas.
#  M, Km, Hm, Dam, dm, cm, mm
#  Autor :   Bruno
#  Data : 9/7/25
#  Lista de Exercícios do Curso Em Video - Prof: Gustavo Guanabara

dis = int(input('Escreva uma distancia em metros'))
km = float(dis / 1000)
hm = float(dis / 100)
dm = float(dis * 10)
cm = float(dis * 100)
mm = float(dis * 1000)

print(f'sua media em km eh {km}')
print(f'sua media em hm eh {hm}')
print(f'sua media em dm eh {dm}')
print(f'sua media em cm eh {cm}')
print(f'sua media em mm eh {mm}')