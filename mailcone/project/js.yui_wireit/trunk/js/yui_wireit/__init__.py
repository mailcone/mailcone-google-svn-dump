from fanstatic import Library, Resource
from js.yui import yuiloader, utilities

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
    minified='build/wireit-min.js',
    depends=[yuiloader, utilities, wireit_css]
)

wiring_editor_js = Resource(
    library,
    'build/wiring-editor.js',
    minified='build/wiring-editor-min.js',
    depends=[wireit_js, wireit_editor_css]
)

wireit = wireit_js
wireing_editor = wiring_editor_js