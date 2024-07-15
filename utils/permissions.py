from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnOrNot(BasePermission) : 
    def has_object_permission(self,request,view,object) :
        if request.user.is_authenticated : 
            return object.id == request.user.id 

class IsStaffOrReadOnly(BasePermission) : 
    
    def has_permission(self,request,view) : 
        if request.method in SAFE_METHODS : 
            return True 
        else : 
            return request.user.is_staff