from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def absolutify(context, path):
    """prefexes the given path with the base url"""
    request = context["request"]
    return request.build_absolute_uri(path)
