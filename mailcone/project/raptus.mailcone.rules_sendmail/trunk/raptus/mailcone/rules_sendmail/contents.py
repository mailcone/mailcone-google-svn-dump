
import grok

from zope import component

from raptus.mailcone.core import utils
from raptus.mailcone.settings.interfaces import ISMTPLocator

from raptus.mailcone.rules import contents
from raptus.mailcone.rules_sendmail import _
from raptus.mailcone.rules_sendmail import interfaces






class SendMailItem(contents.BaseActionItem):
    grok.implements(interfaces.ISendMailItem)
    
    # take only a single email address at the moment
    mail_addrs = ''
    subject = ''
    message = ''
    
    @contents.process
    def process(self, charter):
        for mail in charter.mails:
            self.send(mail)

    def test(self, mail, factory):
        try:
            self.send(mail)
            mapping = dict(factory=factory.title, title=self.title, addrs=self.mail_addrs, message=self.get_message(mail))
            msg = 'Rule <${factory}@${title}> successfully send email(s) to  ${addrs} \nmessage: ${message}'
            return self.translate(_(msg, mapping=mapping), context=utils.getRequest())
        except Exception, e:
            return str(e)
    
    def send(self, mail):
        sender = component.getUtility(ISMTPLocator)()
        sender.send(self.get_message(mail), self.get_message(mail, attr='subject'), self.mail_addrs)




