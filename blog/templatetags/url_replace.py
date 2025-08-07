from django import template

register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    """
    Return encoded querystring after replacing `field` by `value`.
    Usage: ?{% url_replace request 'page' 2 %}
    """
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
