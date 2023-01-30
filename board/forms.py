from tkinter import Widget
from django import forms
from .models import Board, Comment
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget
from django.forms import TextInput

#일반인
class PBoardWriteForm(forms.ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': '게시글 제목'
            }
        ),
        required=True,
    )

    contents = SummernoteTextField()

    field_order = [
        'title',
        #'writer',
        #'sentence',
        'image',
        'contents',
        'file',

    ]

    class Meta:
        model = Board
        fields = [
            'title',
            'contents',
            #'sentence',
            #'writer',
            'image',
            'file'
        ]
        widgets = {
            'contents' : SummernoteWidget()
        }
    
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        contents = cleaned_data.get('contents', '')
        # writer = cleaned_data.get('writer', '')
        #sentence = cleaned_data.get('sentence', '')
        image = cleaned_data.get('image', '')
        file = cleaned_data.get('file', '')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요.')
        elif image == '':
            self.add_error('image', '썸네일 이미지를 등록하세요.')
        elif contents == '':
            self.add_error('contents', '글 내용을 입력하세요.')
        else:
            self.title = title
            self.contents = contents
            #self.writer = writer
            #self.sentence = sentence
            self.image = image
            self.file = file



#과학자
class SBoardWriteForm(forms.ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': '게시글 제목'
            }
        ),
        required=True,
    )
    # sentence = forms.CharField(
    #     label='문장',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': "form-control",
    #             'placeholder': '문장'
    #         }
    #     ),
    #     required=True,
    # )

    contents = SummernoteTextField()

    field_order = [
        'title',
        #'writer',
        #'sentence',
        'contents',
        'file',
    ]

    class Meta:
        model = Board
        fields = [
            'title',
            'contents',
            #'sentence',
            #'writer',
            'file'
        ]
        widgets = {
            'contents' : SummernoteWidget()
        }
    
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        contents = cleaned_data.get('contents', '')
        #writer = cleaned_data.get('writer', '')
        #sentence = cleaned_data.get('sentence', '')
        file = cleaned_data.get('file', '')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요.')
        elif contents == '':
            self.add_error('contents', '글 내용을 입력하세요.')
        else:
            self.title = title
            self.contents = contents
            #self.writer = writer
            #self.sentence = sentence
            self.file = file

#댓글
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('board', 'user',)
        widgets = {
            'content': TextInput(attrs={
                'class': "text-add",
                'placeholder': '내 의견 달기..',
                #'style' : ''
                }),
    }


