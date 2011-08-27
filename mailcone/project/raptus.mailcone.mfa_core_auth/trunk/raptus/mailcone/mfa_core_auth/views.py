import grok

from zope.interface import Interface
from zope.component import getUtility
from zope.pluggableauth.interfaces import IAuthenticatorPlugin
from zope.authentication.interfaces import IAuthentication, IUnauthenticatedPrincipal, ILogout

from raptus.mailcone.mailfilter.views import BaseMasterView

from raptus.mailcone.mailfilter.viewletmanagers import Main
from raptus.mailcone.mfa_core_auth.contents import UserFolder

class Logout(grok.View):
    """XXX"""
    grok.context(Interface)
    grok.require('zope.Public')

    def update(self):
        """XXX"""
        if not IUnauthenticatedPrincipal.providedBy(self.request.principal):
            auth = component.getUtility(IAuthentication)
            ILogout(auth).logout(self.request)

class UserListView(BaseMasterView):
    """XXX"""
    grok.context(UserFolder)
    grok.name('index')
    grok.require('mailfilter.manageUsers')
    
    def update(self):
        """XXX"""
        users = getUtility(IAuthenticatorPlugin,'users')
        self.users = users.listUsers()

class UserListViewlet(grok.Viewlet):
    """XXX"""
    grok.viewletmanager(Main)
    grok.context(UserFolder)
    grok.template('userlist_viewlet')
    grok.view(UserListView)