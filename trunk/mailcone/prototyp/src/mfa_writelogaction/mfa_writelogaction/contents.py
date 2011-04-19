import grok

from zope.component import getUtility
from zope import event, lifecycleevent

from mailfilter.app import SearchableContentMixin
from mailfilter.interfaces import ISearchableContent
from mfa_core_action.interfaces import IAction, IActionType, IActionContainer
from mfa_writelogaction.interfaces import IWriteLogAction, ILogfile, IWriteLogActionSettingObject

class WriteLogAction(grok.Model, SearchableContentMixin):
    """ Provide a action for write messages in logfiles """
    grok.implements(IWriteLogAction, IAction, ISearchableContent)
    grok.context(IActionContainer)

    id = None
    content_type = 'WriteLogAction'
    sortNr = None
    
    def __init__(self, id, logfile, loglevel, logmessage, match):
        """ Constructor """
        super(WriteLogAction, self).__init__()
        self.id = id
        self.logfile = logfile
        self.loglevel = loglevel
        self.logmessage = logmessage
        self.match = match

    def setSortNr(self, number):
        """XXX"""
        self.sortNr = number
        #reindexing
        event.notify(
            lifecycleevent.ObjectModifiedEvent(self, 
                                               lifecycleevent.Attributes(IWriteLogAction, 'sortNr')
            )
        )
        
    grok.traversable('moveUp')
    def moveUp(self):
        return self.__parent__.moveActionUp(self)

    grok.traversable('moveDown')
    def moveDown(self):
        return self.__parent__.moveActionDown(self)

    def getActionTypeTitle(self):
        """ return title for registered filter type """
        return getUtility(IActionType, "WriteLogActionType").title
    
    def apply(self):
        """ XXX """
        #XXX not implemented yet
        pass

class Logfile(grok.Container, SearchableContentMixin):
    """ Define a logfile - used by WriteLogAction """
    grok.context(IWriteLogActionSettingObject)
    grok.implements(ILogfile, ISearchableContent)
    
    id = None
    name = None
    logfile = None
    logpath = None
    
    def __init__(self, name, logfile, filepath):
        """ Constructor """
        super(Logfile, self).__init__()
        self.id = name.replace(' ', '-') # XXX - really simple, could be done better
        self.name = name
        self.logfile = logfile
        self.filepath = filepath