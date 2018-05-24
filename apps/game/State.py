
class State:

    @staticmethod
    def render(state):
        output = ""
        for building in state.buildings.all():
            output += State.renderBuilding(building)
        return output

    @staticmethod
    def renderBuilding(building):
        output = ""
        output += "<div class='building " + building.type + " building_" + str(building.id) + "' id='" + str(building.id) + "'></div>"
        return output
