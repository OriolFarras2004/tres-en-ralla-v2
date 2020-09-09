from tkinter import *

class Tablero():
	
	def __init__(self):
		
		self.root = Tk()
		
		self.root.config(pady=10)
		
		self.root.title("TRES EN RALLA")
		
		self.root.geometry("400x500")
		
		self.root.resizable(width=False, height=False)
		
		self.img_casella_buida = PhotoImage(file="Fitxes_tres_en_ralla/res.png")
		
		self.img_casella_rodona = PhotoImage(file="Fitxes_tres_en_ralla/rodona.png")
		
		self.img_casella_creu = PhotoImage(file="Fitxes_tres_en_ralla/creu.png")
		
		self.frame_titiol = Frame(self.root)
		self.frame_titiol.pack()
		
		self.label_titol = Label(self.frame_titiol, text = "Tres en ralla - ", font=('Helvetica', 16, 'bold'), justify="left")
		self.label_titol.grid(row=0,column=0, sticky="e")
		
		self.frame_casilles = Frame(self.root, padx=10,pady=10)
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
		
		self.frame_informacio = Frame(self.root, padx=10, pady=20, bg = "#BFBFBF")
		self.frame_informacio.pack()
		
		self.label_J1 = Label(self.frame_informacio, text = "J1", font=('Helvetica', 12, 'bold'), bg = "#BFBFBF")
		self.label_J1.grid(row=0, column=0, padx = 30)
		
		self.label_empat = Label(self.frame_informacio, text = "Empats", font=('Helvetica', 12, 'bold'), bg = "#BFBFBF")
		self.label_empat.grid(row=0, column=1, padx = 30)
		
		self.label_J2 = Label(self.frame_informacio, text = "J2", font=('Helvetica', 12, 'bold'), bg = "#BFBFBF")
		self.label_J2.grid(row=0, column=2, padx = 30)
		
		self.punts_J1 = Label(self.frame_informacio, text = "0", bg = "#BFBFBF")
		self.punts_J1.grid(row=1, column=0, padx = 30)
		
		self.punts_empat = Label(self.frame_informacio, text = "0", bg = "#BFBFBF")
		self.punts_empat.grid(row=1, column=1, padx = 30)
		
		self.punts_J2 = Label(self.frame_informacio, text = "0", bg = "#BFBFBF")
		self.punts_J2.grid(row=1, column=2, padx = 30)
		


		self.root.mainloop()
		
	def canviar_titol(self, titol):
		
		self.label_titol.config(text=str(titol))
		
	def canviar_nom_J1(self, nom):
		
		self.label_J1.config(text=str(nom))
		
	def canviar_nom_J2(self, nom):
		
		self.label_J2.config(text=str(nom))

	def canviar_puntuacio_J1(self, puntuacio):
		
		self.punts_J1.config(text=puntuacio)
		
	def canviar_puntuacio_empat(self, puntuacio):
		
		self.punts_empat.config(text=puntuacio)
		
	def canviar_puntuacio_J2(self, puntuacio):
		
		self.punts_J2.config(text=puntuacio)
	
	def posar_ficha(self, posicio, tipus):
		
		if posicio == "a1" and tipus == "x":
			
			self.casilla_a1.config(image= self.img_casella_creu)
			
		elif posicio == "a1" and tipus == "o":
			
			self.casilla_a1.config(image= self.img_casella_rodona)
			
		elif posicio == "a2" and tipus == "x":
			
			self.casilla_a2.config(image= self.img_casella_creu)
			
		elif posicio == "a2" and tipus == "o":
			
			self.casilla_a2.config(image= self.img_casella_rodona)
			
		elif posicio == "a3" and tipus == "x":
			
			self.casilla_a3.config(image= self.img_casella_creu)
			
		elif posicio == "a3" and tipus == "o":
			
			self.casilla_a3.config(image= self.img_casella_rodona)
			
		elif posicio == "b1" and tipus == "x":
			
			self.casilla_b1.config(image= self.img_casella_creu)
			
		elif posicio == "b1" and tipus == "o":
			
			self.casilla_b1.config(image= self.img_casella_rodona)
			
		elif posicio == "b2" and tipus == "x":
			
			self.casilla_b2.config(image= self.img_casella_creu)
			
		elif posicio == "b2" and tipus == "o":
			
			self.casilla_b2.config(image= self.img_casella_rodona)
			
		elif posicio == "b3" and tipus == "x":
			
			self.casilla_b3.config(image= self.img_casella_creu)
			
		elif posicio == "b3" and tipus == "o":
			
			self.casilla_b3.config(image= self.img_casella_rodona)
			
		elif posicio == "c1" and tipus == "x":
			
			self.casilla_c1.config(image= self.img_casella_creu)
			
		elif posicio == "c1" and tipus == "o":
			
			self.casilla_c1.config(image= self.img_casella_rodona)
			
		elif posicio == "c2" and tipus == "x":
			
			self.casilla_c2.config(image= self.img_casella_creu)
			
		elif posicio == "c2" and tipus == "o":
			
			self.casilla_c2.config(image= self.img_casella_rodona)
			
		elif posicio == "c3" and tipus == "x":
			
			self.casilla_c3.config(image= self.img_casella_creu)
			
		elif posicio == "c3" and tipus == "o":
			
			self.casilla_c3.config(image= self.img_casella_rodona)
			


#tablero = Tablero()
"""
Per a canviar el titol -> canviar_titol("Nom del titol")

Per canviar nom del jugador 1 -> canviar_nom_J1("nom del jugador 1")

Per canviar nom del jugador 2 -> canviar_nom_J2("nom del jugador 2")

Per a canvair la puntuacio del jugador 1 -> canviar_putuacio_J1(punts)  ex: punts = 1

Per a canvair la puntuacio del jugador 2 -> canviar_putuacio_J2(punts)  ex: punts = 1

Per a canvair la puntuacio del empat -> canviar_putuacio_empat(punts)  ex: punts = 1

Per a posar una ficha -> posar_ficha(posicio, tipus_de_ficha)  ex: posicio = "a1", tipus_de_ficha = "x" or "o" 


"""


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
