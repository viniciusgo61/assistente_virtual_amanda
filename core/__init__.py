import datetime



class SystemInfo:
    def __init__(self):
        pass

    def get_time():
        now=datetime.datetime.now()
        resposta='São {} horas e {} minutos.'.format(now.hour,now.minute)
        return resposta