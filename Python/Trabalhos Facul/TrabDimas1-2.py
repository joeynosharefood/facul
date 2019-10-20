codeFunc  = str(input('Insira o codigo do funcionario: '))
horasTrab = int(input('Insira as horas trabalhadas: '))
horasExt1 = int(input('Insira as horas extras tipo 1: '))
horasExt2 = int(input('Insira as horas extras tipo 2: '))
valorHoras = float(input('Insira o valor das horas: '))

salBruto = horasTrab * valorHoras
gratif = salBruto * 0.75
horasExt1 *= (valorHoras * 1.15)
horasExt2 *= (valorHoras * 1.25)
extra = horasExt1 + horasExt2

if salBruto <= 2500:
    desc = salBruto * 0.05
else:
    desc = salBruto * 0.1

salLiq = (salBruto + gratif + extra) - desc

print(round(salLiq, 2))
