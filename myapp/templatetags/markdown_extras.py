from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter(name='markdown')
# @stringfilter
def markdown_filter(value):
    print("Markdown filter called with:", value)
    return markdown.markdown(value, safe_mode='escape', extensions=['nl2br'], output_format='html5', tab_length=2, lazy_ol=False, lazy_ol_start=1)
