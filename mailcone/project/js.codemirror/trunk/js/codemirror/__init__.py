from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_syntax', 'resources')



codemirror_css = Resource(library,
                    'lib/codemirror.css',)

codemirror_js = Resource(library,
                         'lib/codemirror.js',
                         depends=[codemirror_css]
                         )

codemirror = codemirror_js


clike = Resource(library, 'mode/clike/clike.js', depends=[codemirror_js])
clojure = Resource(library, 'mode/clojure/clojure.js', depends=[codemirror_js])
coffeescript = Resource(library, 'mode/coffeescript/coffeescript.js', depends=[codemirror_js])
css = Resource(library, 'mode/css/css.js', depends=[codemirror_js])
diff_css = Resource(library, 'mode/diff/diff.css', depends=[codemirror_js])
diff = Resource(library, 'mode/diff/diff.js', depends=[codemirror_js, diff_css])
gfm = Resource(library, 'mode/gfm/gfm.js', depends=[codemirror_js])
groovy = Resource(library, 'mode/groovy/groovy.js', depends=[codemirror_js])
haskell = Resource(library, 'mode/haskell/haskell.js', depends=[codemirror_js])
htmlembedded = Resource(library, 'mode/htmlembedded/htmlembedded.js', depends=[codemirror_js])
htmlmixed = Resource(library, 'mode/htmlmixed/htmlmixed.js', depends=[codemirror_js])
javascript = Resource(library, 'mode/javascript/javascript.js', depends=[codemirror_js])
jinja2 = Resource(library, 'mode/jinja2/jinja2.js', depends=[codemirror_js])
lua = Resource(library, 'mode/lua/lua.js', depends=[codemirror_js])
markdown = Resource(library, 'mode/markdown/markdown.js', depends=[codemirror_js])
ntriples = Resource(library, 'mode/ntriples/ntriples.js', depends=[codemirror_js])
pascal = Resource(library, 'mode/pascal/pascal.js', depends=[codemirror_js])
perl = Resource(library, 'mode/perl/perl.js', depends=[codemirror_js])
php = Resource(library, 'mode/php/php.js', depends=[codemirror_js])
plsql = Resource(library, 'mode/plsql/plsql.js', depends=[codemirror_js])
python = Resource(library, 'mode/python/python.js', depends=[codemirror_js])
r = Resource(library, 'mode/r/r.js', depends=[codemirror_js])
rpm_changes = Resource(library, 'mode/rpm/changes/changes.js', depends=[codemirror_js])
rpm_spec_css = Resource(library, 'mode/rpm/spec/spec.css', depends=[codemirror_js])
rpm_spec = Resource(library, 'mode/rpm/spec/spec.js', depends=[codemirror_js, rpm_spec_css])
rst = Resource(library, 'mode/rst/rst.js', depends=[codemirror_js])
ruby = Resource(library, 'mode/ruby/ruby.js', depends=[codemirror_js])
rust = Resource(library, 'mode/rust/rust.js', depends=[codemirror_js])
scheme = Resource(library, 'mode/scheme/scheme.js', depends=[codemirror_js])
smalltalk = Resource(library, 'mode/smalltalk/smalltalk.js', depends=[codemirror_js])
sparql = Resource(library, 'mode/sparql/sparql.js', depends=[codemirror_js])
stex = Resource(library, 'mode/stex/stex.js', depends=[codemirror_js])
tiddlywiki_css = Resource(library, 'mode/tiddlywiki/tiddlywiki.css', depends=[codemirror_js])
tiddlywiki = Resource(library, 'mode/tiddlywiki/tiddlywiki.js', depends=[codemirror_js, tiddlywiki_css])
velocity = Resource(library, 'mode/velocity/velocity.js', depends=[codemirror_js])
xml = Resource(library, 'mode/xml/xml.js', depends=[codemirror_js])
xmlpure = Resource(library, 'mode/xmlpure/xmlpure.js', depends=[codemirror_js])
yaml = Resource(library, 'mode/yaml/yaml.js', depends=[codemirror_js])


theme_cobalt = Resource(library, 'theme/cobalt.css', depends=[codemirror_js])
theme_eclipse = Resource(library, 'theme/eclipse.css', depends=[codemirror_js])
theme_elegant = Resource(library, 'theme/elegant.css', depends=[codemirror_js])
theme_monokai = Resource(library, 'theme/monokai.css', depends=[codemirror_js])
theme_neat = Resource(library, 'theme/neat.css', depends=[codemirror_js])
theme_night = Resource(library, 'theme/night.css', depends=[codemirror_js])
theme_rubyblue = Resource(library, 'theme/rubyblue.css', depends=[codemirror_js])


util_rubyblue_css = Resource(library, 'lib/util/dialog.css', depends=[codemirror_js])
util_rubyblue = Resource(library, 'lib/util/dialog.js', depends=[codemirror_js, util_rubyblue_css])
util_foldcode = Resource(library, 'lib/util/foldcode.js', depends=[codemirror_js])
util_formatting = Resource(library, 'lib/util/formatting.js', depends=[codemirror_js])
util_javascript_hint = Resource(library, 'lib/util/javascript-hint.js', depends=[codemirror_js])
util_overlay = Resource(library, 'lib/util/overlay.js', depends=[codemirror_js])
util_runmode = Resource(library, 'lib/util/runmode.js', depends=[codemirror_js])
util_search = Resource(library, 'lib/util/search.js', depends=[codemirror_js])
util_searchcursor = Resource(library, 'lib/util/searchcursor.js', depends=[codemirror_js])
util_simple_hint_css = Resource(library, 'lib/util/simple-hint.css', depends=[codemirror_js])
util_simple_hint = Resource(library, 'lib/util/simple-hint.js', depends=[codemirror_js, util_simple_hint_css])





