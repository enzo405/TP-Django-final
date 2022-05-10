from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class player(ModelForm):
	class Meta:
		model = models.Player
		fields = ('nom', 'prix', 'role', 'age','profile','team')
		labels = {
			'nom' : _('Nom'),
			'prix' : _("Prix du joueur") ,
			'role' : _("Rôle du joueur"),
			'age' : _('Âge'),
			'profile' : _('Photo Profile'),
			'team' : _('Team du joueur')
			}


class Team_forms(ModelForm):
	class Meta:
		model = models.Team_models
		fields = ('nom', 'location', 'budget', 'logo')
		labels = {
			'nom' : _('Nom'),
			'budget' : _("Budget de la structure"),
			'location' : _('Location'),
			'logo' : _('Logo')
			}