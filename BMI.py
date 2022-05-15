vaha = float (input ('Zadaj váhu v kg: '))
vyska = float (input ('Zadaj svoju výšku v metroch: '))
bmi = float(vaha/vyska**2)
print (bmi)
if bmi <= 19 :
    print ('Podvýživa')
if bmi > 19 and bmi <= 25 :
    print ('Normálna')
if bmi > 25 and bmi <= 30 :
    print ('Nadváha')
if bmi > 30 :
    print ('Obezita')
