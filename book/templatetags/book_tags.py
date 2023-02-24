from django import template

register = template.Library()


@register.simple_tag
def construct_url(value, field_name, urlencode=None):
    url = "?{}={}".format(field_name, value)

    if urlencode:
        querystring = urlencode.split("&")
        filtered_querystring = filter(
            lambda x: x.split("=")[0] != field_name, querystring
        )
        encoded_querystring = "&".join(filtered_querystring)
        url = "{}&{}".format(url, encoded_querystring)
    return url
