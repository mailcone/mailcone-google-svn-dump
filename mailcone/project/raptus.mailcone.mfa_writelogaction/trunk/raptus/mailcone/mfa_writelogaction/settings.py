import grok

from zope.component import getUtility
from zope.traversing.api import getPath

from raptus.mailcone.mailfilter.app import MailfilterApp
from raptus.mailcone.mailfilter.interfaces import ISearchableContent
from raptus.mailcone.mailfilter.baseClasses import ActionSettingObject

# catalog stuff
from hurry.query.interfaces import IQuery
from hurry.query import set, Eq, And

from raptus.mailcone.mfa_writelogaction.interfaces import IWriteLogActionSettingObject, ILogfile

class WirteLogActionSettingObject(ActionSettingObject):
    """ XXX """
    grok.context(MailfilterApp)
    grok.implements(IWriteLogActionSettingObject, ISearchableContent)
    
    id = 'writeLogActionSettings'
    title = 'Write log action'
    form_name = None
    
    def getLogfiles(self):
        """ XXX """
        query = getUtility(IQuery)
        return query.searchResults(set.AnyOf(('catalog', 'implements'), [ILogfile.__identifier__,]) & 
                                   Eq(('catalog', 'parent_url'), getPath(self)), 
                                   sort_field=('catalog', 'id'))
    
    def delLogfile(self, obj):
        """ XXX """
        del self[obj.__name__]