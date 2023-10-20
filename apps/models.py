from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your models here.
class Users1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)


# # Create or update the group for Facility Managers
# facility_manager, created = Group.objects.get_or_create(name='FacilityManager')
# facility_manager.name = 'Facility Manager'
# facility_manager.save()

# # Create or update the group for Team Leaders
# team_leader_group, created = Group.objects.get_or_create(name='TeamLeader')
# team_leader_group.name = 'Team Leader'
# team_leader_group.save()

# # Create or update the group for Team Members
# team_member_group, created = Group.objects.get_or_create(name='TeamMember')
# team_member_group.name = 'Team Member'
# team_member_group.save()

# # Create or update the group for Trainees
# trainee_group, created = Group.objects.get_or_create(name='Trainee')
# trainee_group.name = 'Trainee'
# trainee_group.save()


teacher_group, created = Group.objects.get_or_create(name='Teacher')
teacher_group.name = 'Teacher'
teacher_group.save()

student_group, created = Group.objects.get_or_create(name='Student')
student_group.name = 'Student'
student_group.save()
