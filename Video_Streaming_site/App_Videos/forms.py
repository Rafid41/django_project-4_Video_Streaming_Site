from django import forms
from App_Videos.models import Video_post, Comment


# modify model structure
# class PostForm(forms.ModelForm):
#     category = forms.ModelChoiceField(queryset=Video_post.category.objects.all(), empty_label="Select a category")
#     class Meta:
#         model = Video_post
#         fields = ['title', 'link',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)