from zope import schema
from zope import interface

from raptus.mailcone.rules import interfaces
from raptus.mailcone.layout.formlib import ProposeTextField

from raptus.mailcone.rules_sendmail import _



class ISendMailItem(interfaces.IActionItem):
    """ write output to log file
    """
    
    mail_addrs = schema.TextLine(title=_('Email addresses'),
                                 required=True,
                                 description=_('a list of email addresses to send the message.'))

    subject = ProposeTextField(title=_('Subject'),
                              required=True,
                              description=_('the subject to write in the mail header.'),
                              vocabulary='raptus.mailcone.rule_sendmail.propose')

    message = ProposeTextField(title=_('Message'),
                               required=True,
                               description=_('the message to write in the mail..'),
                               vocabulary='raptus.mailcone.rule_sendmail.propose')