import grok
from zope.component import getMultiAdapter

from raptus.mailcone.mailfilter.viewletmanagers import Main
from raptus.mailcone.mailfilter.views import BaseMasterView
from raptus.mailcone.mfa_core_filter.interfaces import IFilterContainer
from raptus.mailcone.mfa_simplematchfilter.interfaces import ISimpleMatchFilter
from raptus.mailcone.mfa_simplematchfilter.contents import SimpleMatchFilter

class AddSimpleMatchFilterView(BaseMasterView):
    """ Provide view container for viewlet which contains the generate add form """
    grok.context(IFilterContainer)
    grok.name('addSimpleMatchFilter')
    grok.require('mailfilter.view')
    
class AddSimpleMatchFilterViewlet(grok.Viewlet):
    """ provide viewlet for the generate edit form AddSimpleMatchFilterForm """
    grok.viewletmanager(Main)
    grok.context(IFilterContainer)
    grok.view(AddSimpleMatchFilterView)

    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name='addsimplematchfilterform')
        self.form.update_form()

    def render(self):
        return self.form.render()

    
class SimpleMatchFilterView(BaseMasterView):
    """ View for simple match filter - redirect to parent object view """
    grok.context(ISimpleMatchFilter)
    grok.name('index')
    grok.require('mailfilter.view')

class SimpleMatchFilterViewlet(grok.Viewlet):
    """ XXX """
    grok.context(ISimpleMatchFilter)
    grok.template('simplematchfilter_viewlet')
    grok.viewletmanager(Main)
    grok.view(SimpleMatchFilterView)

class SimpleMatchFilterMacro(grok.View):
    """ Provide an html snippet for simple match filters """
    grok.context(ISimpleMatchFilter)
    grok.name('macro')
    grok.template('simplematchfilter_macro')
    grok.require('mailfilter.view')

class EditSimpleMatchFilterView(BaseMasterView):
    """ Provide view container for viewlet which contains the generate edit form """
    grok.context(ISimpleMatchFilter)
    grok.name('edit')
    grok.require('mailfilter.view')
    
class EditSimpleMatchFilterViewlet(grok.Viewlet):
    """ provide viewlet for the generate edit form EditSimpleMatchFilterForm """
    grok.viewletmanager(Main)
    grok.context(ISimpleMatchFilter)
    grok.view(EditSimpleMatchFilterView)

    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name='editsimplematchfilterform')
        self.form.update_form()

    def render(self):
        return self.form.render()
    
class DeleteSimpleMatchFilterView(grok.View):
    grok.context(ISimpleMatchFilter)
    grok.name('delete')
    grok.require('mailfilter.view')
    
    parent = None
    
    def update(self):
        self.parent = self.context.__parent__
        self.parent.delFilter(self.context)
    
    def render(self):
        self.redirect(self.url(self.parent))