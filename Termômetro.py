print('-*-*-*-*-*-*-*-')
print(' Termômetro CFK')
print('-*-*-*-*-*-*-*-')
temp = float(input('Digite a temperatura atual em celsius:'))
k = temp + 273.15
f = (temp * 9/5) + 32
print('Temperatura em Celsius', temp,"°C")
print('Temperatura em Farenheit', f,'°F')
print('Temperatura em Kelvin', k, '°K')
