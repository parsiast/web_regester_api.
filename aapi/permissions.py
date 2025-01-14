from rest_framework import permissions

class IsAuthorOrReeadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif obj.author == request.user :
            return True
        else :
            return False