from django import forms
from django.contrib.auth.models import User, Group
from .models import Location, Position, Throwing, ThrowingDescription, ThrowingSchedule, User, ThrowPlans, LiftingDescription, LiftingSchedule, LiftPlans, Athlete, Coach
import datetime
from django.contrib.auth.forms import UserCreationForm

class CoachForm(forms.ModelForm):
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    class Meta:
        model = Coach
        exclude = ('coach_user',)

class AthleteForm(forms.ModelForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all())
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    class Meta:
        model = Athlete
        exclude = ('ath_user',)

class ThrowingForm(forms.ModelForm):
    throw_data = forms.JSONField()

    class Meta:
        model = Throwing
        exclude = ('ath_user', 'throw_date')

class ThrowDescForm(forms.ModelForm):
    THROW_TYPE_CHOICES = [
        ('R', 'Recovery'),
        ('T', 'Tracked')
    ]
    throw_name = forms.CharField(max_length=225)
    throw_desc = forms.CharField(widget=forms.Textarea, label='Throw description')
    throw_type = forms.ChoiceField(choices=THROW_TYPE_CHOICES)
    throw_sets = forms.IntegerField()
    throw_reps = forms.IntegerField()

    class Meta:
        model = ThrowingDescription
        fields = ('throw_name', 'throw_desc', 'throw_type', 'throw_sets', 'throw_reps')

class ThrowScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    ath_user = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Athlete'), label='Athlete')
    plan = forms.ModelChoiceField(queryset=ThrowPlans.objects.all())

    class Meta:
        model = ThrowingSchedule
        fields = ('date', 'ath_user', 'plan')

class ThrowPlanForm(forms.ModelForm):
    plan_name = forms.CharField()
    throws = forms.ModelMultipleChoiceField(widget = forms.SelectMultiple(attrs={'size':'15'}),
            queryset=ThrowingDescription.objects.all(), label='Throws (Hold CTRL to select multiple)')

    class Meta:
        model = ThrowPlans
        fields = ('plan_name', 'throws')

class LiftDescForm(forms.ModelForm):
    LIFT_TYPE_CHOICES = [
        ('S', 'Stretch'),
        ('T', 'Tracked')
    ]
    lift_name = forms.CharField(max_length=225)
    lift_desc = forms.CharField(widget=forms.Textarea, label='Lift description')
    lift_type = forms.ChoiceField(choices=LIFT_TYPE_CHOICES)
    lift_sets = forms.IntegerField()
    lift_reps = forms.IntegerField()

    class Meta:
        model = LiftingDescription
        fields = ('lift_name', 'lift_desc', 'lift_type', 'lift_sets', 'lift_reps')

class LiftScheduleForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    ath_user = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Athlete'), label='Athlete')
    plan = forms.ModelChoiceField(queryset=LiftPlans.objects.all())

    class Meta:
        model = LiftingSchedule
        fields = ('date', 'ath_user', 'plan')

class LiftPlanForm(forms.ModelForm):
    plan_name = forms.CharField()
    lifts = forms.ModelMultipleChoiceField(widget = forms.SelectMultiple(attrs={'size':'15'}),
            queryset=LiftingDescription.objects.all(), label='Lifts (Hold CTRL to select multiple)')

    class Meta:
        model = LiftPlans
        fields = ('plan_name', 'lifts')

class UserCreateForm(UserCreationForm):
    usertype = forms.ChoiceField(choices=[('Athlete', 'Athlete'),('Coach', 'Coach')])
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save()
        if self.cleaned_data['usertype']=='Athlete':
            userprofile = Athlete(ath_user=user, ath_location=self.cleaned_data['location'], ath_position=self.cleaned_data['position'])
            user.groups.add(Group.objects.get(name='Athlete'))
        elif self.cleaned_data['usertype']=='Coach':
            userprofile = Coach(coach_location=self.cleaned_data['location'], coach_user=user)
            user.groups.add(Group.objects.get(name='Coach'))
        userprofile.save()
        return user, userprofile