from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager) : 

    def create_user(self,email,password,**kwargs) : 
        
        user = self.model(email=self.normalize_email(email),**kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**kwargs) : 
        kwargs.setdefault("is_active",True)
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)
        return self.create_user(email=email,password=password,**kwargs)

