from django.conf import settings
from cms import api
from djangocms_text_ckeditor.cms_plugins import TextPlugin


def create_cms_page(ot_config, news, content_object):
    """Create cms page"""

    ot_config = ot_config.cmsotconfig

    if content_object:
        #TODO: handle page update
        page = content_object
    else:
        page = api.create_page(
            title=news.title,
            template=ot_config.template,
            language=ot_config.language,
            parent=ot_config.parent_page
        )

        placeholder = page.placeholders.get(slot=ot_config.placeholder)

        api.add_plugin(
            placeholder=placeholder,
            language=ot_config.language,
            plugin_type=TextPlugin,
            body=news.description
        )

    return page