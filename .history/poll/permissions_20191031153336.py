from rest_framework.permissions import DjangoModelPermissions

class RjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': [],
        'PATCH': [],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }