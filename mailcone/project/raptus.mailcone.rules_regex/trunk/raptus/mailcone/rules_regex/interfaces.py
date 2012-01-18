from zope import schema
from zope import interface
from zope import component

from raptus.mailcone.rules_regex import _
from raptus.mailcone.rules import interfaces





class IRegexItem(interfaces.IConditionItem):
    """ Interface for regex match filter
    """

    regex = schema.TextLine(title=_('Needle'),
                             required=True,
                             description=_('a search string to find with the choosen operator'))
    
    source = schema.Choice(title=_('Source'),
                           vocabulary='raptus.mailcone.mails.mailattributes',
                           required=True)