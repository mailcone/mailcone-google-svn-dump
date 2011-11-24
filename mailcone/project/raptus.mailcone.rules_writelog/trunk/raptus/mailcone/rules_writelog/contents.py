import grok

from raptus.mailcone.rules import contents
from raptus.mailcone.rules_writelog import interfaces





class WriteLogItem(contents.BaseActionItem):
    grok.implements(interfaces.IWriteLogItem)
    
    def process(self, charter):
        for i in charter.mails:
            print i













