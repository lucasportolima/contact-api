from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    """
    Takes a user and a group name,
    and returns `True` if the user is in that group.
    """
    try:
        return user.groups.filter(name=group_name).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    """
        Check if user has permission
    """
    return any([_is_in_group(user, group_name)
                for group_name in required_groups])


class HasPermission(permissions.BasePermission):
    """
        Class used to check user permission on the view
    """

    def __init__(self, groups):
        super(HasPermission, self).__init__()
        self._groups = groups

    def has_permission(self, request, view):
        """
            Override method has_permission of BasePermission
        """

        has_group_permission = _has_group_permission(
            request.user, self._groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        """
            Override method has_object_permission of BasePermission
        """

        has_group_permission = _has_group_permission(
            request.user, self._groups)
        return request.user and has_group_permission
