import cv2
import os
import numpy as np
import logger


def gray (dossierE , dossierS):
    global gray
    files = os.listdir(dossierE)

    for f in files:
        img = cv2.imread(f"{dossierE}/{f}")
        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except cv2.error as e:
            print(f'image pas en jpg/png:{f}')


        try:
            cv2.imwrite(f"{dossierS}/{f}", gray)
        except NameError as e:
            print('variable pas créee')
        except cv2.error as e:
            print('')
        logger.log(f'gray = {f}')



def flou(dossierE, dossierS, flouter):
    if flouter <= 0 or flouter % 2 ==0 :
        print('flou level invalide')
    else:
        global flou
        files = os.listdir(dossierE)
        for f in files:
            img = cv2.imread(f"{dossierE}/{f}")

            try:
                flou = cv2.GaussianBlur(img, (flouter, flouter), cv2.BORDER_DEFAULT)
            except cv2.error as e:
                print(f'image pas en jpg/png:{f}')


            try:
                cv2.imwrite(f"{dossierS}/{f}", flou)
            except NameError as e:
                print('varable pas crée')
            except cv2.error as e:
                print('')
            logger.log(f'flou = {f}')


def latter(dossierE, dossierS, di):
    global latter
    files = os.listdir(dossierE)
    kernel = np.ones((di, di), np.uint(8))

    for f in files:
        img = cv2.imread(f"{dossierE}/{f}")

        try:
            latter = cv2.dilate(img, kernel, 20)
        except cv2.error as e:
            print(f'image pas en jpg/png:{f}')

        try:
            cv2.imwrite(f"{dossierS}/{f}", latter)
        except NameError as e:
            print('variable pas crée')
        except cv2.error as e:
            print('')
        logger.log(f'latter = {f}')
