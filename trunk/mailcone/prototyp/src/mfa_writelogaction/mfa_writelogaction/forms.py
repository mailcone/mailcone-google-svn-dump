import grok

from mfa_core_action.interfaces import IActionContainer
from mfa_writelogaction.interfaces import IWriteLogAction
from mfa_writelogaction.contents import WriteLogAction

class AddWriteLogActionForm(grok.AddForm):
    """ Generate add from for write log action content - based on grok.AddFrom """
    grok.context(IActionContainer)
    form_fields = grok.AutoFields(IWriteLogAction)
    template = grok.PageTemplateFile('writelogaction_form.pt')
    #XXX set right permission
    grok.require('mailfilter.view')
    label = "Add write log filter"
    
    @grok.action('Add action', name='addWriteLogAction')
    def add(self, **data):
        """ Provide action for generate form - save form data in a new write log action object """
        data['id'] = self.context.getNextId()
        obj = WriteLogAction(**data)
        self.context.addAction(obj)
        return self.redirect(self.url(obj))

class EditWriteLogActionForm(grok.EditForm):
    """ Provides generic form for edit """
    grok.context(IWriteLogAction)
    form_fields = grok.AutoFields(IWriteLogAction)
    template = grok.PageTemplateFile('writelogaction_form.pt')
    #XXX set right permission
    grok.require('mailfilter.view')
    label = "Edit write log filter"
    
    @grok.action('save', name='editWriteLogAction')
    def save(self, **data):
        """ Provide save action for generate edit form """
        # XXX if new name id should be also changed
        self.applyData(self.context, **data)
        return self.redirect(self.url(self.context))