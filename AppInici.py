from tkinter import *
from tkinter import messagebox 

class AppInici():
	
	def __init__(self):
		
		self.root = Tk()
		
		self.root.title("Configuració inicial")
		
		self.frame = Frame(self.root, padx=10, pady=10)
		self.frame.pack()
		
		self.label_nom_jugador_1 = Label(self.frame, text = "Nom del jugador 1:")
		self.label_nom_jugador_1.grid(row=0, column=0, sticky=E)
		
		self.label_nom_jugador_2 = Label(self.frame, text = "Nom del jugador 2:", state = DISABLED)
		self.label_nom_jugador_2.grid(row=1, column=0, sticky=E)

		
		self.txt_nom_jugador_1 = StringVar()
		self.txt_nom_jugador_2 = StringVar()
		
		
		self.entry_jugador_1 = Entry(self.frame, textvariable=self.txt_nom_jugador_1)
		self.entry_jugador_1.grid(row=0,column=1)
		
		self.entry_jugador_2 = Entry(self.frame, state=DISABLED, textvariable=self.txt_nom_jugador_2)
		self.entry_jugador_2.grid(row=1,column=1)
		
		
		self.frame2 = Frame(self.root)
		self.frame2.pack()
		
		self.label_mode_de_joc = Label(self.frame2, text = "Mode de joc:")
		self.label_mode_de_joc.grid(row=0, column=0, sticky=E)
		
		self.opcio = IntVar()
		
		self.radiobutton_facil = Radiobutton(self.frame2, text="Indrividual FÀCIL", value = 1, variable = self.opcio, command=self.desactivar_segon_jugador)
		self.radiobutton_facil.grid(row=0, column=1, sticky=W)
		
		self.radiobutton_facil = Radiobutton(self.frame2, text="Indrividual NORMAL", value = 2, variable = self.opcio, command=self.desactivar_segon_jugador)
		self.radiobutton_facil.grid(row=1, column=1, sticky=W)
		
		self.radiobutton_facil = Radiobutton(self.frame2, text="Indrividual DIFÍCIL", value = 3, variable = self.opcio, command=self.desactivar_segon_jugador)
		self.radiobutton_facil.grid(row=2, column=1, sticky=W)
		
		self.radiobutton_facil = Radiobutton(self.frame2, text="Multijugador local", value = 4, variable = self.opcio, command=self.activar_segon_jugador)
		self.radiobutton_facil.grid(row=3, column=1, sticky=W)
		
		self.frame3 = Frame(self.root, padx=10, pady=10)
		self.frame3.pack()
		
		self.boto_aceptar = Button(self.frame3, text="Aceptar", command=lambda:self.boto_aceptar_apretat())
		self.boto_aceptar.pack()
		
		self.aceptar = False
		
		self.nom_jugador_1 = ""
		
		self.nom_jugador_2 = ""

		self.mode_de_joc = ""
		
		self.errors = False
		
		self.root.mainloop()

	def activar_segon_jugador(self):
		
		self.label_nom_jugador_2.config(state=NORMAL)
		self.entry_jugador_2.config(state=NORMAL)
		
	def desactivar_segon_jugador(self):
		
		self.label_nom_jugador_2.config(state=DISABLED)
		self.entry_jugador_2.config(state=DISABLED)
		self.txt_nom_jugador_2.set("")
	
	def detectar_erroros(self):


		if self.txt_nom_jugador_1.get() == "":
			
			self.errors = True
			
		elif self.opcio.get() != 1 and self.opcio.get() != 2 and self.opcio.get() != 3:
			
			if self.opcio.get() == 4 and self.txt_nom_jugador_2.get() != "":
				self.errors = False
				
			else:
				self.errors = True
			
		
		return self.errors
		
		
	
	def boto_aceptar_apretat(self):
		
		#funcio per a detectar errors
		
		self.aceptar = True
		
		self.errors = False
		
		self.detectar_erroros()
		
		self.nom_jugador_1 = self.txt_nom_jugador_1.get()
		self.nom_jugador_2 = self.txt_nom_jugador_2.get()	
		self.mode_de_joc = self.opcio.get()
		
		if self.detectar_erroros() == True:
			
			messagebox.showwarning("INCORRECTE", "Introdueix totes les dades correctament.")
			
		else: 
			messagebox.showinfo("INFORMACIÓ", "Totes les dades s'han registrat correctament.")
			
			self.root.quit()
		
# Al finalitzar aquesta classe no s'ha de cridar es cridara en un arxiu diferent això nomes es per fer proves

		
#inici = AppInici()	

#print(inici.nom_jugador_1, inici.nom_jugador_2, inici.mode_de_joc, inici.aceptar)

"""
inici.nom_jugador_1 -> Nom del jugador 1

inici.nom_jugador_2 -> Nom del jugador 2

inici.mode_de_joc -> Mode de joc selecionat --  1: Facil individual, 2: Normal individual, 3: Dificil individual, 4: Multijugador local

inici.aceptar -> Per saber si li ha donat al boto Aceptar o a tancat l'app per la creueta de dalt -- True: Ha apretat el boto aceptar, False: Ha apretat la creueta

"""

