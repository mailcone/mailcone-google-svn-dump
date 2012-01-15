from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_syntax', 'resources', 'public')




syntax_js = Resource(
    library,
    'jquery.syntax.js',
    minified='jquery.syntax.min.js',
    depends=[jquery]
)

cache_js = Resource(library,
                    'jquery.cache.js',
                    depends=[syntax_js])


syntax = cache_js





