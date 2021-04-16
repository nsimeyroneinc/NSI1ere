#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:19:30 2021

@author: michael
"""

import csv
from collections import OrderedDict   # structure de données utilisée

# On importe le fichier d'exemple de base de données de films
exemple_films_csv = open('films_exemple.csv','r', encoding ='utf-8')
lecteur_exemple = csv.DictReader(exemple_films_csv, delimiter=';')

distribution_csv = open('distribution.csv','r', encoding ='utf-8')
distribution_exemple = csv.DictReader(distribution_csv, delimiter=';')

"""
# Une méthode élémentaire pour créer la liste des enregistrement ligne par ligne
films = []
for ligne in lecteur_exemple:
   films.append(ligne)
"""
#Une méthode plus rapide pour créer la liste des enregistrements
films = list(lecteur_exemple)
distri=list(distribution_exemple)

tab=[]
# On affiche les 5 premiers films
for i in range(len(films)):
    tab.append(films[i]['movie_id'])
print(tab)
print(len(tab))
distribution_exemple1=[]
for k in range(len(distri)):
    print(distri[k]['movie_id'])
    if distri[k]['movie_id'] in tab:
        distribution_exemple1.append(distri[k])
        
print(len(distribution_exemple1))

print(len(films))

def creer_csv(table_donnees, nom_fichier):
    """
    Crée un fichier csv à partir d'une table de données. 
    @param table_donnees : liste de dictionnaires ordonnés
    @param nom_fichier : chaine de caractères, la logique veut qu'elle finisse par l'extension .csv
    """
    en_tete = list(table_donnees[0].keys())
    csv_bis = open(nom_fichier, mode="w", encoding="utf-8", newline = "")
    csv_ecrivain = csv.DictWriter(csv_bis, delimiter =";",fieldnames = en_tete)

    csv_ecrivain.writeheader()
    for ligne in table_donnees:
        csv_ecrivain.writerow(ligne)
        
    csv_bis.close()
    return

creer_csv(distri,"distributions_exemples.csv")