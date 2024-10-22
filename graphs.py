with open("./2020-data.txt", mode = 'r') as file: 
    temp = file.read()

temp = temp.split('\n')
temp.remove('')
temperatures = [float(i) for i in temp]

PRED_RANGE = range(len(temperatures))


import json

from js import Bokeh, JSON

from bokeh.embed import json_item
from bokeh.plotting import figure

# create a new plot with default tools, using figure
p = figure(width=400, height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
p.scatter(list(range(len(temperatures))), temperatures, size=3, line_color="orange", fill_color="orange", fill_alpha=0.5)
p_json = json.dumps(json_item(p, "myplot"))

Bokeh.embed.embed_item(JSON.parse(p_json))



from pyscript import document, display

setup_string = """
class _data_obj: 
    def __init__(self): 
        pass
    def prediction(self, data, value): 
        return NotImplemented

data__object = _data_obj()"""

redraw_string = """
preds = [data__object.prediction(temperatures, value) for value in PRED_RANGE]

# create a new plot with default tools, using figure
p = figure(width=400, height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
p.scatter(list(PRED_RANGE), temperatures, size=3, line_color="green", fill_color="green", fill_alpha=0.5)
p.line(list(PRED_RANGE), preds, line_width = 2, color = "red")
p_json = json.dumps(json_item(p, "myplot"))

previous = document.getElementById("myplot")
previous.removeChild(previous.firstChild)

Bokeh.embed.embed_item(JSON.parse(p_json))
"""

def handle_event(event):
    code = setup_string + str(event.code) + redraw_string
    display(code)
    exec(code, locals(), globals())
    return False

# Grab reference to the editor
foreign = document.getElementById("g")
# Override handleEvent with your own customisation.
foreign.handleEvent = handle_event

display("Alright")
