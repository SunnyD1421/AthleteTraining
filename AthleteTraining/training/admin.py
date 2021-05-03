from django.contrib import admin
from .models import Location, Position, Athlete, Lifting, LiftingDescription, Throwing, ThrowingDescription, Coach, ThrowPlans, LiftPlans, ThrowingSchedule, LiftingSchedule

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('loc_name', 'loc_address')

@admin.register(Athlete)
class AthelteAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'coach_location')

@admin.register(LiftingDescription)
class LiftingDescriptionAdmin(admin.ModelAdmin):
    list_display = ('lift_name', 'lift_desc',)
    
@admin.register(LiftPlans)
class LiftPlansAdmin(admin.ModelAdmin):
    list_display = ('plan_name',)

@admin.register(Lifting)
class LiftingAdmin(admin.ModelAdmin):
    list_display = ('ath_user',)

@admin.register(LiftingSchedule)
class LiftingScheduleAdmin(admin.ModelAdmin):
    list_display = ('ath_user', 'plan', 'date',)
    
@admin.register(ThrowingDescription)
class ThrowingDescriptionAdmin(admin.ModelAdmin):
    list_display = ('throw_name', 'throw_desc',)

@admin.register(ThrowingSchedule)
class ThrowingScheduleAdmin(admin.ModelAdmin):
    list_display = ('ath_user', 'plan', 'date',)

@admin.register(Throwing)
class ThrowingAdmin(admin.ModelAdmin):
    list_display = ('ath_user',)

@admin.register(ThrowPlans)
class ThrowPlansAdmin(admin.ModelAdmin):
    list_display = ('plan_name',)
'''
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('pos_name',)
    '''