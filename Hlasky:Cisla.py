text = input("Zadaj text: ")
cislice = 0
male = 0
velke = 0
for c in text:
    if c >= '0' and c <= '9':
        cislice += 1
    elif c >= 'A' and c <= 'Z':
        velke += 1
    elif c >= 'a' and c <= 'Z':
        male += 1
            
print("Číslic je ", cislice)
print("Malých písmen je", male)
print("Veľkých písmen je", velke)
