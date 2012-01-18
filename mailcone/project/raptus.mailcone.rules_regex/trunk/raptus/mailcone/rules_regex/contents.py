import grok
import re

from zope import component
from zope.schema.fieldproperty import FieldProperty
from raptus.mailcone.rules import contents
from raptus.mailcone.rules_regex import interfaces




class RegexItem(contents.BaseConditionItem):
    grok.implements(interfaces.IRegexItem)
    
    regex = FieldProperty(interfaces.IRegexItem['regex'])
    source = FieldProperty(interfaces.IRegexItem['source'])

    def check(self, mail):
        source = getattr(mail, self.source)
        if not isinstance(source, (list,tuple,)):
            source = [source]
        for string in source:
            match = re.match(self.regex, string)
            if match is not None:
                return True
        return False


