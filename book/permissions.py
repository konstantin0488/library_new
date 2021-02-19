from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    # def has_permission(self, request, view, obj=None):
    #     print('has_permission')
    #     print(request.method)
    #     return request.method in permissions.SAFE_METHODS
            # return True
        #
        # if obj:
        #     return obj.user == request.id
        # return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user