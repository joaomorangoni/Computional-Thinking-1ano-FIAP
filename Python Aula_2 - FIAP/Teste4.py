dist = float(input("Insira a distancia percorrida em km: "))
vel = float(input("Insira a velocidade média em km/h: "))

tempo = dist/vel
h = int(tempo)
m = int((tempo - h) * 60)

print(f"Tempo estimado: {h}:{m}")