from django.conf import settings
import importlib

DEFAULT_ACTIONS = (
    'django_ot.actions.dummy_action',
)

OT_IMPORT_ACTIONS = getattr(settings, 'OT_IMPORT_ACTIONS', DEFAULT_ACTIONS)
CONNECTION_ERROR = "There was problem with your connection to opentopic."

def get_action_choices():
    choices = []
    for action in OT_IMPORT_ACTIONS:
        m, f = action.rsplit('.', 1)
        action_func = getattr(importlib.import_module(m), f)
        choices.append((action, action_func.__doc__ or action_func.__name__))
    return choices


OT_ACTION_CHOICES = get_action_choices()