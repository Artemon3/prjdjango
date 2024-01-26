from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'desc', 'owner', 'is_published', )

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if word in cleaned_data:
                raise forms.ValidationError('Присутствуют недопустимые одно или несколько слов!')
        return cleaned_data

    def clean_desc(self):
        cleaned_data = self.cleaned_data['desc']
        for word in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if word in cleaned_data:
                raise forms.ValidationError('Присутствуют недопустимые одно или несколько слов!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

