from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import Schelling


class HappyElement(TextElement):
    """
    Display a text count of how many happy agents there are.
    """

    def __init__(self):
        pass

    def render(self, model):
        return "Happy agents: " + str(model.happy)


def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.8, "Filled": "true", "Layer": 0}

    if agent.type == 0:
        portrayal["Color"] = ["#10145F", "#10145F"]
        portrayal["stroke_color"] = "#B7FDFF"
    else:
        portrayal["Color"] = ["#EAE315", "#EAE315"]
        portrayal["stroke_color"] = "#000000"
    return portrayal


happy_element = HappyElement()
canvas_element = CanvasGrid(schelling_draw, 100, 100, 800, 800)
happy_chart = ChartModule([{"Label": "happy", "Color": "Black"}])

# chart = ChartModule([{"Label": "Num_Explorer","Color" : "Black"}, {"Label": "Num_Exploiter","Color": "Red"}],data_collector_name = 'datacollector')
# server = ModularServer(World, [grid, chart], "Demo", {"N": 100, "coop": 0.5})

model_params = {
    "height": 100,
    "width": 100,
    "density": UserSettableParameter("slider", "Agent density", 0.7, 0.1, 1.0, 0.1),
    "minority_pc": UserSettableParameter(
        "slider", "Fraction minority", 0.2, 0.00, 1.0, 0.05
    ),
    "homophily": UserSettableParameter("slider", "Homophily", 3, 0, 8, 1),
}

server = ModularServer(
    Schelling, [canvas_element, happy_element, happy_chart], "Schelling", model_params
)
