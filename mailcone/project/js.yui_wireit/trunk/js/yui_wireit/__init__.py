from fanstatic import Library, Resource
from js.yui import yuiloader

library = Library('yui_wireit', 'resources')

wireit_css = Resource(
    library,
    'css/WireIt.css',
    depends=[]
)

wireit_editor_css = Resource(
    library,
    'css/WireItEditor.css',
    depends=[]
)

wireit_js = Resource(
    library,
    'build/wireit.js',
    minified='build/wireit.min.js',
    depends=[yuiloader, wireit_css]
)

wireit_editor_js = Resource(
    library,
    'build/wireit-editor.js',
    minified='build/wireit-editor-min.js',
    depends=[wireit_js, wireit_editor_css]
)

wireit = wireit_js
wireit_editor = wireit_editor_js