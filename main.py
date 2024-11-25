#afficher l'alphabet en minuscule
import string
alphabet_maj = string.ascii_lowercase
print("alphabet en minuscule :", alphabet_maj)

#affiche l'alphbaet à l'envers
alp_inv = alphabet_maj[::-1]
print(alp_inv)

#prog variable
ma_string = "Je suis une String"
print(ma_string)

#job7
num1 = 40
num2 = 2
print (40 + 2)

#job8
num1 = 3
num2 = 14
print (3 * 14)

#gestion d'un inventaire
nom = "stylo"
prix_unitaire = 1.5
quantite_stock = 2500
#Affichage du produit en console
print("INVENTAIRE")
print(f"Nom du produit :  {nom}")
print(f"Prix Unitaire (€) : {prix_unitaire:.2f} € ")
print(f"Quantite total du stock : {quantite_stock} stylos")
#ajout de prix
quantite_stock += 300
print(quantite_stock)
#quantite de stylos que veut l'utilisateur
while True:
    quantite = input("Quelle quantité de sytlos voulez-vous : ")
    if quantite.isdigit():
        # Conversion de l'entrée en entier si c'est bien un chiffre
        quantite = int(quantite)
        if quantite > quantite_stock:
            print(f"Desolé, il ne reste que: {quantite_stock} stylos")
            continue
        else:
            quantite_stock -= quantite  
            print(f"Vous avez acheté {quantite} stylos.") 
            print(f"Quantité stock restant: {quantite_stock} stylos")

        break
    else:
        print("Entrée invalide. Veuillez entrer un chiffre.")


#augmentation du prix de 10%
augmentation = 10
prix_unitaire_augm = prix_unitaire * (1 + augmentation/100)
print(f"Prix unitaire après inflation : {prix_unitaire_augm:.2f} €")
#Affichage du produit en console après augmentation
print("INVENTAIRE APRES INFLATION DE 10%")
print(f"Nom du produit :  {nom}")
print(f"Prix Unitaire (€) : {prix_unitaire_augm:.2f} € ")
print(f"Quantite total du stock : {quantite_stock} stylos")

#Simulation financiere
#variable pour %invest et taux rendement
invest = 1300
taux_an = 5
#affiche gain annuel en fct du taux de rendement
gain_annuel = invest * (taux_an / 100)
print(f"Le gain annuel est : {gain_annuel:.2f} €")
#augmentation du capital et du % de rendement
invest += 5000
taux_an += 2
gain_annuel = invest * (taux_an / 100)
print(f"Le gain annuel après augmentation est : {gain_annuel:.2f} €")
#diminution du capital et du rendement
invest *= 0.9
taux_an -= 1
gain_annuel = invest * (taux_an / 100)
print(f"Gain après retrait de 10% et diminution du taux de 1% : {gain_annuel} €")


# Chaine qui détermine si e est présent
chaine = input("Entrez une chaine de caractère ? :")

#vérifier si le e est présent
if "e" in chaine:
    print("La lettre e est dans la chaine de caractères.")
else:
    print("La lettre e n'est pas présente dans la chaine de caractères.")



