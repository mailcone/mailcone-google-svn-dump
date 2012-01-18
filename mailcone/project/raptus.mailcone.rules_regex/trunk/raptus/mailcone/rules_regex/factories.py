import json
import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules.factories import BaseFactoryCondition


from raptus.mailcone.rules_regex import _
from raptus.mailcone.rules_regex.contents import RegexItem
from raptus.mailcone.rules_regex.interfaces import IRegexItem





class RegexFactory(BaseFactoryCondition):
    grok.name('raptus.mailcone.rules.regex')
    grok.implements(interfaces.IConditionItemFactory)
    
    
    title = _('Regex')
    description = _('Match input with given regular expression.')
    form_fields = grok.AutoFields(IRegexItem)
    ruleitem_class = RegexItem




