import grok, os

#from zope.app.authentication.authentication import PluggableAuthentication
#from zope.app.security.interfaces import IAuthentication

from raptus.mailcone.core.interfaces import IMailcone
from raptus.mailcone.customers.interfaces import ICustomersContainerHolder



class Mailcone(grok.Application, grok.Container):
    grok.implements(IMailcone,
                    ICustomersContainerHolder)
    #grok.local_utility(PluggableAuthentication, provides=IAuthentication, setup=auth.setup_authentication)
