from django.shortcuts import render, redirect, HttpResponseRedirect
from .Map import Map
from .models import *
from .Turn import Turn

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
        'GDP': Turn.computeGDP(state)
    }
    return render(request, 'game/state.html', context)

def restart(request):
    GameData.objects.get(id=request.session['game']).delete()
    return redirect('/')

def turn(request):
    game = GameData.objects.get(id=request.session['game'])
    Turn.process(game)
    game.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def own_states(request):
    
