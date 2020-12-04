from fonction import gray, flou, latter
import sys
import os
import logger

try:
    args = sys.argv

    #dossier d'entrer
    for t in range(0, len(args)):
        arg = args[t]
        if arg == '-i':
            dossier_entrance = f'{args[t + 1]}'

    #dossier de sortie
    for t in range(0, len(args)):
        arg = args[t]
        if arg == '-o':
            dossier_exit = f'{args[t+1]}'
            #creer un dossier avec le nom 'args[t+1]'
            if not os.path.exists(args[t+1]):
                os.mkdir(args[t + 1])

    #fonction help
    for t in range (0, len(args)):
        if args[t] == '-h':
            print("")
            print("----help----")
            print("-o est le dossier de sortie il a besoin d'un nom apres")
            print("-i est le dossier d'entrer il a besoin d'un nom juste apres")
            print("--gray permet de modifier la couleur de l'image pour la mettre en noir et blanc")
            print("--flou permet de flouter l'image et ecrire le degres de flou apres en nombre impair ex : --flou 19")
            print("--latter permet de dilatter les pixelset ecrire le degres de flou apres ex : --latter 10")
            print("")


    for t in range(0, len(args)):
        if args[t] == '--flou':
            floutage = int(args[t+1])


    for t in range(0, len(args)):
        if args[t] == '--latter':
            di = int(args[t+1])


    try:
        if args[1] == '--gray':
            gray(dossier_entrance, dossier_exit)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == '--flou':
                    flou(dossier_exit, dossier_exit, floutage)
                elif arg == '--latter':
                    latter(dossier_exit, dossier_exit, di)
        elif args[1] == '--flou':
            flou(dossier_entrance, dossier_exit, floutage)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == '--gray':
                    gray(dossier_exit, dossier_exit)
                elif arg == '--latter':
                    latter(dossier_exit,dossier_exit, di)

        elif args[1] == '--latter':
            latter(dossier_entrance, dossier_exit, di)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == '--flou':
                    flou(dossier_exit, dossier_exit, floutage)
                elif arg == '--gray':
                    gray(dossier_exit,dossier_exit)
    except IndexError as e:
        print("")
        print('mettre une option de filtre')
except FileNotFoundError as e:
    print("")
    print('dossier inexistant')
except IndexError as e :
    print(e)
except ValueError as e:
    print("")
    print("tu n'as pas mit de valeur")



logger.dump_log()


