from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name', )


class PageForm(forms.ModelForm):
    title = forms.CharField(help_text="Please enter a page title.")
    url = forms.URLField(help_text="Please enter the URL for the page.")
    views = forms.CharField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Page
        exclude = ('category', )
