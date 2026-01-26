# =========================
# NIVÅ 1
# =========================

# Oppgave 1: Dine første variabler
fornavn = "Adrian"
alder = 18

print(fornavn)
print(alder)
print()

# Oppgave 2: Enkle beregninger
a = 10
b = 3

print("Sum:", a + b)
print("Differanse:", a - b)
print()

# Oppgave 3: Tekst og tall
poeng = 95
print("Du fikk " + str(poeng) + " poeng")
print()


# =========================
# NIVÅ 2 – MED BRUKERINPUT
# =========================

# Oppgave 4: Enkel hilsen
navn = input("Hva heter du? ")
print("Hei " + navn + "!")
print()

# Oppgave 5: Enkel kalkulator
tall1 = int(input("Skriv et tall: "))
tall2 = int(input("Skriv et tall til: "))

print("Summen er:", tall1 + tall2)
print()

# Oppgave 6: Alders-kalkulator
fødselsår = int(input("Hvilket år er du født? "))
alder_2025 = 2025 - fødselsår

print("Du er", alder_2025, "år gammel i 2025")

år = int(input("Hvilket år vil du regne alder for? "))
print("Du er", år - fødselsår, "år i", år)
print()


# =========================
# NIVÅ 3 – LISTER
# =========================

# Oppgave 7: Favoritter (ingen input)
favorittfilmer = ["Inception", "Interstellar", "Matrix", "Gladiator"]

print("Alle filmer:", favorittfilmer)
print("Første film:", favorittfilmer[0])
print("Siste to filmer:", favorittfilmer[2:])
print()

# Oppgave 8: Personlig info med input
navn = input("Navn: ")
alder = input("Alder: ")
favorittfarge = input("Favorittfarge: ")

print(f"Jeg heter {navn}, er {alder} år og liker fargen {favorittfarge}.")
print()

# Oppgave 9: Liste med input
film1 = input("Favorittfilm 1: ")
film2 = input("Favorittfilm 2: ")
film3 = input("Favorittfilm 3: ")

filmer = [film1, film2, film3]
print("Dine favoritter er:", filmer)
print()


# =========================
# NIVÅ 4 – UTFORDRINGER
# =========================

# Oppgave 10: Mini profil-generator
navn = input("Navn: ")
alder = input("Alder: ")
by = input("By: ")
hobby = input("Hobby: ")

print("\n=== PROFIL ===")
print("Navn:", navn)
print("Alder:", alder, "år")
print("Bor i:", by)
print("Hobby:", hobby)
print()

# Oppgave 11: String-eksperiment (ingen input)
ord = "PROGRAMMERING"

print("Små bokstaver:", ord.lower())
print("Store bokstaver:", ord.upper())
print("Bokstaver 3 til 8:", ord[2:8])
print("Baklengs:", ord[::-1])
print()

# Oppgave 12: Avansert kalkulator
tall1 = int(input("Tall 1: "))
tall2 = int(input("Tall 2: "))

print("Sum:", tall1 + tall2)
print("Differanse:", tall1 - tall2)
print("Produkt:", tall1 * tall2)
print("Gjennomsnitt:", (tall1 + tall2) / 2)
print("Største tall:", max(tall1, tall2))
print()


# =========================
# DEBUGGING-OPPGAVER
# =========================

# Oppgave 13: Finn feilen
navn = input("Navnet ditt: ")
print("Hei " + navn + "!")
print()

# Oppgave 14: Type-problem
år = int(input("Hvilket år er det? "))
neste_år = år + 1
print("Neste år er det", neste_år)
print()

# Oppgave 15: Liste-problem
farger = ["rød", "blå", "grønn"]

print("Min favoritt er:", farger[1])
print("Mine to favoritter er:", farger[1:3])
print()

print("Program ferdig 🎉")
