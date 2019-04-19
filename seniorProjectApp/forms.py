from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Progress


class ProgressForm(ModelForm):
    class Meta:
        model = Progress
        fields = ['userID','progressID',  'linkID', 'isCompleted', 'notes']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'degreeID')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'degreeID')

