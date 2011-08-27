import grok
from zope.component import getMultiAdapter

from raptus.mailcone.mailfilter.views import BaseMasterView

from raptus.mailcone.mfa_core_action.interfaces import IActionContainer
from raptus.mailcone.mailfilter.viewletmanagers import Main
from raptus.mailcone.mfa_sendnotificationaction.interfaces import ISendNotificationAction
from raptus.mailcone.mfa_sendnotificationaction.contents import SendNotificationAction

class AddSendNotificationActionView(BaseMasterView):
    """ Provide view container for viewlet which contains the generate add form """
    grok.context(IActionContainer)
    grok.name('addSendNotificationAction')
    grok.require('mailfilter.view')

class AddSendNotificationActionViewlet(grok.Viewlet):
    """ provide viewlet for the generate edit form AddSendNotificationActionForm """
    grok.viewletmanager(Main)
    grok.context(IActionContainer)
    grok.view(AddSendNotificationActionView)

    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name='addsendnotificationactionform')
        self.form.update_form()

    def render(self):
        return self.form.render()
    
class SendNotificationActionView(BaseMasterView):
    """ View for send notification action - redirect to parent object view """
    grok.context(ISendNotificationAction)
    grok.name('index')
    grok.require('mailfilter.view')

class SendNotificationActionViewlet(grok.Viewlet):
    """ XXX """
    grok.context(ISendNotificationAction)
    grok.template('sendnotificationaction_viewlet')
    grok.viewletmanager(Main)
    grok.view(SendNotificationActionView)

class SendNotificationActionMacro(grok.View):
    """ Provide an html snippet for send notification actions """
    grok.context(ISendNotificationAction)
    grok.name('macro')
    grok.template('sendnotificationaction_macro')
    grok.require('mailfilter.view')

class EditSendNotificationActionView(BaseMasterView):
    """ Provide view container for viewlet which contains the generate edit form """
    grok.context(ISendNotificationAction)
    grok.name('edit')
    grok.require('mailfilter.view')

class EditSendNotificationActionViewlet(grok.Viewlet):
    """ provide viewlet for the generate edit form EditSendNotificatonActionForm """
    grok.viewletmanager(Main)
    grok.context(ISendNotificationAction)
    grok.view(EditSendNotificationActionView)
    
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name='editsendnotficiationactionform')
        self.form.update_form()

    def render(self):
        return self.form.render()
    
class DeleteSendNotificationActionView(grok.View):
    grok.context(ISendNotificationAction)
    grok.name('delete')
    grok.require('mailfilter.view')
    
    parent = None
    
    def update(self):
        self.parent = self.context.__parent__
        self.parent.delAction(self.context)
    
    def render(self):
        self.redirect(self.url(self.parent))