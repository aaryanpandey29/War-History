from django.db import models
from django.utils.text import slugify


class Articles(models.Model):

    Name = models.CharField(max_length=255)
    Year = models.CharField(max_length=30)
    Victor = models.CharField(max_length=30)
    Importance = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=50)

    # Before
    # Side 1
    side1_Name = models.CharField(max_length=255)
    side1_troops = models.CharField(max_length=255)
    side1_infantry = models.CharField(max_length=255)
    side1_cavalry = models.CharField(max_length=255)
    side1_veterans = models.CharField(max_length=255)
    side1_morale = models.CharField(max_length=255)
    side1_food = models.CharField(max_length=255)
    side1_supplyLoss = models.CharField(max_length=255)
    side1_armor = models.CharField(max_length=255)
    side1_mountedUnits = models.CharField(max_length=255)
    side1_mainRoute = models.CharField(max_length=255)
    side1_routeLength = models.CharField(max_length=255)
    side1_contested = models.CharField(max_length=255)
    side1_supplyDelay = models.CharField(max_length=255)

    # Side 2
    side2_Name = models.CharField(max_length=255)
    side2_troops = models.CharField(max_length=255)
    side2_infantry = models.CharField(max_length=255)
    side2_cavalry = models.CharField(max_length=255)
    side2_veterans = models.CharField(max_length=255)
    side2_morale = models.CharField(max_length=255)
    side2_food = models.CharField(max_length=255)
    side2_supplyLoss = models.CharField(max_length=255)
    side2_armor = models.CharField(max_length=255)
    side2_mountedUnits = models.CharField(max_length=255)
    side2_mainRoute = models.CharField(max_length=255)
    side2_routeLength = models.CharField(max_length=255)
    side2_contested = models.CharField(max_length=255)
    side2_supplyDelay = models.CharField(max_length=255)

    Terrain = models.CharField(max_length=30)
    Weather = models.CharField(max_length=30)
    Visibility = models.CharField(max_length=30)
    Mobility = models.CharField(max_length=30)

    # Side 1
    commander1_name = models.CharField(max_length=255)
    commander1_SuccessfulDecisions = models.TextField()
    commander1_FailedDecisions = models.TextField()

    # Side 2
    commander2_name = models.CharField(max_length=255)
    commander2_successfulDecisions = models.TextField()
    commander2_FailedDecisions = models.TextField()

    # During
    TurningPoint = models.TextField()
    side1_battlePressure = models.CharField(max_length=255)
    side2_battlePressure = models.CharField(max_length=255)

    # After
    side1_casualties = models.CharField(max_length=255)
    side1_captured = models.CharField(max_length=255)
    side1_equipmentLoss = models.CharField(max_length=255)
    side1_supplyLoss = models.CharField(max_length=255)

    side2_casualties = models.CharField(max_length=255)
    side2_captured = models.CharField(max_length=255)
    side2_equipmentLoss = models.CharField(max_length=255)
    side2_supplyLoss = models.CharField(max_length=255)

    TacticalReform = models.TextField()
    DoctrineChange = models.TextField()
    MoraleEffect = models.TextField()
    HistoricalImpact = models.TextField()
    MilitaryInfluence = models.TextField()
    LongTermConsequence = models.TextField()

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.Name
