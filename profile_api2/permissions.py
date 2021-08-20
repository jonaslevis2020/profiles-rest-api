from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user has the permissions to edit the profile"""
        if request.method in permissions.SAFE_METHODS:
            return True