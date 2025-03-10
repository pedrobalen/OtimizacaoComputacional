import random
n = 50
li = [random.randint(1, 100) for _ in range(n)]
print(li)

media = sum(li) / n
print(media)

diferenca_abaixo = [abs(num - media) for num in li]
minimo = min(diferenca_abaixo)
print(li[diferenca_abaixo.index(minimo)]) 

acima_media = [num for num in li if num > media]
diferenca_acima = [abs(num - media) for num in acima_media]
minimo_acima = min(diferenca_acima)
print(acima_media[diferenca_acima.index(minimo_acima)])
