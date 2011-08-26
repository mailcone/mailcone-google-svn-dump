import grok

from raptus.mailcone.mailfilter.interfaces import ICopy
from raptus.mailcone.mfa_sendnotificationaction.interfaces import ISendNotificationAction
from raptus.mailcone.mfa_sendnotificationaction.contents import SendNotificationAction

class CopySendNotificationAction(grok.Adapter):
    """ Adapter provide ICopy for send notification objects """
    grok.implements(ICopy)
    grok.context(ISendNotificationAction)
    
    def copy(self, context):
        """ duplicate instance and save new instance in the given context """
        newRule = context
        obj = self.context
        nextId = newRule.getNextId()
        newAction = SendNotificationAction(nextId, obj.to, obj.subject, obj.body, obj.orgMail, obj.match)
        newRule.addAction(newAction)