import grok, os

#from zope.app.authentication.authentication import PluggableAuthentication
#from zope.app.security.interfaces import IAuthentication

from hurry.query.query import Query
from hurry.query.interfaces import IQuery

from raptus.mailcone.core.interfaces import IMailcone


class Mailcone(grok.Application, grok.Container):
    grok.implements(IMailcone)
    #grok.local_utility(PluggableAuthentication, provides=IAuthentication, setup=auth.setup_authentication)
    grok.local_utility(Query, provides=IQuery)
