from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_caret', 'resources')

caret_js = Resource(
    library,
    'jquery.caret.1.02.js',
    minified='jquery.caret.1.02.min.js',
    depends=[jquery]
)

caret = caret_js
