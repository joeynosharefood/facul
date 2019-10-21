entry = str(input('')).split(' ')
alt = float(entry[0])
raio = float(entry[1])

areaExt = 2 * (3.14 * (raio * raio))
areaExt = areaExt + (2 * 3.14 * raio * alt)

totalLtas = (areaExt / 3) / 18

print(round((totalLtas), 2))
print(round((totalLtas * 86.50), 2))
