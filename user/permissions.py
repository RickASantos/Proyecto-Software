from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    message = 'No tienes permisos de administrador para realizar esta accion.'

    def has_permission(self, request, view):

        if request.user.typeuser.type_user == 2:
            return True

        return False

class IsEmployeeUser(permissions.BasePermission):
    message = 'No tienes permisos de administrador para realizar esta accion.'

    def has_permission(self, request, view):

        if request.user.typeuser.type_user == 2:
            return True

        return False
