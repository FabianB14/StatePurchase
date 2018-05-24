from .Roll import Roll

class Turn:

    @staticmethod
    def process(game):
        for state in game.states.all():
            Turn.processState(state)

    @staticmethod
    def processState(state):
        state.stats.money += Turn.computeIncome(state)
        state.stats.population *= 1.01
        state.stats.traffic = Turn.computeTraffic(state)
        state.stats.crime = Turn.computeCrime(state)
        state.stats.education = Turn.computeEducation(state)
        state.stats.save()
        Turn.breakdown(state)
        state.save()

    @staticmethod
    def breakdown(state):
        for building in state.buildings.all():
            if Roll.chance(0.25):
                if building.status != 0:
                    building.status -= 1
            building.save()

    @staticmethod
    def computeIncome(state):
        return Turn.computeGDP(state) * 0.1

    @staticmethod
    def computeGDP(state):
        return state.stats.population
    
        traffic = 1 - min(Turn.computeTraffic(state), 1)
        crime = state.stats.population * min(Turn.computeCrime(state), 1)
        return max(state.stats.population * traffic - crime * 0.5, 0)

    @staticmethod
    def computeTraffic(state):
        roads = state.buildings.filter(type="road")
        capacity = Turn.computeTrafficCapacity(roads)
        if capacity == 0:
            return 1
        base = (state.stats.population * 0.2) / capacity
        return base

    @staticmethod
    def computeTrafficCapacity(roads):
        capacity = 0.0
        for road in roads:
            status = float(road.status) / 2.0
            efficency = float(road.efficency) / 2.0
            size = float(road.size) / 10.0
            capacity += status * (efficency + 0.5) * 300.0 * size
        return capacity

    @staticmethod
    def computeCrime(state):
        stations = state.buildings.filter(type="police")
        capacity = Turn.computeCrimeCapacity(stations)
        if capacity == 0:
            return 1
        base = (state.stats.population * 0.1) / capacity
        return base

    @staticmethod
    def computeCrimeCapacity(stations):
        capacity = 0.0
        for station in stations:
            status = float(station.status) / 2.0
            efficency = float(station.efficency) / 2.0
            size = float(station.size) / 10.0
            capacity += status * (efficency + 0.5) * 200.0 * size
        return capacity

    @staticmethod
    def computeEducation(state):
        schools = state.buildings.filter(type="school")
        capacity = Turn.computeSchoolCapacity(schools)
        if capacity == 0:
            return 0
        base = (capacity * 3) / state.stats.population
        return base

    @staticmethod
    def computeSchoolCapacity(stations):
        capacity = 0.0
        for station in stations:
            status = float(station.status) / 2.0
            efficency = float(station.efficency) / 2.0
            size = float(station.size) / 10.0
            capacity += status * (efficency + 0.5) * 20.0 * size
        return capacity
