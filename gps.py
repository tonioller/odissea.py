print("¿Grados?")
grados = int(input())

print("¿minutos?")
minutos = int(input())

print("¿segundos?")
segundos = int(input())

r = grados + minutos/60 + segundos/3600

print(f"Grados decimales {r}")
