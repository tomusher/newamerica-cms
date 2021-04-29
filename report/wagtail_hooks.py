from wagtail.core import hooks

from home.models import PublicationPermissions

from .models import Report


@hooks.register('construct_page_action_menu')
def remove_publish_report_if_no_permission(menu_items, request, context):
    """Remove the 'Publish' action from all reports unless the user is a
    superuser or in one of the auth groups specifically chosen for
    this permission.

    """
    if isinstance(context.get('page'), Report):
        settings = PublicationPermissions.for_request(request)
        if request.user.is_superuser:
            # superusers can always publish
            return

        if not request.user.groups.all() & settings.groups_with_report_permission.all():
            menu_items[:] = [
                item for item in menu_items if item.name != 'action-publish'
            ]
