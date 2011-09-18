import os
import json
import grok

from grokcore.view.interfaces import ITemplateFileFactory

from zope import component

from raptus.mailcone.rules import _
from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules import resource

from raptus.mailcone.layout.views import Page, DeleteForm, AddForm

grok.templatedir('templates')



class WireItBoard(Page):
    grok.context(interfaces.IRuleset)
    
    def update(self):
        super(WireItBoard, self).update()
        resource.wireit.need()


    @property
    def toolbox(self):
        li = list()
        li.append(dict( title = _('Inputs'),
                        items = self._rules(interfaces.IInputItemFactory),)) 
        li.append(dict( title = _('Conditions'),
                        items = self._rules(interfaces.IConditionItemFactory),))
        li.append(dict( title = _('Actions'),
                        items = self._rules(interfaces.IActionItemFactory),))
        return li
    
    def _rules(self, interface):
        gen = component.getAdapters((self.context,),interface,)
        return sorted(gen, key=lambda item:item[1].order)

    @property
    def toolboxconfig(self):
        return json.dumps(dict(collapsible=True,
                               autoHeight=True,
                               active=-1))


class IdentifierMixing(object):
    def identifer(self, identifer=None):
        """ find for each ruleitem the factory class
        """
        if identifer is None:
            identifer = json.loads(self.request.form.get('identifer'))
        name = identifer.get('name')
        implements = identifer.get('implements')
        interface = None
        for i in implements:
            mod = i.get('module')
            inter = i.get('interface')
            mod = __import__(mod, None, None, mod)
            inter = getattr(mod, inter)
            if issubclass(inter, interfaces.IRuleItemFactory):
                interface = inter
                break
        return component.queryAdapter(self.context, interface, name=name)


class BaseDeleteForm(DeleteForm, IdentifierMixing):
    grok.name('wireit_delete')
    grok.context(interfaces.IRuleset)
    
    def __call__(self):
        self.factory = self.identifer()
        return super(BaseDeleteForm, self).__call__()
    
    def item_title(self):
        return self.factory.box_title()
    
    @grok.action(_(u'Delete'), name='wireit_delete')
    def handle_delete(self, **data):
        """ we use only the button, the rest we do it with javascript
        """
    
    @grok.action(_(u'Cancel'), name='cancel', validator=lambda *args, **kwargs: {})
    def handle_cancel(self, **data):
        """ we use only the button, the rest we do it with javascript
        """


class BaseEditForm(AddForm, IdentifierMixing):
    grok.name('wireit_edit')
    grok.context(interfaces.IRuleset)
    
    
    def __call__(self):
        self.form_template = self.template
        filepath = os.path.join(os.path.dirname(__file__),'templates','edit_form_wireit.cpt')
        self.template = component.getUtility(ITemplateFileFactory, name='cpt')(filename=filepath)
        self.factory = self.identifer()
        return super(BaseEditForm, self).__call__()
    
    @property
    def form_fields(self):
        return self.factory.form_fields
    
    def formhtml(self):
        return self.form_template.render(self)
    
    def overridehtml(self):
        filepath = os.path.join(os.path.dirname(__file__),'templates','override_form_wireit.cpt')
        return component.getUtility(ITemplateFileFactory, name='cpt')(filename=filepath).render(self)

    @property
    def overrides(self):
        return self.factory.override_properties()

    def verifyhtml(self):
        filepath = os.path.join(os.path.dirname(__file__),'templates','verify_form_wireit.cpt')
        return component.getUtility(ITemplateFileFactory, name='cpt')(filename=filepath).render(self)
    
    def infohtml(self):
        return '<p>%s</p>' % self.factory.description
    
    @property
    def tabs(self, ignors=[]):
        li = list()
        li.append(dict(id='ui-tabs-form',
                       title=_('Properties'),
                       html=self.formhtml()))
        li.append(dict(id='ui-tabs-overrides',
                       title=_('Override'),
                       html=self.overridehtml()))
        li.append(dict(id='ui-tabs-verify',
                       title=_('Test'),
                       html=self.verifyhtml()))
        li.append(dict(id='ui-tabs-info',
                       title=_('Info'),
                       html=self.infohtml()))
        return [i for i in li if not  i.get('id') in ignors]
    
    def item_title(self):
        return self.factory.box_title()
    
    @grok.action(_(u'Save'), name='wireit_save')
    def handle_edit(self, **data):
        """ we use only the button, the rest we do it with javascript
        """
    
    @grok.action(_(u'Cancel'), name='cancel', validator=lambda *args, **kwargs: {})
    def handle_cancel(self, **data):
        """ we use only the button, the rest we do it with javascript
        """

    
        