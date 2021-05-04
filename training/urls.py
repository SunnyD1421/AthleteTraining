from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Training-Home'),
    path('about/', views.about, name='Training-About'),
    path('signup/', views.signup, name='Training-Signup'),
    
    path('visualize/', views.visualize, name='Training-Visualize'),
    path('visualize/throwing/', views.visualizeThrow, name='Training-visualizeThrow'),
    path('visualize/lifting/', views.visualizeLift, name='Training-visualizeLift'),

    path('athlete-dashboard/<int:year>/<int:month>/<int:day>', views.scheduleAth, name='Training-Schedule'),
    path('athlete-dashboard/', views.athDash, name='Training-AthleteDashboard'),
    path('coach-dashboard/', views.coachDash, name='Training-CoachDashboard'),
    
    path('coach-dashboard/addThrowExercise/', views.editThrowdesc, name='Training-AddThrow'),
    path('coach-dashboard/addThrowSchedule/', views.editThrowschedule, name='Training-AddThrowSchedule'),
    path('coach-dashboard/addThrowPlan/', views.editThrowplan, name='Training-AddThrowPlan'),
    path('coach-dashboard/addLiftExercise/', views.editLiftdesc , name='Training-AddLift'),
    path('coach-dashboard/addLiftSchedule', views.editLiftschedule , name='Training-AddLiftSchedule'),
    path('coach-dashboard/addLiftPlan', views.editLiftplan , name='Training-AddLiftPlan'),
    ]
## Login/Logout Django urls
urlpatterns += [
        path('accounts/', include('django.contrib.auth.urls')),
    ]