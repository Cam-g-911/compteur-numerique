personne = 0

def on_button_pressed_a():
    global personne
    personne = personne + 1
    basic.show_number(personne)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global personne
    personne = personne - 1
    basic.show_number(personne)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
