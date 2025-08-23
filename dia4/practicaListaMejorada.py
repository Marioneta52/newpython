valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado =[n**2 for n in valores]
print(valores_cuadrado)

valores2 = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[n for n in valores2 if n%2==0]
print(valores_pares)

##
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(c-32)*(5/9) for c in temperatura_fahrenheit]
print(grados_celsius)