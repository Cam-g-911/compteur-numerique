let personne = 0
input.onButtonPressed(Button.A, function () {
    personne = personne + 1
    basic.showNumber(personne)
})
input.onButtonPressed(Button.B, function () {
    personne = personne - 1
    basic.showNumber(personne)
})
basic.forever(function () {
	
})
