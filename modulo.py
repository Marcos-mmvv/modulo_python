
from datetime import date

def exibir_menu():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\nBrasília {dia} de {meses[mes -1]} de {ano}.\n')
    print('1 - Calcular a área do quadrilátero')
    print('2 - Calcular a área do círculo')
    print('3 - Calcular a área do triângulo')
    print('4 - Calcular a área do trapézio')
    print('5 - Sair do programa \n')

#Função do quadrilátero
def calcular_quadrilateros(b, h):
    a = b * h
    return a

# Função da circunferência
def calcular_circulo(r):
    a = 3.14*r**2
    return a

# Função do triângulo
def calcular_triangulo(b, h):
    a = (b * h)/2
    return a

# Função do trapézio
def calcular_trapezio(b_menor, b_maior, h):
    a = ((b_menor + b_maior)*h)/2
    return a


