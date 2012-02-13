from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_cookie', 'resources')

cookie_js = Resource(
    library,
    'jquery.cookie.js',
    minified='jquery.cookie.min.js',
    depends=[jquery]
)

cookie = cookie_js
