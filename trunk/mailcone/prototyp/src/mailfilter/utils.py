# grok stuff
import grok

import smtplib

from zope.component import getUtilitiesFor
from fanstatic import Library, Resource
from js.jquery import jquery

from mailfilter.interfaces import (
    IRuleType,
    IRuleTypeManager,
    ISeverity,
    ISeverityManager,
    IPeriodUnit,
    IPeriodUnitManager,
    IRuleJSExtenerManager,
    IControlPanelJSExtention,
    IControlPanel,
    IConfiglet,
    ISmtpServerUtil
)

class ControlPanel(grok.GlobalUtility):
    """ Provide a utility for configlet management """
    grok.implements(IControlPanel)
    
    def _getConfiglets(self):
        """ return a list of configlets """
        return getUtilitiesFor(IConfiglet)
    
    def listConfiglets(self):
        """ return a list of dicts with the keys (title and url) for registered configlets """
        return [{'id' :configlet[1].id, 
                 'title' : configlet[1].title, 
                 'url' :configlet[1].url} for configlet in self._getConfiglets()]

class RuleJSExtenerManager(grok.GlobalUtility):
    """ XXX """
    grok.implements(IRuleJSExtenerManager)
    
    def _getJSExtensions(self):
        """XXX"""
        return getUtilitiesFor(IControlPanelJSExtention)
    
    def listJSExtensions(self):
        """ XXX """
        jsExtensions = []
        [jsExtensions.extend(extension[1].listExtensions()) for extension in self._getJSExtensions()]
        return jsExtensions

class RuleSetConfigletJSExtender(grok.GlobalUtility):    
    """ XXX """
    grok.implements(IControlPanelJSExtention)
    grok.name('RuleSetConfigletJSExtender')
    jsExtensions = []
    
    def __init__(self):
        library = Library('mailfilter', 'static')
        extension = Resource(library, 'ruleset_jsextender.js', depends=[jquery])
        self.jsExtensions.append(extension)

    def listExtensions(self):
        return self.jsExtensions

class AppConfigletJSExtender(grok.GlobalUtility):    
    """ XXX """
    grok.implements(IControlPanelJSExtention)
    grok.name('AppConfigletJSExtender')
    jsExtensions = []
    
    def __init__(self):
        library = Library('mailfilter', 'static')
        extension = Resource(library, 'appconfiglet_jsextender.js', depends=[jquery])
        self.jsExtensions.append(extension)

    def listExtensions(self):
        return self.jsExtensions

class UserConfigletJSExtender(grok.GlobalUtility):    
    """ XXX """
    grok.implements(IControlPanelJSExtention)
    grok.name('UserConfigletJSExtender')
    jsExtensions = []
    
    def __init__(self):
        library = Library('mailfilter', 'static')
        extension = Resource(library, 'user_jsextender.js', depends=[jquery])
        self.jsExtensions.append(extension)

    def listExtensions(self):
        return self.jsExtensions

#XXX - make base object
class PeriodUnitManager(grok.GlobalUtility):
    """ XXX """
    grok.implements(IPeriodUnitManager)
    
    def getUtilKeys(self):
        """ return keys of registered IPeriodUnit utilities """
        sources = getUtilitiesFor(IPeriodUnit)
        return [source[0] for source in sources]

    def getUtil(self,id):
        """ return util provides IPeriodUnit with id given as parameter """
        return getUtility(IPeriodUnit, id)

#XXX - make base object
class SeverityManager(grok.GlobalUtility):
    """ XXX """
    grok.implements(ISeverityManager)
    
    def getUtilKeys(self):
        """ return keys of registered ISeverity utilities """
        sources = getUtilitiesFor(ISeverity)
        return [source[0] for source in sources]

    def getUtil(self,id):
        """ return util provides ISeverity with id given as parameter """
        return getUtility(ISeverity, id)

#XXX - make base object
class RuleTypeManager(grok.GlobalUtility):
    """ XXX """
    grok.implements(IRuleTypeManager)
    
    def getUtilKeys(self):
        """ return keys of registered IRuleType utilities """
        sources = getUtilitiesFor(IRuleType)
        return [source[0] for source in sources]

    def getUtil(self,id):
        """ return util provides IRuleType with id given as parameter """
        return getUtility(IRuleType, id)

# XXX - must be done in a local utility if smtp should be configurable
class SmtpServerUtil(grok.GlobalUtility):
    """ XXX """
    grok.implements(ISmtpServerUtil)
    
    host = None
    user = None
    passwd = None
    authrequeried = None
    
    def _addHeader(self):
        """ not provided yet - maybe in future versions """

    def send(self, mail):
        """ send given mail obj over configured smtp host """
        smtpObj = smtplib.SMTP(self.host)
        if self.authrequeried:
            smtpObj.login(self.user, self.passwd)
        smtpObj.sendmail(mail['From'], mail['To'], mail.as_string())
        
    def _addFooter(self):
        """ not provided yet - maybe in future versions """

#XXX move to filter 
from zope.component import getUtility
from hurry.query.interfaces import IQuery
from hurry.query import Eq
from mailfilter.interfaces import IFilterMailsUtility
from mailfilter.contents import Mail
from megrok import rdb

class FilterMailsUtility(grok.GlobalUtility):
    """ XXX - only for testing, must be moved maybe... - and if not renamed """
    grok.implements(IFilterMailsUtility)
    
    mails = []
    
    def _getMails(self):
        """ XXX """
        session = rdb.Session()
        #XXX take only not matched mails
        self.mails = session.query(Mail).all()
    
    def _getCustomers(self):
        """ XXX """
        query = getUtility(IQuery)
        return query.searchResults(Eq(('catalog', 'content_type'), 'Customer'))
    
    def _walkRules(self, customer):
        """ XXX """
        for rule in customer.getRules():
            rule.apply(self.mails)
            
    def filterMails(self):
        """ XXX """
        self._getMails()    
        for customer in self._getCustomers():
            self._walkRules(customer)