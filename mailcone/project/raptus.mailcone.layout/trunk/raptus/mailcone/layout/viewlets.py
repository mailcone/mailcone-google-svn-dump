import grok

from zope.interface import Interface
from zope import component
from zope.interface.common.interfaces import IException
from zope.app.security.interfaces import IAuthentication

from raptus.mailcone.layout import navigation





grok.templatedir('templates')
grok.context(Interface)

class HeaderManager(grok.ViewletManager):
    grok.name('header')

class ContentBeforeManager(grok.ViewletManager):
    grok.name('content.before')

class ContentManager(grok.ViewletManager):
    grok.name('content')

class ContentAfterManager(grok.ViewletManager):
    grok.name('content.after')

class NavigationManager(grok.ViewletManager):
    grok.name('navigation')

class FooterManager(grok.ViewletManager):
    grok.name('footer')
    


class Logo(grok.Viewlet):
    grok.viewletmanager(HeaderManager)
    
    @property
    def homelink(self):
        return grok.url(self.request, grok.getSite())

class Footer(grok.Viewlet):
    grok.viewletmanager(FooterManager)


class MainNavigation(grok.Viewlet):
    grok.viewletmanager(NavigationManager)


class HeaderNavigation(grok.Viewlet):
    grok.viewletmanager(HeaderManager)
    
    @property
    def username(self):
        principal = component.queryUtility(IAuthentication).authenticate(self.request)
        if principal is None:
            return None
        return principal.title
    
    


class ExceptionLogo(grok.Viewlet):
    grok.viewletmanager(ContentBeforeManager)
    grok.context(IException)
