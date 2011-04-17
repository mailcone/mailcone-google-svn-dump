import grok

from datetime import datetime

from mailfilter.app import MailfilterApp
from mailfilter.interfaces import (
    IRuleSet, 
    IRuleContainer, 
    IRule, 
    IMailfilterApp,
    IDatabaseSettings,
)
from mailfilter.contents import RuleSet, Rule

#
# App configuration
#
class EditAppSettings(grok.EditForm):
    """ XXX """
    grok.context(MailfilterApp)
    form_fields = grok.AutoFields(IMailfilterApp)
    grok.require('mailfilter.manageUsers')
    label = "Edit app configurations"
    
    @grok.action('save', name='saveAppSettings')
    def save(self, **data):
        """ XXX"""
        self.applyData(self.context, **data)

class EditDbSettings(grok.EditForm):
    """ XXX """
    grok.context(MailfilterApp)
    form_fields = grok.AutoFields(IDatabaseSettings)
    grok.require('mailfilter.manageUsers')
    label = "Edit database configurations"
    
    @grok.action('save', name='saveDatabaseSettings')
    def save(self, **data):
        """ XXX"""
        self.applyData(self.context, **data)

#
# RuleSet specific forms
#
class AddRuleSetForm(grok.AddForm):
    """ Generate add from for rule set content - based on grok.AddFrom """ 
    grok.context(MailfilterApp)
    form_fields = grok.AutoFields(IRuleSet).omit('id')
    #XXX set right permission
    grok.require('mailfilter.view')
    label = "Add a rule set"
    
    @grok.action('Add rule set')
    def add(self, **data):
        """ Provide add action for generate form - save form data in a new rule set object """
        obj = RuleSet(**data)
        self.context[obj.id] = obj

class EditRuleSetForm(grok.EditForm):
    """ Provides generic form for edit """
    grok.context(IRuleSet)
    form_fields = grok.AutoFields(IRuleSet).omit ('id')
    #XXX set right permission
    grok.require('mailfilter.view')
    label = "Edit rule set"
    
    @grok.action('save')
    def save(self, **data):
        """ Provide save action for generate edit form """
        self.applyData(self.context, **data)
        # XXX if new name id should be also changed

#
# Rule specific forms
#
class AddRuleForm(grok.AddForm):
    """ Generate add from for rule content - based on grok.AddFrom """
    grok.context(IRuleContainer)
    form_fields = grok.AutoFields(IRule).omit ('id', 'last_modification', 'last_modi_user', 'last_match')
    #XXX set right permission
    grok.require('mailfilter.view')
    label = "Add a rule"

    @grok.action('add', name='addRule')
    def add(self, **data):
        """ Provide add action for generate form - save form data in a new rule object """
        #XXX - must be done better - util which provide this, maybe allready exist
        data ['last_modi_user'] = self.request.principal
        newRule = Rule(**data)
        self.context.addRule(newRule)
        return self.redirect(self.url(newRule))

class EditRuleForm(grok.EditForm):
    """ Provides generic form for edit """
    grok.context(IRule)
    form_fields = grok.AutoFields(IRule).omit ('id', 'last_modification', 'last_modi_user', 'last_match')
    #XXX set right permission
    grok.require('mailfilter.view')
    label = "Edit rule"
    
    @grok.action('save', name='editRule')
    def save(self, **data):
        """ Provide save action for generate edit form """
        # XXX if new name id should be also changed
        self.applyData(self.context, **data)
        # XXX - should be done later in a Event IObjectCreatedEvent and IContainerModifiedEvent
        self.context.setLastModificationDate(datetime.now())
        #XXX - must be done better - util which provide this, maybe allready exist
        self.context.setLastModificationUser(self.request.principal)
        return self.redirect(self.url(self.context))