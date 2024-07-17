from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path

image_path = Path(__file__).parent.parent / "static/test.jpg"
file_path = Path(__file__).parent.parent / "static/test.mp3"


class TestBase(APITestCase) : 

    @classmethod
    def setUpTestData(self) -> None : 

        self.image_1 = SimpleUploadedFile(
                content = open(image_path,"rb").read() , 
                content_type = "image/jpg",
                name = "image1.jpg"
            )
        self.image_2 = SimpleUploadedFile(
                content = open(image_path,"rb").read() , 
                content_type = "image/jpg",
                name = "image2.jpg"
            )
        
        self.file_1 = SimpleUploadedFile(
                content = open(file_path,"rb").read() , 
                content_type = "audio/mpeg",
                name = "file1.mp3"
            )

        self.file_2 = SimpleUploadedFile(
                content = open(file_path,"rb").read() , 
                content_type = "audio/mpeg",
                name = "file2.mp3"
            )

        self.staff_user = get_user_model().objects.create(
            email = "staff_user@gmail.com",
            username = "staff-user@gmail.com",
            is_staff = True , 
            is_active = True
        )
        
        self.normal_user = get_user_model().objects.create(
            email = "normal_user@gmail.com",
            username = "normal-user@gmail.com",
            is_active = True
        )

        return super().setUpTestData()