from django import forms

from gid.models import Ot, Tyr

class OtForm(forms.ModelForm):

    class Meta:
        model = Ot
        fields = ('author', 'text',)


class TyrForm(forms.ModelForm):

    class Meta:
        model = Tyr
        fields = ('title', 'text',)