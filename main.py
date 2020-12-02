import cv2
import os
import numpy as np


#separe dans notre logique dossier entree/sortie et fichier
try:
    dossier_entrance = "images"
    dossier_exit = "images2.0"
    #1 ouvrir un dossier qui contient des images

    files = os.listdir(dossier_entrance)

    #2 pous chacune des images les ouvrir avec opencv, appliquer le filtre , enregistrer l'image dans le dossier de sortie

    for f in files:
        #TODO rajouter un if pour filtrer les extensions fichiers
        img = cv2.imread(f"{dossier_entrance}/{f}")
        kernel = np.ones((10, 10),np.uint(8))


        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except cv2.error as e:
            print('image pas en jpg/png')


        try:
            flou = cv2.GaussianBlur(img,(5,11),cv2.BORDER_DEFAULT)
        except cv2.error as e:
            print('taille de flou pair ou image pas en jpg/png')


        try:
            latter = cv2.dilate(img, kernel, 20)
        except cv2.error as e:
            print('')


        try:
           cv2.imwrite(f"{dossier_exit}/{f}", flou)
        except NameError as e:
            print('varible pas crée')
        except cv2.error as e:
            print('')


except FileNotFoundError as e:
    print('dossier inexistant')








