import grok

from zope import component

from zope.schema import vocabulary

from raptus.mailcone.rules_simplematch import _
from raptus.mailcone.rules_simplematch import interfaces


register = vocabulary.getVocabularyRegistry().register
def vocabulary_operators(context):
    terms = list()
    for name, operator in component.getUtilitiesFor(interfaces.IOperator):
        terms.append(vocabulary.SimpleTerm(value=operator.id, title=operator.title))
    return vocabulary.SimpleVocabulary(terms)
register('raptus.mailcone.rules_simplematch.operators', vocabulary_operators)


class BaseOperator(grok.GlobalUtility):
    grok.implements(interfaces.IOperator)
    grok.baseclass()
    
    title = None
    
    @property
    def id(self):
        return getattr(self, 'grokcore.component.directive.name')
    
    def apply(self, needle, source):
        pass



class OperatorIs(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.is')
    
    title = _('Is')

    def apply(self, needle, source):
        if filterCondition == source:
            return True
        return False


class OperatorIsNot(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.is_not')
    
    title = _('Is not')
    
    def apply(self, needle, source):
        if filterCondition != source:
            return True
        return False 


class OperatorContains(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.contains')
    
    title = _('Contains')

    def apply(self, needle, source):
        funcRes = super(SimpleFilterOperatorContains, self).apply(filterCondition, source)
        if funcRes != 0:
            return True
        return False


class OperatorNotContains(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.not_contains')
    
    title = _('Does not contains')

    def apply(self, needle, source):
        funcRes = super(SimpleFilterOperatorContains, self).apply(filterCondition, source)
        if funcRes == 0:
            return True
        return False


class OperatorBeginsWith(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.begins_with')
    
    title = _('Begins with')

    def apply(self, needle, source):
        funcRes = super(SimpleFilterOperatorContains, self).apply(filterCondition, source)
        return funcRes


class OperatorEndsWith(BaseOperator):
    grok.name('raptus.mailcone.rules_simplematch.ends_with')
    
    title = _('Ends with')

    def apply(self, needle, source):
        funcRes = super(SimpleFilterOperatorContains, self).apply(filterCondition, source)
        return funcRes











