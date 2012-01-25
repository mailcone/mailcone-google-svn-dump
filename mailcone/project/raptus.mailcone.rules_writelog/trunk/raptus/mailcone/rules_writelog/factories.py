import json
import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules.factories import BaseFactoryAction
from raptus.mailcone.rules.interfaces import IActionItemFactory

from raptus.mailcone.rules_writelog import _
from raptus.mailcone.rules_writelog import interfaces
from raptus.mailcone.rules_writelog.contents import WriteLogItem


class WriteLogFactory(BaseFactoryAction):
    grok.name('raptus.mailcone.rules.writelog')
    grok.implements(IActionItemFactory)
    
    
    title = _('Write log')
    description = _('write defined message in a log file.')
    form_fields = grok.AutoFields(interfaces.IWriteLogItem)
    ruleitem_class = WriteLogItem

