from fonction import gray, flou, latter
import sys

try:
    dossier_entrance = "images"
    dossier_exit = "images2.0"

    args = sys.argv



    for i in range(0, len(args)):
        arg = args[i]
        print(arg)
        if arg == 'gray':
            gray(dossier_entrance,dossier_exit)
        elif arg == 'flou':
            flou(dossier_exit, dossier_exit)
        elif arg == 'latter':
            latter(dossier_entrance, dossier_exit)

except FileNotFoundError as e:
    print('dossier inexistant')

