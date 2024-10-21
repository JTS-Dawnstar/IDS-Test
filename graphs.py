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
with open("./2020-data.txt", mode = 'r') as file: 
    temp = file.read()

temp = temp.split('\n')
temp.remove('')
__data__ = [float(i) for i in temp]
del temp, file

class _data_obj: 
    def __init__(self): 
        pass
    def prediction(self, data, value): 
        return NotImplemented

data__object = _data_obj()"""

def handle_event(event):
    # will log `print(6 * 7)`
    event.code = setup_string + event.code
    display(event.code)
    # prevent default execution
    return True

# Grab reference to the editor
foreign = document.getElementById("g")
# Override handleEvent with your own customisation.
foreign.handleEvent = handle_event

display("Alright")
