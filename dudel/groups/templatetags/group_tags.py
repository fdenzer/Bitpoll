from django import template
from dudel.groups.models import GroupInvitation

register = template.Library()


@register.assignment_tag(takes_context=True)
def open_invitations(context):
    user = context['user']
    if user.is_authenticated():
        return GroupInvitation.objects.filter(invitee=user).count()


@register.assignment_tag(takes_context=True)
def get_invitations(context):
    user = context['user']
    if user.is_authenticated():
        return GroupInvitation.objects.filter(invitee=user).all()


@register.assignment_tag(takes_context=True)
def get_user_groups(context):
    user = context['user']
    if user.is_authenticated():
        return user.groups.all().order_by('name')
