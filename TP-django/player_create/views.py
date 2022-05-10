from pyexpat import model
from tkinter.tix import COLUMN
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import player, Team_forms
from . import models
import random


def formulaire_player(request):
	ALLjoueur = models.Player.objects.all()
	emptylist = []
	for l in ALLjoueur:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	if request.method == "POST":
		form = player(request)
		if form.is_valid():
			joueur = form.save()
			return render(request,"affiche_player.html",{"player" : joueur, "randomID_player": random_id})
		else:
			return render(request,"formulaire_player.html",{"form_player": form, "randomID_player": random_id})
	else :
		form = player()
		return render(request,"formulaire_player.html",{"form_player" : form, "randomID_player": random_id})

def traitement_player(request):
	lform = player(request.POST)
	if lform.is_valid():
		joueur = lform.save()
		joueur.save()
		return HttpResponseRedirect("/player/")
	else:
		return render(request,"formulaire_player.html",{"player" : joueur})

def index_player(request):
	ALLjoueur = models.Player.objects.all()
	emptylist = []
	for l in ALLjoueur:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	liste = list(models.Player.objects.all())
	return render(request,"index_player.html",{"listALL_player": liste, "randomID_player": random_id})

def affiche_player(request, id):
	ALLjoueur = models.Player.objects.all()
	emptylist = []
	for l in ALLjoueur:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	joueur = models.Player.objects.get(pk=id)
	return render(request,'affiche_player.html',{"player": joueur, "randomID_player": random_id})

def update_player(request, id):
	ALLjoueur = models.Player.objects.all()
	emptylist = []
	for l in ALLjoueur:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	joueur = models.Player.objects.get(pk=id)
	form1 = player(joueur.dictionnaire())
	return render(request,'formulaire_player.html',{"form_player": form1, "id_player":id, "randomID_player":random_id})

def updatetraitement_player(request, id):
	ALLjoueur = models.Player.objects.all()
	emptylist = []
	for l in ALLjoueur:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	form1 = player(request.POST)
	if form1.is_valid():
		joueur = form1.save(commit=False)
		joueur.id = id
		joueur.save()
		return HttpResponseRedirect("/player/")
	else:
		return render(request,"formulaire_player.html",{"form_player": form1, "id_player":id, "randomID_player": random_id})

def delete_player(request, id):
	player = models.Player.objects.get(pk=id)
	player.delete()
	return HttpResponseRedirect("/player/")



def formulaire_team(request):
	ALLekip = models.Team_models.objects.all()
	emptylist = []
	for l in ALLekip:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	if request.method == "POST":
		form = Team_forms(request)
		if form.is_valid():
			ekip = form.save()
			return render(request,"affiche_team.html",{"team" : ekip, "randomID_team": random_id})
		else:
			return render(request,"formulaire_team.html",{"form_team": form, "randomID_team": random_id})
	else :
		form = Team_forms()
		return render(request,"formulaire_team.html",{"form_team" : form})

def traitement_team(request):
	ALLekip = models.Team_models.objects.all()
	emptylist = []
	for l in ALLekip:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	lform = Team_forms(request.POST)
	if lform.is_valid():
		ekip = lform.save()
		return HttpResponseRedirect("/team/")
	else:
		return render(request,"formulaire_team.html",{"team" : ekip})

def index_team(request):
	ALLekip = models.Team_models.objects.all()
	emptylist = []
	for l in ALLekip:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	liste = list(models.Team_models.objects.all())
	return render(request,"index_team.html",{"listALL_team": liste, "randomID_team": random_id})

def affiche_team(request, id):
	ALLekip = models.Team_models.objects.all()
	ekip_container = list(models.Player.objects.filter(team_id=id))
	emptylist = []
	for l in ALLekip:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	ekip = models.Team_models.objects.get(pk=id)
	return render(request,'affiche_team.html',{"team": ekip, "team_container": ekip_container, "randomID_team": random_id})

def update_team(request, id):
	ALLekip = models.Team_models.objects.all()
	emptylist = []
	for l in ALLekip:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	ekip = models.Team_models.objects.get(pk=id)
	form1 = Team_forms(ekip.dictionnaire())
	return render(request,'formulaire_team.html',{"form_team": form1, "id_team":id, "randomID_team":random_id})

def updatetraitement_team(request, id):
	ALLekip = models.Team_models.objects.all()
	emptylist = []
	for l in ALLekip:
		emptylist.append(l.id)
		random_id = emptylist[random.randint(0,len(emptylist)-1)]
	form1 = Team_forms(request.POST)
	if form1.is_valid():
		ekip = form1.save(commit=False)
		ekip.id = id
		ekip.save()
		return HttpResponseRedirect("/team/")
	else:
		return render(request,"formulaire_team.html",{"form_team": form1, "id_team":id, "randomID_team": random_id})

def delete_team(request, id):
	team = models.Team_models.objects.get(pk=id)
	team.delete()
	return HttpResponseRedirect("/team/")





def traitement_PtoT(request, id):
    if request.method == "POST":
        form = player(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.team_id = id
            p.team = models.Team_models.objects.get(pk=id)
            p.save()
            return render(request, 'affiche_team.html', {'joueur': p, "id":id})
        else:
            return render(request, 'formulaire_player.html', {'form': form, "id":id})