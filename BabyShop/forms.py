from django.forms import ModelForm
from .models import Product, Author

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'author', 'page', 'wtitten')