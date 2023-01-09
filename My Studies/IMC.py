# IMC
import math
peso = float(input('Insira seu peso:'))
alt = float(input('Insira sua altura:'))
nalt = alt * alt
calc = peso / nalt
print('Seu imc é de:', math.floor(calc))
if calc < 18.5:
    print('Você está abaixo do peso')
elif calc >= 18.5 and calc <= 25:
    print('Você está no peso ideal')
elif calc > 25 and calc <= 30:
    print('Você está com sobrepeso')
elif calc > 30 and calc <= 40:
    print('Você está obeso')
elif calc > 40:
    print('Você está com obesidade mórbida')
