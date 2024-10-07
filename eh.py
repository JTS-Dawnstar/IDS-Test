from pyscript import document, display

def handle_event(event):
    # will log `print(6 * 7)`
    display(event.code)
    # prevent default execution
    return True

# Grab reference to the editor
foreign = document.getElementById("g")
# Override handleEvent with your own customisation.
foreign.handleEvent = handle_event

display("Alright")