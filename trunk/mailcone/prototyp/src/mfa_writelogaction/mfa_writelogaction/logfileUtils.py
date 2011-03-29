import grok

from mfa_writelogaction.interfaces import ILogfileUtil

class LogfileUtil(object):
    """ XXX """
    grok.implements(ILogfileUtil)
    
    name = None
    logfile = None
    filepath = None

class InfoLogfileUtil(LogfileUtil, grok.GlobalUtility):
    """ XXX """
    grok.name('info')
    
    name = 'Infolog'
    logfile = ''
    
class ErrorLogfileUtil(LogfileUtil, grok.GlobalUtility):
    """ XXX """
    grok.name('error')
    
    name = 'Errorlog'
    logfile = ''