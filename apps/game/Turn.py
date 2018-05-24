
class Turn:

    @staticmethod
    def process(game):
        for state in game.states.all():
            Turn.processState(state)

    @staticmethod
    def processState(state):
        state.stats.money += Turn.computeIncome(state)
        state.stats.population *= 1.01
        state.stats.save()
        state.save()

    @staticmethod
    def computeIncome(state):
        return Turn.computeGDP(state) * 0.1

    @staticmethod
    def computeGDP(state):
        return state.stats.population
    
