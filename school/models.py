from django.db import models


# Define the abstract base class for Person
class PersonBase(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)

    class Meta:
        abstract = True
        ordering = ['last_name', 'first_name', 'id']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# Define the abstract base class for Worker, inheriting from PersonBase
class WorkerBase(PersonBase):
    experience = models.IntegerField(default=0)

    class Meta:
        abstract = True


# Define the Student model, inheriting from PersonBase
class Student(PersonBase):
    faculty = models.CharField(max_length=255, blank=False)


# Define the Teacher model, inheriting from WorkerBase
class Teacher(WorkerBase):
    title = models.CharField(max_length=255, blank=True)

    @property
    def full_name(self):
        if self.title:
            return f"{self.title} {super().full_name}"
        else:
            return super().full_name
