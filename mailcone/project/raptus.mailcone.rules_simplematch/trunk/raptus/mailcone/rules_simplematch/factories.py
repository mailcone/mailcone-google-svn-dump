import json
import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules.factories import BaseFactory


from raptus.mailcone.rules_simplematch import _
from raptus.mailcone.rules_simplematch.interfaces import ISimpleMatchItem
from raptus.mailcone.rules_simplematch.contents import SimpleMatchItem



class SimpleMatchFactory(BaseFactory):
    grok.name('raptus.mailcone.rules.simplematch')
    grok.implements(interfaces.IConditionItemFactory)
    
    
    title = _('Simple match')
    description = _('no idee was this thing do ???')
    form_fields = grok.AutoFields(ISimpleMatchItem)
    ruleitem_class = SimpleMatchItem


    def box_input(self):
        li = list()
        li.append(dict(title=self._translate(_('input')) ))
        return li
    
    def box_output(self):
        li = list()
        li.append(dict(title=self._translate(_('match')) ))
        li.append(dict(title=self._translate(_('do not match')) ))
        return li