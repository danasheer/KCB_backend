from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated, IsAdminUser


class IsOwner(BasePermission):
    message = 'You must be the owner.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
