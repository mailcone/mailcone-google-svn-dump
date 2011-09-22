import grok

from raptus.mailcone.rules import contents
from raptus.mailcone.rules_simplematch import interfaces

class SimpleMatchItem(contents.BaseConditionItem):
    grok.implements(interfaces.ISimpleMatchItem)
    
    needle = None
    operator = None