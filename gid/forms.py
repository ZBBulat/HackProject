from django import forms

from gid.models import Post , Tyr


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class TyrForm(forms.ModelForm):

    class Meta:
        model = Tyr
        fields = ('title', 'text',)