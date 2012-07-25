from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_splitter', 'resources')


splitter = Resource(
    library,
    'splitter.js',
    minified='splitter.min.js',
    depends=[jquery]
)


fixed_splitter = Resource(
    library,
    'fixed_splitter.js',
    minified='fixed_splitter.min.js',
    depends=[jquery]
)
