from django import forms
from .models import BlogPost


class StyledModelForm(forms.ModelForm):
    
    field_styles = {}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_field_styles()
    
    def apply_field_styles(self):
        for field_name, attrs in self.field_styles.items():
            if field_name in self.fields and attrs:
                self.fields[field_name].widget.attrs.update(attrs)


class BlogPostForm(StyledModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
    
    field_styles = {
        'title': {
            'class': 'form-control',
            'placeholder': '请输入文章标题',
            'style': 'font-size: 18px; padding: 10px; margin-bottom: 15px;'
        },
        'text': {
            'class': 'form-control',
            'placeholder': '请输入文章内容...',
            'rows': 15,
            'style': 'font-size: 18px; padding: 10px; margin-bottom: 15px;'
        }
    }
    
