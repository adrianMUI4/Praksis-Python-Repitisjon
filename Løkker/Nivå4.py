# hemmeligtall = 7
# gjett = -1
# while gjett != hemmeligtall:
#     gjett = int(input("Gjett fram til det hemmelige tallet: "))
#     if gjett < hemmeligtall:
#         print("for lavt")
#     elif gjett > hemmeligtall:
#         print("For høyt")
# print("Riktig")



# handleliste = []

# while True:
#     vare = input("Skriv inn varen du vil ha (skriv ferdig for å avslutte): ")

#     if vare.lower() == "ferdig":
#             break
    
#     handleliste.append(vare)

# print("Du skal handle:")
# print(handleliste)





sum = 0
antall = (int(input("hvor mange tall vil dere legge sammen? ")))

for i   in range(antall):
    tall = int(input("Skriv inn et tall: "))
    sum = sum + tall

print("Total summen er:", sum)







    