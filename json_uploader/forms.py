from django import forms




class JSONUploaderForm(forms.Form):
    file = forms.FileField(label='')

    def __init__(self, *args, **kwargs):
        super(JSONUploaderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control input-lg'