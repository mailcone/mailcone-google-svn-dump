import json
import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules.factories import BaseFactoryCondition


from raptus.mailcone.rules_simplematch import _
from raptus.mailcone.rules_simplematch.interfaces import ISimpleMatchItem
from raptus.mailcone.rules_simplematch.contents import SimpleMatchItem



class SimpleMatchFactory(BaseFactoryCondition):
    grok.name('raptus.mailcone.rules.simplematch')
    grok.implements(interfaces.IConditionItemFactory)
    
    
    title = _('Simple match')
    description = _('match a input with a simple rule. like: is, startswith, content...')
    form_fields = grok.AutoFields(ISimpleMatchItem)
    ruleitem_class = SimpleMatchItem
