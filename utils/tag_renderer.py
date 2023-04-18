from .constants import TAGS


def tag_renderer(request):
    """
    Makes tuple of tags available in all templates
    """
    return {
       'tags': dict(TAGS),
    }