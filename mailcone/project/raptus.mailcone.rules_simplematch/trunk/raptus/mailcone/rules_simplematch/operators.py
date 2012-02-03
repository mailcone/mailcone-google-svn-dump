import grok

from zope import component

from zope.schema import vocabulary

from raptus.mailcone.rules_simplematch import _
from raptus.mailcone.rules_simplematch import interfaces





register = vocabulary.getVocabularyRegistry().register
def vocabulary_operators(context):
    terms = list()
    for name, operator in component.getUtilitiesFor(interfaces.IOperator):
        terms.append(vocabulary.SimpleTerm(value=name, title=operator.title))
    return vocabulary.SimpleVocabulary(terms)
register('raptus.mailcone.rules_simplematch.operators', vocabulary_operators)



class BaseOperator(grok.GlobalUtility):
    grok.implements(interfaces.IOperator)
    grok.baseclass()
    
    title = None
    
    def list(self, source):
        if isinstance(source, (list, tuple,)):
            return source
        else:
            return [source]



class OperatorIs(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.is')
    
    title = _('Is')

    def apply(self, needle, source):
        if not self.list(source):
            return False
        for val in self.list(source):
            if needle != val:
                return False
        return True


class OperatorIsNot(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.is_not')
    
    title = _('Is not')
    
    def apply(self, needle, source):
        if not self.list(source):
            return False
        for val in self.list(source):
            if needle == val:
                return False
        return True


class OperatorContains(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.contains')
    
    title = _('Contains')

    def apply(self, needle, source):
        if not self.list(source):
            return False
        for val in self.list(source):
            if not needle in val:
                return False
        return True


class OperatorNotContains(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.not_contains')
    
    title = _('Does not contains')

    def apply(self, needle, source):
        if not self.list(source):
            return False
        for val in self.list(source):
            if needle in val:
                return False
        return True


class OperatorBeginsWith(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.begins_with')
    
    title = _('Begins with')

    def apply(self, needle, source):
        if not self.list(source):
            return False
        for val in self.list(source):
            if not val.startswith(needle):
                return False
        return True


class OperatorEndsWith(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.ends_with')
    
    title = _('Ends with')

    def apply(self, needle, source):
        if not self.list(source):
            return False
        for val in self.list(source):
            if not val.endswith(needle):
                return False
        return True











