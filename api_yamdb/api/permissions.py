from rest_framework.permissions import BasePermission, SAFE_METHODS


class ModeratorOrReadOnly(BasePermission):
    """Доступ только от модератора и выше."""
    MIN_PERMISSION_CLASS = 1

    def has_object_permission(self, request, view, obj):
        return (
            request.user.permission_level() >= self.MIN_PERMISSION_CLASS
            or request.user.is_staff
            or request.user.is_superuser
        )

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or request.user.is_authenticated()
        )


class AdminOrReadOnly(BasePermission):
    """Доступ только от админа и выше."""
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            (request.user.is_authenticated and
             (request.user.is_staff or request.user.role == 'admin')
             )
        )
