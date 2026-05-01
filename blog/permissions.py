from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorPermission(BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method is SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        if not request.user.is_authenticated:
            return False

        return obj.author.user == request.author
