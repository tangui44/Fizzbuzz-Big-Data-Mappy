import csv
import sys

pathE= sys.argv[1]
pathS = sys.argv[2]

ligne = open(pathE,"r") # Lecture du fichier d'entrée 
r = ligne.readlines()
print(len(r))

listzoom = []
occu = 1
tampon = ''

myfile = open(pathS, 'w') # Création du fichier de sortie 
mywriter = csv.writer(myfile, delimiter='\t', dialect='excel', lineterminator='\n')

for row in r:
    tp = row.split(",")
    tp1 = tp[1].split("\t")

    if(tp1[0].isdigit() and len(tp1[0])==3):
        tp2 = tp1[1].split("/")

        # Vérifier si la url suit la forme réquis : /map/1.0/slab/photo/256/16/32798/22739
        if(tp2[1]== 'map' and tp2[2]== '1.0' and tp2[3]== 'slab' and tp2[5]== '256' and tp2[6].isdigit() and tp2[7].isdigit() and '\n' in tp2[8]):
            tep = tp2[8].split('\n')

            # Vérifie si la dernière partie de l'url est un entier 
            if(tep[0].isdigit()):
                # Vérifie si le viewmode a changé 
                if(tp2[4]==tampon):
                    occu += 1

                    # Vérifie si le niveau de Zoom est déjà dans la liste des zoom
                    if(not(tp2[6]in listzoom)):
                        listzoom.append(tp2[6])
                    # Vérifie si c'est la dernière ligne 
                    if(row == r[len(r)-1]) :
                        # on écrit sur le fichier de sortie 
                        mywriter.writerow([tampon,str(occu),' '.join(listzoom) ])
                else :
                    # Vérifie si c'est la première ligne 
                    if(row == r[0]):
                        occu = 1 
                        tampon = tp2[4]
                        listzoom = []
                        listzoom.append(tp2[6])
                    # Vérifie si c'est la dernière ligne 
                    elif(row == r[len(r)-1]) :
                        mywriter.writerow([tampon,str(occu),' '.join(listzoom) ])
                        occu = 1 
                        tampon = tp2[4]
                        listzoom = []
                        listzoom.append(tp2[6])
                        mywriter.writerow([tampon,str(occu),' '.join(listzoom) ])
                    else :
                        mywriter.writerow([tampon,str(occu),' '.join(listzoom) ])
                        occu = 1 
                        tampon = tp2[4]
                        listzoom = []
                        listzoom.append(tp2[6])
                    


