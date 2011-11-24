import grok

from zope import component
from zope.schema.fieldproperty import FieldProperty
from raptus.mailcone.rules import contents
from raptus.mailcone.rules_simplematch import interfaces





class SimpleMatchItem(contents.BaseConditionItem):
    grok.implements(interfaces.ISimpleMatchItem)
    
    needle = FieldProperty(interfaces.ISimpleMatchItem['needle'])
    operator = FieldProperty(interfaces.ISimpleMatchItem['operator'])
    source = FieldProperty(interfaces.ISimpleMatchItem['source'])

    def check(self, mail):
        operator = component.getUtility(interfaces.IOperator, name=self.operator)
        return operator.apply(self.needle, getattr(mail, self.source))


