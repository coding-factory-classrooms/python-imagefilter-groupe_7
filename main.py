from fonction import gray, flou, latter
import sys

try:

    dossier_entrance = "images"
    dossier_exit = "images2.0"

    args = sys.argv
    try:
        if args[1] == 'gray':
            gray(dossier_entrance,dossier_exit)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == 'flou':
                    flou(dossier_exit, dossier_exit)
                elif arg == 'latter':
                    latter(dossier_exit,dossier_exit)

        elif args[1] == 'flou':
            flou(dossier_entrance, dossier_exit)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == 'gray':
                    gray(dossier_exit, dossier_exit)
                elif arg == 'latter':
                    latter(dossier_exit,dossier_exit)

        elif args[1] == 'latter':
            latter(dossier_entrance, dossier_exit)
            for i in range(2, len(args)):
                arg = args[i]
                if arg == 'flou':
                    flou(dossier_exit, dossier_exit)
                elif arg == 'gray':
                    gray(dossier_exit,dossier_exit)
    except IndexError as e:
        print('mettre une option de filtre')
except FileNotFoundError as e:
    print('dossier inexistant')



