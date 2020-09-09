from tkinter import *

class Tablero():
	
	def __init__(self):
		
		self.root = Tk()
		
		self.img_casella_buida = PhotoImage(file="Fitxes_tres_en_ralla/res.png")
		
		self.img_casella_rodona = PhotoImage(file="Fitxes_tres_en_ralla/rodona.png")
		
		self.img_casella_creu = PhotoImage(file="Fitxes_tres_en_ralla/creu.png")
		
		self.frame_casilles = Frame(self.root)
		self.frame_casilles.pack()
		
		self.casilla_a1 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_a1.grid(row=0, column=0)
		
		self.casilla_a2 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_a2.grid(row=1, column=0)
		
		self.casilla_a3 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_a3.grid(row=2, column=0)
		
		self.casilla_b1 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_b1.grid(row=0, column=1)
		
		self.casilla_b2 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_b2.grid(row=1, column=1)
		
		self.casilla_b3 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_b3.grid(row=2, column=1)
		
		self.casilla_c1 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_c1.grid(row=0, column=2)
		
		self.casilla_c2 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_c2.grid(row=1, column=2)
		
		self.casilla_c3 = Button(self.frame_casilles, image = self.img_casella_buida)
		self.casilla_c3.grid(row=2, column=2)
		

		
		"""	
				|				|
					|				|
					|				|
			A1		|		B1		|	C1
					|				|
					|				|
		-----------------------------------------
					|				|
					|				|
			A2		|		B2		|	C2
					|				|	
					|				|
					|				|
		-----------------------------------------
					|				|
					|				|
			A3		|		B3		|	C3
					|				|
					|				|
					|				|
		
		"""
		self.root.mainloop()
		
tablero = Tablero()
