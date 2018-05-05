ScreenManagement:
	transition:
	First:
	Calculator:







<First>:
	name: 'first'
	canvas:
		Rectangle:
			source: 'bmilook.jpg'
			size: self.size
			pos: self.pos



	GridLayout:
		rows: 3
		Label:
			text:"BMI Calculatr\nBy Simeon Ikudabo"
			markup: True
			font_size: 30
		Label:
			text: "Copyright @2017 \nApple Store, Google play, Windows 10"
			markup: True
			font_size: 30


		Button:
			on_release: app.root.current = 'next'
			text: 'Continue'
			font_size: 30
			size_hint: .1, .1


<Calculator>:
	name: 'next'
	canvas:
		Rectangle:
			source: 'bmilook.jpg'
			size: self.size
			pos: self.pos


	GridLayout:
		rows: 4
		columns: 3#One row for now because I have two objects. Take the number of objects divided by the number 2 to get a valid number of rows 
		Label: 
			text: 'Enter your weight in pounds!'

		TextInput:
			id: weight
			multiline: False

		Label:
			text: 'Enter your height in inches!'

		TextInput:
			id: height
			multiline: False 

		Label:
			text: 'Results'

		TextInput:
			text: ''
			id: results 

		Button:
			text: 'Calculate'




