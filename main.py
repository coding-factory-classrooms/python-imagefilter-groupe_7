import cv2
import os
import numpy as np

#separe dans notre logique dossier entree/sortie et fichier
dossier_entrance = "images"
dossier_exit = "images2.0"
#1 ouvrir un dossier qui contient des images
files = os.listdir(dossier_entrance)
#2 pous chacune des images les ouvrir avec opencv, appliquer le filtre , enregistrer l'image dans le dossier de sortie
for f in files:
    print(f)
    #TODO rajouter un if pour filtrer les extensions fichiers
    img = cv2.imread(f"{dossier_entrance}/{f}")
    kernel = np.ones((10, 10),np.uint(8))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flou = cv2.medianBlur(img, 15)
    latter = cv2.dilate(img, kernel, 20)
    cv2.imwrite(f"{dossier_exit}/{f}", latter)









