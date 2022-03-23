from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerOrReadOnly(BasePermission):
    """Доступ только от автора и выше."""
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return (
            obj.author == request.user
            or request.user.permission_level() >= 1
            or request.user.is_staff
            or request.user.is_superuser
        )


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
    # Не уверен в том, что это будет работать правильно

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.is_staff or request.user.role == 'admin'))
        )
