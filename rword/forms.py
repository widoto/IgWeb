from importlib.resources import contents
from django import forms
from .models import SentenceList, SentenceListComment
from django.forms import TextInput

#일반인
class RSentencesWriteForm(forms.Form):
    #sentence = forms.CharField(error_messages={'required':"문장을 입력하세요"}, label="문장")
    #contents = forms.CharField(error_messages={'required':"문장을 입력하세요"}, widget=forms.Textarea, label='설명')
    sentence = forms.CharField(
        error_messages={'required':"문장을 입력하세요"},
        label="문장",
        widget=forms.TextInput(attrs={
            'class': 'form-control onesentence',
            'placeholder': '랜덤 단어를 넣어 한 문장으로 완성하세요.'
        })
    )
    contents = forms.CharField(
        error_messages={'required':"문장을 입력하세요"},
        label='설명',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': '내용을 입력해 주세요.',
            'rows':"5"
        })

    )

#댓글
class SentencesCommentForm(forms.ModelForm):
    class Meta:
        model = SentenceListComment
        exclude = ('Sentence', 'user',)
        widgets = {
            'content': TextInput(attrs={
                'class': "text-add",
                'placeholder': '내 의견 달기..'
                }),
    }
