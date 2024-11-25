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
