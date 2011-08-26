import grok

from raptus.mailcone.mfa_core_action.interfaces import IAction

class Action(object):
    """XXX"""
    grok.implements(IAction)