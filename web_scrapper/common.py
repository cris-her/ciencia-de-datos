import yaml

__config = None

def config():
    #Acceso a una variable global dentro de la función
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.load(f)

    return __config