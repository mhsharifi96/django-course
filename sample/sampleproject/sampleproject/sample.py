from django.db import models


class ActiveStudentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def males(self):
        return self.get_queryset().filter(gender='male')

    def females(self):
        return self.get_queryset().filter(gender='female')


class ActiveTeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def males(self):
        return self.get_queryset().filter(gender='male')

    def females(self):
        return self.get_queryset().filter(gender='female')


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updsated_at = models.DateTimeField(auto_now=rue)
    


class person(BaseModel):
    name = models.CharField(max_length=30)
    roll_number = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active_objects = ActiveStudentsManager()
    teacher_objets = ActiveTeacherManager()
    # student_objets = ActiveStudentManager()





    person.active_objects.male().female()





