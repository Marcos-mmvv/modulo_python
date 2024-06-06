# Importar o módulo
import os
from modulo import*

if __name__ == '__main__':
    
    while True:
        exibir_menu()
        opcao = input('Informe a opção desejada: ')
        os.system('cls')

        match opcao:
            case '1':
                b = int(input('Informe o valor da base: '))
                h = int(input('Informe o valor da altura: '))
                print(f'Área do quadrilátero: {calcular_quadrilateros(b, h)}\n')
                continue
            case '2':
                r = int(input('Raio do círculo: '))
                print(f'Área: {calcular_circulo(r)}\n')
                continue
            case '3':
                b = int(input('Informe o valor da base: '))
                h = int(input('Informe o valor da altura: '))
                print(f'Área do triângulo: {calcular_triangulo(b, h)}\n')
                continue
            case '4':
                base_menor = int(input('Informe o valor da base menor: '))
                base_maior = int(input('Informe o valor da base maior: '))
                h = int(input('Informe a altura: '))
                print(f'Área do trapézio: {calcular_trapezio(base_menor, base_maior, h)}\n')
                continue
            case '5':
                break
            
        
        
            