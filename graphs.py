with open("./lvl1-data.txt", mode = 'r') as file: 
    temp = file.read()

temp = temp.split('\n')
# temp.remove('')
_data = [float(i) for i in temp]

KNOWN_RANGE = range(40)
PRED_RANGE = range(60, 70)
known_data = [_data[i] for i in KNOWN_RANGE]

import json

from js import Bokeh, JSON

from bokeh.embed import json_item
from bokeh.plotting import figure

import numpy as np

# create a new plot with default tools, using figure
p = figure(width=400, height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
p.scatter(list(KNOWN_RANGE), known_data, size=3, line_color="green", fill_color="green", fill_alpha=0.5)

p.vstrip(x0 = [KNOWN_RANGE.start], x1 = [KNOWN_RANGE.stop], fill_color = "green", fill_alpha = 0.2)
p.vstrip(x0 = [PRED_RANGE.start], x1 = [PRED_RANGE.stop], fill_color = "red", fill_alpha = 0.2)

p.hstrip(y0 = [0], y1 = [0], line_color = "black", line_dash = 'dashed')
p.vstrip(x0 = [0], x1 = [0], line_color = "black", line_dash = 'dashed')

p_json = json.dumps(json_item(p, "myplot"))

Bokeh.embed.embed_item(JSON.parse(p_json))



from pyscript import document, display

setup_string = """

class __data__: 
    x = list(KNOWN_RANGE)
    y = known_data

class _data_obj: 
    def __init__(self): 
        pass
    def prediction(self, value): 
        return NotImplemented

data__object = _data_obj()"""

redraw_string = """
preds = [data__object.prediction(value) for value in list(range(len(_data)))]

# Stuff with RMSE. 
truth = np.array([_data[i] for i in PRED_RANGE])
measured = np.array([preds[i] for i in PRED_RANGE]) # The 'preds' var comes from 'redraw_string' in the exec. 

rmse = np.linalg.norm(measured - truth) / np.sqrt(len(truth))
if rmse <= 5: 
    display("Average Error: " + str(rmse) + ". \\n Your average error was less than 5! You passed the level! ", append = False)
else: 
    display("Average Error: " + str(rmse) + ". ", append = False)


# create a new plot with default tools, using figure
p = figure(width=400, height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
if rmse <= 5: 
    p.scatter(list(range(len(_data))), _data, size=3, line_color="green", fill_color="green", fill_alpha=0.5)
else: 
    p.scatter(list(KNOWN_RANGE), known_data, size=3, line_color="green", fill_color="green", fill_alpha=0.5)
p.line(list(range(len(_data))), preds, line_width = 2, color = "red")

p.vstrip(x0 = [KNOWN_RANGE.start], x1 = [KNOWN_RANGE.stop], fill_color = "green", fill_alpha = 0.2)
p.vstrip(x0 = [PRED_RANGE.start], x1 = [PRED_RANGE.stop], fill_color = "red", fill_alpha = 0.2)

p.hstrip(y0 = [0], y1 = [0], line_color = "black", line_dash = 'dashed')
p.vstrip(x0 = [0], x1 = [0], line_color = "black", line_dash = 'dashed')

p_json = json.dumps(json_item(p, "myplot"))

previous = document.getElementById("myplot")
previous.removeChild(previous.firstChild)

Bokeh.embed.embed_item(JSON.parse(p_json))
"""

def handle_event(event):
    code = setup_string + str(event.code) + redraw_string
    # display(code)
    exec(code, globals(), globals())
    
    return False

# Grab reference to the editor
foreign = document.getElementById("g")
# Override handleEvent with your own customisation.
foreign.handleEvent = handle_event

# display("Alright")
