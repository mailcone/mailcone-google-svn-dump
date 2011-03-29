import grok

from mfa_core_action.interfaces import IActionMatchType

class ActionMatchType(object):
    """ XXX """
    grok.implements(IActionMatchType)
    name = None

class ActionMatchTypeMatch(ActionMatchType, grok.GlobalUtility):
    """ XXX """
    grok.name('match')    
    name = 'if match'

class ActionMatchTypeNotMatch(ActionMatchType, grok.GlobalUtility):
    """ XXX """
    grok.name('not match')
    name = 'if does not match'