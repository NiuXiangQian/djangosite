from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=2)
    occupation = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return str({"id": self.id, "gender": self.gender, "age": self.age, "occupation": self.occupation,
                    "zip_code": self.zip_code})

    class Meta:
        db_table = "user"
