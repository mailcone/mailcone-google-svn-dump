import grok
from fanstatic import Library, Resource
from zope.component import getUtilitiesFor, getUtility

from mailfilter.resource import rulesetJsExtender
from mailfilter.interfaces import IControlPanelJSExtention
from mfa_core_action.interfaces import IActionType

from mfa_writelogaction.interfaces import ILogfileManager, ILogfileUtil, ILoglevelManager, ILoglevelUtil

class WrtieLogActionType(grok.GlobalUtility):
    """ Utility provide action type write log for filter manager """
    grok.implements(IActionType)
    grok.name('WriteLogActionType')
    
    title = 'write log'
    addFormName = 'addWriteLogAction'
    
class WrtieLogActionJSExtender(grok.GlobalUtility):    
    """ XXX - test"""
    grok.implements(IControlPanelJSExtention)
    grok.name('WrtieLogActionJSExtender')
    jsExtensions = []
    
    def __init__(self):
        library = Library('mfa_writelogaction', 'static')
        extension = Resource(library, 'writelogaction_jsextender.js', depends=[rulesetJsExtender])
        self.jsExtensions.append(extension)

    def listExtensions(self):
        return self.jsExtensions
    
class LogfileManager(grok.GlobalUtility):
    """ XXX """
    grok.implements(ILogfileManager)
    
    def getLogfileKeys(self):
        """ XXX """
        sources = getUtilitiesFor(ILogfileUtil)
        return [source[0] for source in sources]

    def getLogfileUtil(self,id):
        """ XXX """
        return getUtility(ILogfileUtil, id)
    
class LoglevelManager(grok.GlobalUtility):
    """ XXX """
    grok.implements(ILoglevelManager)
    
    def getLoglevelKeys(self):
        """ XXX """
        sources = getUtilitiesFor(ILoglevelUtil)
        return [source[0] for source in sources]
    
    def getLoglevelUtil(self, id):
        """ XXX """
        return getUtility(ILoglevelUtil, id)