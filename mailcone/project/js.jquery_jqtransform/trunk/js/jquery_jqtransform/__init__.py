from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_jqtransform', 'resources')


jqtransform_css = Resource(
    library,
    'jqtransform.css',
    depends=[]
)

jqtransform_js = Resource(
    library,
    'jquery.jqtransform.js',
    minified='jquery.jqtransform.min.js',
    depends=[jquery, jqtransform_css]
)

jqtransform = jqtransform_js
