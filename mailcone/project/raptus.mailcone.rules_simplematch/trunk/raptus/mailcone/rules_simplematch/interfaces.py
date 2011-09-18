from zope import schema
from zope import interface
from zope import component

from raptus.mailcone.rules_simplematch import _
from raptus.mailcone.rules import interfaces



class IOperator(interface.Interface):
    """ define operators utilities for a simple match rule
    """
    
    id = interface.Attribute('id of the utility must be unique')
    title = interface.Attribute('display name. should be a zope.i18n')
    
    def apply(self, needle, source):
        """ search needle in source
        """


class ISimpleMatchItem(interfaces.IConditionItem):
    """ Interface for simple match filter
    """
#    source = schema.Choice(title=u'source',
#                           source = MailSources(),
#                           required=True)
    
    operator = schema.Choice(title=_('Operator'),
                             vocabulary='raptus.mailcone.rules_simplematch.operators',
                             required=True)
    
    needle = schema.TextLine(title=_('Search string'),
                             required=True,
                             description=_('a search string to find with the choosen operator'))


