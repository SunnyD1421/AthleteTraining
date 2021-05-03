from django.db import models 
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

'''
----------------Utility Models-----------------
'''
## Position on the field. Used for scheduling by player type
class Position(models.Model):
    pos_name = models.CharField(max_length=15)

    def __str__(self):
        return self.pos_name

'''
----------------Data Models-----------------
'''
## Location of a Facility
class Location(models.Model):
    loc_name = models.CharField(max_length=45)
    loc_address = models.CharField(max_length=45)

    def __str__(self):
        return self.loc_name

    class Meta:
        ordering = ('loc_name', 'loc_address')
    
## Extra User columns unique to Athletes
class Athlete(models.Model):
    ath_user = models.OneToOneField(User, on_delete=models.CASCADE)
    ath_position = models.ForeignKey(Position, on_delete=models.RESTRICT)
    ath_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return User.get_full_name(self.ath_user)
    
## Extra User columns unique to Coaches 
class Coach(models.Model):
    coach_user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return User.get_full_name(self.coach_user)
    
    class Meta:
        verbose_name_plural = "Coaches"
        
## Lifting Descriptions 
class LiftingDescription(models.Model):
    LIFT_TYPE_CHOICES = [
        ('S', 'Stretch'),
        ('T', 'Tracked')
    ]
    lift_name = models.CharField(max_length=225, unique=True)
    lift_desc = models.CharField(max_length=225)
    lift_type = models.CharField(max_length=225, choices=LIFT_TYPE_CHOICES)
    lift_sets = models.IntegerField(null=True)
    lift_reps = models.IntegerField(null=True)
    #lift_video = models.CharField(max_length=225)

    def __str__(self):
        return self.lift_name

    def setsToList(self):
        sets = self.lift_sets
        setlist = []
        i=1
        while i <= sets:
            setlist += [i]
            i+=1

        return setlist

    def repsToList(self):
        reps = self.lift_reps
        replist = []
        i=1
        while i <= reps:
            replist += [i]
            i+=1

        return replist
    
## Lift Tracking (What Exercise and How Heavy)
class Lifting(models.Model):
    ath_user = models.ForeignKey(User, on_delete=models.CASCADE)
    lift_date = models.DateField(blank=True)
    lift_data = models.JSONField()
    
    class Meta:
        verbose_name_plural = "Lifting"
        unique_together = ['ath_user', 'lift_date']
    
## Lift Plans with up to 20 workouts in each
class LiftPlans(models.Model):
    plan_name = models.CharField(max_length=50)
    lifts = models.ManyToManyField(LiftingDescription)
    
    def __str__(self):
        return self.plan_name

    class Meta:
        verbose_name_plural = "Lift Plans"

## Lifting Practice Schedule
class LiftingSchedule(models.Model):
    date = models.DateField(blank=True)
    ath_user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(LiftPlans, on_delete=models.RESTRICT)

    def __str__(self):
        return LiftPlans.__str__(self.plan)

    class Meta:
        unique_together = ['date', 'ath_user']

## Throwing Descriptions
class ThrowingDescription(models.Model):
    THROW_TYPE_CHOICES = [
        ('R', 'Recovery'),
        ('T', 'Tracked')
    ]
    throw_name = models.CharField(max_length=225, unique=True)
    throw_desc = models.CharField(max_length=225)
    throw_type = models.CharField(max_length=225, choices=THROW_TYPE_CHOICES)
    throw_sets = models.IntegerField(null=True)
    throw_reps = models.IntegerField(null=True)
    #throw_video = models.CharField(max_length=225)

    def __str__(self):
        return self.throw_name

    def setsToList(self):
        sets = self.throw_sets
        setlist = []
        i=1
        while i <= sets:
            setlist += [i]
            i+=1

        return setlist

    def repsToList(self):
        reps = self.throw_reps
        replist = []
        i=1
        while i <= reps:
            replist += [i]
            i+=1

        return replist
    
## Throwing tracking (What Exercise and How fast if applicable)
class Throwing(models.Model):
    ath_user = models.ForeignKey(User, on_delete=models.CASCADE)
    throw_date = models.DateField(blank=True)
    throw_data = models.JSONField()
    
    class Meta:
        verbose_name_plural = "Throwing"
        unique_together = ['ath_user', 'throw_date']

## Lift Plans with up to 10 workouts in each
class ThrowPlans(models.Model):
    plan_name = models.CharField(max_length=50)
    throws = models.ManyToManyField(ThrowingDescription)

    def __str__(self):
        return self.plan_name

    class Meta:
        verbose_name_plural = 'Throw Plans'

## Throwing Practice Schedule
class ThrowingSchedule(models.Model):
    date = models.DateField(blank=True)
    ath_user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(ThrowPlans, on_delete=models.RESTRICT)

    def __str__(self):
        return ThrowPlans.__str__(self.plan)

    class Meta:
        unique_together = ['date', 'ath_user']