import json
import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules.factories import BaseFactory


from raptus.mailcone.rules_sendmail import _



class SendMailFactory(BaseFactory):
    grok.name('raptus.mailcone.rules.sendmail')
    grok.implements(interfaces.IActionItemFactory)
    
    
    title = _('Send email')
    description = _('send a notification mail to a given address.')

    def box_input(self):
        li = list()
        li.append(dict(title=self._translate(_('input')) ))
        return li