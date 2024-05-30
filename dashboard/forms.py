from django import forms
from clientapp.models import CourseModel

class CoursesForm(forms.ModelForm):

    # topics = forms.ModelMultipleChoiceField(queryset=Topic.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CourseModel
        fields = ["title", "level", "duration", "description", "topics", "price"]
