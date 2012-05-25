from zope import schema
from raptus.mailcone.rules import interfaces

from raptus.mailcone.rules_writelog import _
from raptus.mailcone.layout.formlib import ProposeTextField





class IWriteLogItem(interfaces.IActionItem):
    """ write output to log file
    """
    
    path = schema.TextLine(title=_('Path'),
                             required=True,
                             description=_('a absolute path to write the logfile on the filesystem.'))

    message = ProposeTextField(title=_('Message'),
                               required=True,
                               description=_('the message to write in logfile.'),
                               vocabulary='raptus.mailcone.rule_sendmail.propose')