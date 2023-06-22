from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from user.models import User

CARBURANT = [
    ("Diesel", "Diesel"),
    ("Fioul", "Fioul"),
    ("Essence", "Essence"),
]


POWERMODE = [
    ("Continue", "Continue"),
    ("Alternative", "Alternative")
]

SPEED = [
    ("Constant", "Constant"),
    ("Variable", "Variable")
]

ENGINETYPE = [
    ("Combustion", "Combustion"),
    ("Explosion", "Explosino"),
    ("Electric", "Electric"),
]



class CarType(models.Model):
    type_name = models.CharField(max_length=100, default="Regular", primary_key=True)
    nb_seats = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Cartype: {self.type_name}"


class Builder(models.Model):
    name = models.CharField(max_length=100, default="Toyota", primary_key=True)
    hq = models.CharField(max_length=200, default="Monaco, Cameroun")

    def __str__(self) -> str:
        return f"Builder: {self.name}"

class EngineType(models.Model):
    type_name = models.CharField(max_length=200, default="Explosion", choices=ENGINETYPE)

    def __str__(self) -> str:
        return f"Engine type: {self.type_name}"

class Carburant(models.Model):
    name = models.CharField(max_length=200, default=CARBURANT[0], choices=CARBURANT)

    def __str__(self) -> str:
        return f"Carburant: {self.name}"

class PowerType(models.Model):
    type_name = models.CharField(max_length=200, default=POWERMODE[0], choices=POWERMODE)

    def __str__(self) -> str:
        return f"Power: {self.type_name}"

class SpeedType(models.Model):
    type_name = models.CharField(max_length=200, default=SPEED[0], choices=SPEED)

    def __str__(self) -> str:
        return f"Speed: {self.type_name}"
    
    

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    date = models.DateField(auto_now=True)
    price = models.FloatField()
    description = models.TextField(default="No description provided.")
    #car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    model = models.CharField(max_length=200, default="new model")
    color = models.CharField(max_length=100, default="No color provided")
    image = models.ImageField(null=True)
    state = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    builder = models.ForeignKey(Builder, on_delete=models.DO_NOTHING, null=True)
    car_type = models.ForeignKey(CarType, on_delete=models.DO_NOTHING, null=True)
    engine_type = models.ForeignKey(EngineType, on_delete=models.DO_NOTHING, null=True)
    carburant = models.ForeignKey(Carburant, on_delete=models.DO_NOTHING, null=True)
    power = models.ForeignKey(PowerType, on_delete=models.DO_NOTHING, null=True)
    speed = models.ForeignKey(SpeedType, on_delete=models.DO_NOTHING, null=True)
    nb_horses = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"Announcement: {self.builder.name} {self.car_model}"
