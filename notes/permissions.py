from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['HEAD', 'OPTIONS']:
            return True

        # Instance must have an attribute named `author`.
        return obj.author == request.user

