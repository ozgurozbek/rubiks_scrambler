from flask import *
import random
import time

app = Flask(__name__)

#Notation
notation_r = ["R", "R'", "R2"]
notation_l = ["L", "L'", "L2"]
notation_u = ["U", "U'", "U2"]
notation_d = ["D", "D'", "D2"]
notation_f = ["F", "F'", "F2"]
notation_b = ["B", "B'", "B2"]
notation = [notation_r, notation_l, notation_u, notation_d, notation_f, notation_b]

#Oppose function
def oppose(current):
    if current == "R":
        return "L"
    if current == "L":
        return "R"
    if current == "U":
        return "D"
    if current == "D":
        return "U"
    if current == "F":
        return "B"
    if current == "B":
        return "F"
        

@app.route("/")
def root():
    printer = []
    notation_web = []
    debug_web = []
    old = ""
    i = 0
    while i != 20:

        #Pick a Notation Group
        ex = random.choice(notation)
        placeholder = str(ex[0])
        debug_web.append(placeholder)

        if old == placeholder: #Yenisi eskisiyle aynıysa
            debug_web.append("<- Same as previous, skipping...")

        elif old != oppose(placeholder): #Yenisinin zıttı eskisine aynı değilse
            #Pick a Notation
            captive = random.choice(ex)
            printer.append(captive)
            i = i + 1
            old = placeholder

        elif old == oppose(placeholder): #Yenisinin zıttı eskisiyle aynıysa
            debug_web.append("<- Oppose mistake, skipping...")

    notation_web = (' '.join(printer))
    debug_web = (' '.join(debug_web))

    return render_template('home.html', notation_web=notation_web, debug_web=debug_web)

if __name__ == '__main__':
    app.run(debug=True)