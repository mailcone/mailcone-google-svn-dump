import grok
from datetime import datetime

from zope.schema import vocabulary
from zope.i18n import translate
from zope.schema.interfaces import IList

from raptus.mailcone.core import utils

from raptus.mailcone.mails import _
from raptus.mailcone.mails import interfaces




register = vocabulary.getVocabularyRegistry().register
def vocabulary_propose(context):
    index = 0
    terms = list()
    for field in grok.AutoFields(interfaces.IMail):
        if IList.providedBy(field.field):
            continue
        name = '(Mail) %s' % field.field.title
        index += 1
        value = 'placeholder_field_%s' % index
        terms.append(vocabulary.SimpleTerm(value=value,
                                           token=field.field.getName(),
                                           title=name))
    terms.append(vocabulary.SimpleTerm(value=datetime.now().strftime('%Y-%m-%d%T%H:%M:%S'),
                                       token='datetime_now',
                                       title=translate(_('Date Time'), context=utils.getRequest())))
    terms.append(vocabulary.SimpleTerm(value=datetime.now().strftime('%Y-%m-%d'),
                                       token='date_now',
                                       title=translate(_('Date'), context=utils.getRequest())))
    terms.append(vocabulary.SimpleTerm(value=datetime.now().strftime('%H:%M:%S'),
                                       token='time_now',
                                       title=translate(_('Time'), context=utils.getRequest())))
    return vocabulary.SimpleVocabulary(terms)
register('raptus.mailcone.rule_sendmail.propose', vocabulary_propose)
