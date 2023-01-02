import math
co = int(input('Valor do cateto oposto:'))
ca = int(input('Valor do cateto adjacente:'))
vco = math.pow(co, 2)
vca = math.pow(ca, 2)
hip = vca + vco
calc = math.sqrt(hip)
