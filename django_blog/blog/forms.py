from django import forms
from .models import Profile, Post, Comment,Tag

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class CreatePostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='Separate tags with commas')
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tag_string = self.cleaned_data['tags']
        tag_names = [name.strip() for name in tag_string.split(',') if name.strip()]
        return tag_names
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_tags(instance)
        return instance
    
    def save_tags(self, instance):
        instance.tags.clear()
        tag_names = self.cleaned_data['tags']
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
