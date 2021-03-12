import random

print ("Permainan Gunting Batu Kertas")
print ("pilihan :")
print ("1. Batu")
print ("2. Gunting")
print ("3. Kertas")

def permainan ():
    kamu = int(input("Masukan Pilihanmu :"))
    kom = random.choice(["Batu","Gunting","Kertas"])
    if kamu == 1:
        print ("Kamu        : Batu")
        print ("Komputer    :",kom)
        if kom == "Batu":
            print("\t Draw")
        if kom == "Gunting":
            print("\t You Win")
        if kom == "Kertas":
            print("\t You Lose")
    if kamu == 2:
        print ("Kamu        : Gunting")
        print ("Komputer    :",kom)
        if kom == "Batu":
            print("\t You Lose")
        if kom == "Gunting":
            print("\t Draw")
        if kom == "Kertas":
            print("\t You Win")
    if kamu == 3:
        print ("Kamu        : Kertas")
        print ("Komputer    :",kom)
        if kom == "Batu":
            print("\t You Win")
        if kom == "Gunting":
            print("\t Lose")
        if kom == "Kertas":
            print("\t Draw")
permainan()
