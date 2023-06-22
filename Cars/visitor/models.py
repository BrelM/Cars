from django.db import models

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



class CarType(models.Model):
    type_name = models.CharField(max_length=100, default="New model", primary_key=True)
    nbSeats = models.IntegerField()
    
    def __str__(self) -> str:
        return "Cartype: " + self.typeName


class Builder(models.Model):
    name = models.CharField(max_length=100, default="Toyota", primary_key=True)
    hq = models.CharField(max_length=200, default="Monaco, Cameroun")

    def __str__(self) -> str:
        return "Builder: " + self.name

class EngineType(models.Model):
    type_name = models.CharField(max_length=200, default="explosion")

    def __str__(self) -> str:
        return "Engine type: " + self.typeName

class Carburant(models.Model):
    name = models.CharField(max_length=200, default=CARBURANT[0], choices=CARBURANT)

    def __str__(self) -> str:
        return "Carburant: " + self.name

class PowerType(models.Model):
    type_name = models.CharField(max_length=200, default=POWERMODE[0], choices=POWERMODE)

    def __str__(self) -> str:
        return "Power: " + self.typeName

class SpeedType(models.Model):
    type_name = models.CharField(max_length=200, default=SPEED[0], choices=SPEED)

    def __str__(self) -> str:
        return "Speed: " + self.typeName

class Engine(models.Model):
    engine_type = models.ForeignKey(EngineType, on_delete=models.DO_NOTHING)
    carburant = models.ForeignKey(Carburant, on_delete=models.DO_NOTHING)
    power = models.ForeignKey(PowerType, on_delete=models.DO_NOTHING)
    speed = models.ForeignKey(SpeedType, on_delete=models.DO_NOTHING)
    nb_horses = models.IntegerField()

    def __str__(self) -> str:
        return "Engine"
    
    
class Car(models.Model):
    car_model = models.CharField(max_length=200, default="new model")
    color = models.CharField(max_length=100, default="No color provided")
    image = models.ImageField()
    state = models.IntegerField()
    builder = models.ForeignKey(Builder, on_delete=models.DO_NOTHING)
    car_type = models.ForeignKey(CarType, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return "Car: " + self.builder.name + " " + self.carModel

class Announcement(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self) -> str:
        return "Announcement: " + self.car.__str__()
    
    