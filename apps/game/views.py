from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .Map import Map
from .models import *
from .Turn import Turn
from .State import State

def map(request):
    map = startGame()
    user = User.objects.filter(username='test')[0]
    request.session['user'] = user.id
    request.session['game'] = user.games.first().id
    context = {
        'map': map.render()
    }
    return render(request, 'game/map.html', context)

def startGame():
    user = None
    game = None
    users = User.objects.filter(username="test")
    if len(users) == 0:
        user = User.objects.create(username="test")
        user.save()
    else:
        user = users[0]
    games = GameData.objects.filter(user_id=user.id)
    if len(games) == 0:
        game = GameData.objects.create(user_id=user.id)
        game.save()
    else:
        game = games[0]
    map = Map()
    states = StateData.objects.filter(game_id=game.id)
    if len(states) == 0:
        map.create()
    return map

def state(request, state_name):
    game = GameData.objects.get(id=request.session['game'])
    state = game.states.filter(name__iexact=state_name)[0]
    context = {
        'state': state,
        'revenue': Turn.computeIncome(state),
        'GDP': Turn.computeGDP(state),
        'rendition': State.render(state),
        'traffic': int(Turn.computeTraffic(state) * 100),
        'crime': int(Turn.computeCrime(state) * 100),
        'education': int(Turn.computeEducation(state) * 100),
    }
    return render(request, 'game/state.html', context)

def getBuildingData(request, building_id):
    building = BuildingData.objects.get(id=building_id)
    json = "{\"type\": \""+ building.type +"\", \"status\": \"" + str(building.status) + "\", \"efficency\": \""+ str(building.efficency) + "\", \"size\": \""+ str(building.size) + "\"}"
    return HttpResponse(json)

def restart(request):
    GameData.objects.get(id=request.session['game']).delete()
    return redirect('/')

def turn(request):
    game = GameData.objects.get(id=request.session['game'])
    Turn.process(game)
    game.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    

def fixBuilding(request, building_id):
    building = BuildingData.objects.get(id=building_id)
    state = building.state
    if state.stats.money >= 2.5:
        building.status += 1
        building.save()
        state.stats.money -= 2.5
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def buyBuilding(request, state_id, type):
    state = StateData.objects.get(id=state_id)
    if state.stats.money >= 10:
        location = Map.generateLocation()
        size = 1
        if type == "road":
            size = 1 + state.tech.infrastructure
        elif type == "police":
            size = 1 + state.tech.police_training
        else:
            size = 1 + state.tech.curriculum
        building = BuildingData.objects.create(type=type, state_id=state.id, location_id=location.id, size=size)
        building.save()
        state.stats.money -= 10
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def improveTech(request, state_id, type):
    state = StateData.objects.get(id=state_id)
    if state.stats.money >= 20:
        if type == "road":
            state.tech.infrastructure += 1
        elif type == "police":
            state.tech.police_training += 1
        elif type == "school":
            state.tech.curriculum += 1
        state.tech.save()
        state.stats.money -= 20
        state.stats.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
