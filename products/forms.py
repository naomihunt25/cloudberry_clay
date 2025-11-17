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

        categories = Category.objects.all()
        category_choices = []

        for cat in categories:
            label = getattr(cat, "display_name", cat.name)
            category_choices.append((cat.id, label))

        self.fields['category'].choices = category_choices

        for field_name, field in self.fields.items():
            if field_name == "image":
                field.widget.attrs["class"] = "border-black rounded-0"
            else:
                field.widget.attrs["class"] = "border-black rounded-0 form-control"
