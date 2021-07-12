from django.forms import ModelForm, fields
from .models import TODO


class TODOform(ModelForm):
    class Meta:
        model = TODO
        fields = [
            'title' , 'status','priority' ,
        ]




