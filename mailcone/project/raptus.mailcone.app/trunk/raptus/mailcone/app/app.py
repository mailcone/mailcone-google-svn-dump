import grok, os

#from zope.app.authentication.authentication import PluggableAuthentication
#from zope.app.security.interfaces import IAuthentication

from hurry.query.query import Query
from hurry.query.interfaces import IQuery

from z3c.relationfield import RelationCatalog
from zc.relation.interfaces import ICatalog

from raptus.mailcone.core.interfaces import IMailcone


class Mailcone(grok.Application, grok.Container):
    grok.implements(IMailcone)
    #grok.local_utility(PluggableAuthentication, provides=IAuthentication, setup=auth.setup_authentication)
    grok.local_utility(Query, provides=IQuery)
    grok.local_utility(RelationCatalog, provides=ICatalog)
