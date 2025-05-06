from rest_framework import permissions

class IsAuthorEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_object_permission(self, request, view, obj):
        # If the user has the model-level permission, allow it
        if request.user.has_perm(self.perms_map.get(request.method, [])[0]):
            return True

        # For PUT, PATCH, and DELETE, only allow if the user is the author
        return obj.author == request.user  # Changed to creator

 