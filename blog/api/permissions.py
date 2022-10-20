from rest_framework import permissions

class IsPostOwnerOrReadOnly(permissions.BasePermission):
    #! If the request.user is the same as the author, it can update/delete. Otherwise can view 👇
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    #! "Admin" can do any action. If not it can only view 👇
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin