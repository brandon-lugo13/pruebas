print ('vamos a calcular su indice de masa corporal')
weight = float(input('1. ingrese el valor en kilogramos: '))
height = float(input ('2. ingrese su altura en metros asi: (1.70): '))

bmi = (weight / height ** 2)

print ('su indice de masa corporal  es : ', round(bmi, 2))

if 0<=bmi<=18.5:
  print ('tienes bajo peso')
if bmi>=18.5 and bmi<=24.9:
  print('tienes un peso normal')
if bmi>=25.0 and bmi<=29.9:
  print('tienes sobrepeso')
if bmi>=30.0 and bmi<=100.0:
  print('eres obeso')
if bmi<=0 or bmi>=500.0:
  print ('error')










