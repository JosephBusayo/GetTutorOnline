from django.db import models
from parents.models import ParentProfile
# Create your models here.


class Tutor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ID_CHOICES = (
        ('NIN', 'NIN'),
        ('PVC', 'Permanent Voters Card'),
        ('INTL', 'International Passport'),
        ('DRIV', 'Drivers\' License'),
    )
    profile = models.OneToOneField(ParentProfile, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=False, blank=False, default='M')
    age = models.CharField(max_length=2, null=False, default=20, blank=False)
    dob = models.DateField()
    disabilities = models.CharField(max_length=150, default='None', null=False)
    nce = models.CharField(max_length=100, default='None',
                           null=False, blank=True, verbose_name='College of Education')
    bachelors = models.CharField(
        max_length=200, default='None', null=False, blank=True, verbose_name='Bachelors')
    post_grad = models.CharField(max_length=100, default='None',
                                 null=False, blank=True, verbose_name='Post Graduate Studies')
    masters = models.CharField(
        max_length=200, default='None', null=False, blank=True, verbose_name='Masters')
    phd = models.CharField(max_length=100, default='None', null=False,
                           blank=True, verbose_name='Doctor of Philosophy(PhD)')
    government_id_type = models.CharField(
        choices=ID_CHOICES, max_length=4, null=False, blank=False)
    government_id_number = models.PositiveIntegerField()
    yrs_of_experience = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    bank_account_number = models.PositiveIntegerField()
    social_media_verification = models.BooleanField(default=False)
    government_id_verification = models.BooleanField(default=False)
    bank_verification = models.BooleanField(default=False)
    slug = models.SlugField()
    became_tutor_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.title} {self.profile.user.first_name} {self.profile.user.last_name}"


class Expertise(models.Model):
    GRADE_CHOICES = (
        ('primary', 'Primary'),
        ('juniors', 'Junior Secondary'),
        ('seniors', 'Senior Secondary'),
    )

    name = models.CharField(max_length=30)
    grade = models.CharField(choices=GRADE_CHOICES,
                             default='juniors', max_length=10)

    def __str__(self):
        return f"{self.name} for {self.grade}"


class TutoringPlan(models.Model):
    MEDIUM_CHOICES = (
        ('online', 'Online Tutoring'),
        ('physical', 'Physical Tutoring'),
        ('both', 'Online and Physical Tutoring'),
    )
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    major = models.OneToOneField(
        Expertise, on_delete=models.SET_NULL, null=True, related_name='major')
    minor1 = models.OneToOneField(
        Expertise, on_delete=models.SET_NULL, null=True, related_name='minor1')
    minor2 = models.OneToOneField(
        Expertise, on_delete=models.SET_NULL, null=True, related_name='minor2')
    medium = models.CharField(
        max_length=10, choices=MEDIUM_CHOICES, default='online')
    locations = models.CharField(
        max_length=200, null=False, blank=False, default='Any Location...')
    rate_per_hour = models.PositiveIntegerField()

    def __str__(self):
        tutor = self.tutor.profile
        return f"{tutor.title} {tutor.user.first_name} {tutor.user.last_name}'s Tutoring Plan"
