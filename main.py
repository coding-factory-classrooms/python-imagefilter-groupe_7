from fonction import gray, flou, latter
import sys
import os

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
            print("--flou permet de flouter l'image")
            print("--latter permet de dilatter les pixels")
            print("")

    try:
        if args[1] == '--gray':
            gray(dossier_entrance,dossier_exit)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == '--flou':
                    flou(dossier_exit, dossier_exit)
                elif arg == '--latter':
                    latter(dossier_exit,dossier_exit)

        elif args[1] == '--flou':
            flou(dossier_entrance, dossier_exit)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == '--gray':
                    gray(dossier_exit, dossier_exit)
                elif arg == '--latter':
                    latter(dossier_exit,dossier_exit)

        elif args[1] == '--latter':
            latter(dossier_entrance, dossier_exit)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == '--flou':
                    flou(dossier_exit, dossier_exit)
                elif arg == '--gray':
                    gray(dossier_exit,dossier_exit)
    except IndexError as e:
        print('mettre une option de filtre')
except FileNotFoundError as e:
    print('dossier inexistant')

