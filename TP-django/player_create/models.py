from django.db import models

role_choice = [
    ("Star Player","Star Player"),
    ("Awper","Awper"),
    ("Lurker","Lurker"),
    ("Entry","Entry"),
    ("Second Entry","Second Entry"),
    ("Leader IG","Leader IG"),
    ("Fix BP","Fix BP"),
    ("Pivot","Pivot"),
]

class Player(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(blank=False)
    role = models.CharField(max_length=20 ,choices=role_choice)
    age = models.IntegerField(blank=False)
    profile = models.URLField(null= True)
    team = models.ForeignKey("Team_models", on_delete=models.CASCADE , null=True)

    def __str__(self):
        chaine = f"{self.nom}: {self.role} | {self.prix}$ | {self.age} ans."
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom, "prix":self.prix, "role":self.role,"age":self.age,"profile":self.profile, "team":self.team}


class Team_models(models.Model):
    nom = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    budget = models.IntegerField(blank=False)
    logo = models.URLField(null= True)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom, "location":self.location, "budget":self.budget,"logo":self.logo}