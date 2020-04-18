'''
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
'''

from django import forms
from .models import HuckYou, Images

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    #body = forms.CharField(max_length=20000, label="Article text")

    class Meta:
        model = HuckYou
#        fields = ('article', 'title', 'text', )
        fields = ('article', )
        widgets = {
             'article': RichTextFormField(),
             'file': CKEditorUploadingWidget(),
             }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )