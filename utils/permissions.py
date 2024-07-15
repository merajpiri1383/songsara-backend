from rest_framework.permissions import BasePermission 

class IsOwnOrNot(BasePermission) : 
    def has_object_permission(self,request,view,object) :
        if request.user.is_authenticated : 
            return object.id == request.user.id 