from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'category',
            'sku',
            'rating',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        all_categories = Category.objects.all()
        self.fields['category'].choices = [
            (cat.id, cat.get_friendly_name()) for cat in all_categories
        ]

        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{existing_classes} form-input".strip()