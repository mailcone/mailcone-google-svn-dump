import grok

from mailfilter.app import MailfilterApp
from mailfilter.interfaces import ISearchableContent
from mailfilter.baseClasses import ActionSettingObject

from mfa_writelogaction.interfaces import IWriteLogActionSettingObject

class WirteLogActionSettingObject(ActionSettingObject):
    """ XXX """
    grok.context(MailfilterApp)
    grok.implements(IWriteLogActionSettingObject, ISearchableContent)
    
    id = 'writeLogActionSettings'
    title = 'Write log action'
    form_name = None