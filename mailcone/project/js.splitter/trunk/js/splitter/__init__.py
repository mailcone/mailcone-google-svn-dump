from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('splitter.js', 'resources')

splitter_js = Resource(
    library,
    'splitter.js',
    minified='splitter.min.js',
    depends=[jquery]
)

splitter = splitter_js
