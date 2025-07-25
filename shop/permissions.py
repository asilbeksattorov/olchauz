from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permission barcha uchun ruxsat
        if request.method in SAFE_METHODS:
            return True

        # Write permission faqat komment egasi uchun
        return obj.user == request.user
