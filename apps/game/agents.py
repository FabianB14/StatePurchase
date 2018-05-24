from .models import * 
from django.shortcuts import render, redirect, HttpResponseRedirect
from .Map import Map



class agentOperations:
    def levels(self,Map):
        
        Agent = User.objects.get(agent = 'agent_id')
        Agent_level = User.objects.create(level = 'Governor')
        if AgentData.state.all() > 2:
            Agent = User.objects.create(level = 'Local Senator')
        if AgentData.state.all() >5:
            Agent = User.objects.create(level = 'Regional Senator')
        if AgentData.state.all() == 10:
            Agent = User.objects.create(level= 'President')
        if Agent == User.objects.get(level = 'God Emperor'):
            Agent = User.objects.create(Level = 'Winner')
        return Agent





