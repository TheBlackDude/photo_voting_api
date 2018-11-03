from rest_framework import permissions

class IsImageOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, image):
        if request.user:
            return image.owner == request.user
        return False
