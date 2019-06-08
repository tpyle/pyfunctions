import sys
import getpass
import builtins
import os

from requests import Session
from zeep import Client
from zeep.transports import Transport
from .pfail import pfail

# Override so it prompts over stderr
def raw_input(prompt=None):
    if prompt:
        sys.stderr.write(str(prompt))
        return builtins.raw_input()

# I need to make a closure to remember these things
def getFunc ( _nas, funcstr ):
    return lambda self,args: getattr(_nas, funcstr)(self.addsession(args))

class Nas:
    sessionid = None
    # Appends the sessionid to the arguments
    def addsession(self,args):
        args['sessionid'] = self.sessionid
        return args
    # Initializes the client and logs in
    def __init__(self,clientstring='api.wsdl.gsoap', login=None):
        username = ''
        password = ''
        i = 0
        for arg in sys.argv:
            if arg == '--user':
                if i+1 >= len ( sys.argv ):
                    pfail ( 'No Username' )
                username  = sys.argv[i+1]
            elif arg == '--pass':
                if i+1 >= len ( sys.argv ):
                    pfail ( 'No Password' )
                password = sys.argv[i+1]
            i += 1

        if username == '':
            username = input('Username: ')
        if password == '':
            password = getpass.getpass()

        nassession = Session()
        nassession.trust_env = False
        nassession.verify = False
        _nas = Client(os.path.join(os.path.dirname(__file__), clientstring), transport=Transport(session=nassession)).service
        try:
            sessionid = _nas.login({'username': username, 'password': password}).Text
            res = None
            if login != None:
                res = login(username, password)
            self.sessionid = sessionid
            for func in dir(_nas):
                if not func.startswith('_'):
                    setattr(Nas, func, getFunc(_nas,func))

        except:
            pfail ( 'Invalid Credentials' )
