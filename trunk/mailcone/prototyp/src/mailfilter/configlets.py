# grok stuff
import grok

from mailfilter.interfaces import IConfiglet, ISettingConfiglet

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

# XXX - should be renamed to SettingConfiglet
class AppConfiglet(grok.GlobalUtility):
    """ Utility provide a gui to manage users """
    grok.implements(IConfiglet)
    grok.name('AppConfiglet')

    id = 'AppConfiglet' # defines link id
    title = 'settings' # defines link content
    url = 'appConfiglet'
    
class AppSettingConfiglet(grok.GlobalUtility):
    """ XXX """
    grok.implements(ISettingConfiglet)
    grok.name('AppSettings')
    
    id = 'AppSettings' # defines link id
    title = 'app' # defines link content
    url = 'appSettings'

class DatabaseSettingConfiglet(grok.GlobalUtility):
    """ XXX """
    grok.implements(ISettingConfiglet)
    grok.name('DatabaseSettings')
    
    id = 'DatabaseSettings' # defines link id
    title = 'database' # defines link content
    url = 'databaseSettings'

#XXX - should be moved to mfa_core_filter
class FilterSettingConfiglet(grok.GlobalUtility):
    """ XXX """
    grok.implements(ISettingConfiglet)
    grok.name('FilterSettings')
    
    id = 'FilterSettings' # defines link id
    title = 'filters' # defines link content
    url = 'filterSettings'

#XXX - should be moved to mfa_core_action    
class ActionSettingConfiglet(grok.GlobalUtility):
    """ XXX """
    grok.implements(ISettingConfiglet)
    grok.name('ActionSettings')
    
    id = 'ActionSettings' # defines link id
    title = 'actions' # defines link content
    url = 'actionSettings'