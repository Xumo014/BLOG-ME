from django import forms
from .models import Coments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ['name', 'email', 'website', 'msg']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})


