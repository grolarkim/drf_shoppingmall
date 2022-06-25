from rest_framework.permissions import BasePermission


class PostOrLoginRequired(BasePermission):
    SAFE_METHODS = ("POST",)

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            or request.method in self.SAFE_METHODS
        )
