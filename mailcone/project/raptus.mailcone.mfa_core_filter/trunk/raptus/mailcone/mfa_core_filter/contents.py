import grok

from raptus.mailcone.mfa_core_filter.interfaces import IFilter

class Filter(object):
    """XXX"""
    grok.implements(IFilter)