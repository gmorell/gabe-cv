import mistune
from django import template
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

register = template.Library()

# shamelessly grabbed from https://www.ignoredbydinosaurs.com/posts/275-easy-markdown-and-syntax-highlighting-django

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter(linenos='table')
        return highlight(code, lexer, formatter)

@register.filter
def hl8markdown(value):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(value)