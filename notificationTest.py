import notifyServer
import util
import threading
import time




def serverThreadFunc(server,condition):

    print('starting server thread')
    server.start()






def w():
    print('ha')

def lol(**kwargs):
    if not kwargs['a']:
        print('still working')
    else:
        print('Suck it %s' % kwargs['a'])

commands ={'lol':lol, 'w':w}


server = notifyServer.getServer(commands = commands)
server.start()
