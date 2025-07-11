from markdown import markdown
from django.utils.safestring import mark_safe


def markdown_to_html(text: str) -> str:
    """
    Converts a Markdown formatted string to HTML.
    Uses the 'extra' and 'nl2br' extensions for additional features.
    """
    html = markdown(text, extensions=['extra', 'nl2br'])
    return mark_safe(html)
