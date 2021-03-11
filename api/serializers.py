from rest_framework import serializers
from .models import Formdata

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formdata
        fields = '__all__'
            
            # 'first_name', 'last_name', 'company_name', 'file_upload', 'email', 'budget', 'contact_number', 'about_project'
        # , 'interested_in'