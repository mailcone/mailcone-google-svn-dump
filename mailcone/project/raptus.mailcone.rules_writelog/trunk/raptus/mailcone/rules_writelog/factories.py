import json
import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules.factories import BaseFactory


from raptus.mailcone.rules_writelog import _



class WriteLogFactory(BaseFactory):
    grok.name('raptus.mailcone.rules.writelog')
    grok.implements(interfaces.IActionItemFactory)
    
    
    title = _('Write log')
    description = _('write defined message in a log file.')

    def box_input(self):
        li = list()
        li.append(dict(title=self._translate(_('input')) ))
        return li
    