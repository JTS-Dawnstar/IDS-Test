with open("./2020-data.txt", mode = 'r') as file: 
    temp = file.read()

temp = temp.split('\n')
temp.remove('')
temperatures = [float(i) for i in temp]


import json

from js import Bokeh, JSON

from bokeh.embed import json_item
from bokeh.plotting import figure

# create a new plot with default tools, using figure
p = figure(width=400, height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
p.circle(list(range(len(temperatures))), temperatures, size=3, line_color="orange", fill_color="orange", fill_alpha=0.5)
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
# create a new plot with default tools, using figure
p = figure(width=400, height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
p.circle(list(range(len(temperatures))), temperatures, size=3, line_color="orange", fill_color="purple", fill_alpha=0.5)
p_json = json.dumps(json_item(p, "myplot"))
"""

def handle_event(event):
    code = setup_string + event.code + redraw_string
    display(code)
    exec(code, locals(), globals())
    return False

# Grab reference to the editor
foreign = document.getElementById("g")
# Override handleEvent with your own customisation.
foreign.handleEvent = handle_event

display("Alright")
