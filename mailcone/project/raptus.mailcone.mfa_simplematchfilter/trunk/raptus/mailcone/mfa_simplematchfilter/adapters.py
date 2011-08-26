import grok

from raptus.mailcone.mailfilter.interfaces import ICopy
from raptus.mailcone.mfa_simplematchfilter.interfaces import ISimpleMatchFilter 
from raptus.mailcone.mfa_simplematchfilter.contents import SimpleMatchFilter

class CopySimpleMatchFilter(grok.Adapter):
    """ Adapter provide ICopy for simple match filter objects """
    grok.implements(ICopy)
    grok.context(ISimpleMatchFilter)
    
    def copy(self, context):
        """ duplicate instance and save new instance in the given context """
        newRule = context
        obj = self.context
        nextId = newRule.getNextId()
        newFilter = SimpleMatchFilter(nextId, obj.source, obj.operator, obj.condition)
        newRule.addFilter(newFilter)