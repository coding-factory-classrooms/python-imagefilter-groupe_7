from _datetime import datetime
log_file = 'imageFilter.log'

def log(msg):
    """
    Permet de dire a quel heure et a quel date une modification
    a etait faite puis de mettre les info de cette modification

    :param msg: message a ecrire dans le log
    """
    now = datetime.now()
    timestamp= now.strftime('%d/%m/%Y %H:%M:%S')
    formatted = f'{timestamp} --{msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')



def dump_log():
    """
    Permet de mettre les info de la fonction log dans un fichier
    """
    with open(log_file,'r') as f :
        print(f.read())