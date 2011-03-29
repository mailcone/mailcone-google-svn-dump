# grok stuff
import grok

from mailfilter.interfaces import IConfiglet

class RuleSetConfiglet(grok.GlobalUtility):
    """ Utility provide a gui to manage rule sets """
    grok.implements(IConfiglet)
    grok.name('RuleSetConfiglet')

    id = 'RuleSetConfiglet' # defines link id
    title = 'rule sets' # defines link content
    url = 'rulesetConfiglet'

#XXX move to mfa_core_auth
class UserConfiglet(grok.GlobalUtility):
    """ Utility provide a gui to manage users """
    grok.implements(IConfiglet)
    grok.name('UserConfiglet')

    id = 'UserConfiglet' # defines link id
    title = 'users' # defines link content
    url = 'userConfiglet'
    
class AppConfiglet(grok.GlobalUtility):
    """ Utility provide a gui to manage users """
    grok.implements(IConfiglet)
    grok.name('AppConfiglet')

    id = 'AppConfiglet' # defines link id
    title = 'app settings' # defines link content
    url = 'appConfiglet'