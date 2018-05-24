from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    level = models.CharField(max_length = 30)
    

class GameData(models.Model):
    user = models.ForeignKey(User, related_name="games", on_delete=models.CASCADE)

class AgentData(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(GameData, related_name="agents", on_delete=models.CASCADE)

class TechData(models.Model):
    schools = models.IntegerField(default=0)
    curriculum = models.IntegerField(default=0)
    roads = models.IntegerField(default=0)
    infrastructure = models.IntegerField(default=0)
    police_stations = models.IntegerField(default=0)
    police_training = models.IntegerField(default=0)

class StatData(models.Model):
    education = models.FloatField(default=0)
    traffic = models.FloatField(default=0)
    crime = models.FloatField(default=0)
    population = models.IntegerField(default=0)
    money = models.FloatField(default=0)

class StateData(models.Model):
    name = models.CharField(max_length=255)
    tech = models.ForeignKey(TechData, related_name="state", on_delete=models.CASCADE)
    stats = models.ForeignKey(StatData, related_name="state", on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentData, related_name="states", on_delete=models.CASCADE)
    game = models.ForeignKey(GameData, related_name="states", on_delete=models.CASCADE)
    levels = models.ForeignKey(User, related_name='states',on_delete = models.CASCADE)
