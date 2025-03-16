from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """Permission : Seuls les admins peuvent modifier, les autres peuvent juste lire."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'ADMIN'

class IsModeratorOrReadOnly(permissions.BasePermission):
    """Permission : Les modérateurs et admins peuvent modifier, les autres peuvent juste lire."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'MODERATEUR']
