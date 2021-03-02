import fileinput

listzoom = []
occu = 1
tampon = ''
text = ""

for line in fileinput.input():
    tp = line.split(",")
    #print(line.rstrip())
    #print(tp)

    tp1 = tp[1].split("\t")

    if(tp1[0].isdigit() and len(tp1[0])==3):
        tp2 = tp1[1].split("/")

        # Vérifier si la url suit la forme réquis : /map/1.0/slab/photo/256/16/32798/22739
        if(tp2[1]== 'map' and tp2[2]== '1.0' and tp2[3]== 'slab' and tp2[5].isdigit() and tp2[6].isdigit() and tp2[7].isdigit()):
            # Vérifie si le viewmode a changé 
            if(tp2[4]==tampon):
                occu += 1

                # Vérifie si le niveau de Zoom est déjà dans la liste des zoom
                if(not(tp2[6]in listzoom)):
                    listzoom.append(tp2[6])
            else :
                # Vérifie si c'est la première ligne 
                if(fileinput.isfirstline()):
                    occu = 1 
                    tampon = tp2[4]
                    listzoom = []
                    listzoom.append(tp2[6])
                else :
                    text = tampon +'\t'+ str(occu) + '\t' + ','.join(listzoom) + '\n'
                    sys.stdout.write(text)
                    occu = 1 
                    tampon = tp2[4]
                    listzoom = []
                    listzoom.append(tp2[6])
text = tampon +'\t'+ str(occu) + '\t' + ','.join(listzoom) + '\n'
sys.stdout.write(text)
