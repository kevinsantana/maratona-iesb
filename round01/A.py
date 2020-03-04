from math import pi, ceil

raio = float(input())*100
perimetro = 2*round(pi, 6)*raio
pessoas = ceil(perimetro/175)
print(pessoas)