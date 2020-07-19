from django import template
from store.models import Car, Tag

register = template.Library()


@register.inclusion_tag('store/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Car.objects.order_by('-views')[:cnt]
    return {"cars": posts}

@register.inclusion_tag('store/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}
