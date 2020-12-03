import cv2
import os
import numpy as np


def gray (dossierE , dossierS):
    files = os.listdir(dossierE)

    for f in files:
        img = cv2.imread(f"{dossierE}/{f}")

        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except cv2.error as e:
            print('image pas en jpg/png')

        try:
            cv2.imwrite(f"{dossierS}/{f}", gray)
        except NameError as e:
            print('varible pas crée')
        except cv2.error as e:
            print('')



def flou(dossierE, dossierS):
    files = os.listdir(dossierE)

    for f in files:
        img = cv2.imread(f"{dossierE}/{f}")

        try:
            flou = cv2.GaussianBlur(img, (5, 11), cv2.BORDER_DEFAULT)
        except cv2.error as e:
            print('taille de flou pair ou image pas en jpg/png')

        try:
            cv2.imwrite(f"{dossierS}/{f}", flou)
        except NameError as e:
            print('varible pas crée')
        except cv2.error as e:
            print('')


def latter(dossierE, dossierS):
    files = os.listdir(dossierE)
    kernel = np.ones((10, 10), np.uint(8))

    for f in files:
        img = cv2.imread(f"{dossierE}/{f}")

        try:
            latter = cv2.dilate(img, kernel, 20)
        except cv2.error as e:
            print('image pas en jpg/png')

        try:
            cv2.imwrite(f"{dossierS}/{f}", latter)
        except NameError as e:
            print('varible pas crée')
        except cv2.error as e:
            print('')