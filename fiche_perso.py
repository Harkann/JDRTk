import tkinter as tk
from tinydb import TinyDB, Query

class ListeFiches(tk.Frame):
    """ Liste toutes les fiches de personnages contenues dans la bdd configurée """
    def __init__(self, init_menu, jdr_name, master=None):
        self.master = master
        super().__init__(master)
        self.init_menu = init_menu
        self.jdr_name = jdr_name
        self.database = TinyDB(jdr_name+"/personnages.json") #fichier dans lequel sont stockés tous les personnages.
        self.pack()
        self.master.title("Liste des Personnages")
        self.display_fiches()

    def new_fiche(self):
        self.destroy()
        app = FichePerso(self.master,None,self.database)

    def display_fiches(self):
        liste_persos = []
        liste_fonctions = []


        for perso in self.database.search(Query().nom.exists()):
            print(perso["nom"])
            liste_persos.append(tk.Button(self, text = perso["nom"], command = lambda : self.fiche(perso["nom"])))
            liste_persos[-1].pack(side="top")
        self.new_fiche = tk.Button(self, text = "Nouveau Personnage", command = self.new_fiche)
        self.new_fiche.pack(side="top")
        self.back_main = tk.Button(self, text="Menu Principal", command=self.back_menu)
        self.back_main.pack(side="bottom")

    def fiche(self,personnage):
        self.destroy()
        app = FichePerso(self.master,personnage,self.database)

    def back_menu(self):
        app = self.init_menu(self)

class FichePerso(tk.Frame):
    """ Gère l'affichage d'une fiche de personnage """
    def __init__(self, master=None, personnage=None,database=None):
        super().__init__(master)
        if personnage:
            self.personnage = database.search(Query().nom == personnage)
        else:
            self.personnage = None
        print(self.personnage)
        self.database = database
        self.pack()
        self.master.title("Fiche Personnage")
        print("TODO : Afficher fiche perso")
        self.resume = ResumePerso(master=self,personnage=self.personnage,database=self.database)
        self.resume.pack(side="top")
        self.save = tk.Button(self, text = "Sauvegarder", command=self.save_all)
        self.save.pack(side="bottom")

    def save_all(self):
        self.resume.save()

class ResumePerso(tk.Frame):
    def __init__(self, master=None, personnage=None,database=None):
        super().__init__(master)
        self.pack()
        if personnage:
            self.personnage = personnage[0]
        else : self.personnage = None
        self.database = database
        self.nom = tk.Text(self,heigh=1,width=20)
        tk.Label(self, text="Nom").grid(row=0,sticky="E")
        if self.personnage:
            self.nom.insert(tk.END,self.personnage["nom"])
        self.nom.grid(row=0,column=1, sticky="W")
        self.origine = tk.Text(self,heigh=1,width=20)
        if self.personnage:
            self.origine.insert(tk.END,self.personnage["origine"])
        tk.Label(self, text="Origine").grid(row=0,column=2,sticky="E")
        self.origine.grid(row=0,column=3,sticky="W")
        if self.personnage:
            self.metiers = self.personnage["metiers"]
        else : self.metiers = [""]
        self.metiers_frame = tk.Frame(self)
        self.metiers_fields = []
        for i in self.metiers :
            self.metiers_fields.append(tk.Text(self.metiers_frame,heigh=1,width=20))
            self.metiers_fields[-1].insert(tk.END,i)
            self.metiers_fields[-1].pack(side="left")
        tk.Label(self, text="Métiers").grid(row=1,sticky="E")
        self.metiers_frame.grid(row=1,column=1,sticky="W")
        self.genre = tk.Text(self,heigh=1,width=20)
        if self.personnage:
            self.genre.insert(tk.END,self.personnage["genre"])
        tk.Label(self, text="Genre").grid(row=1,column=2,sticky="E")
        self.genre.grid(row=1,column=3,sticky="W")
        self.niveau = tk.Text(self,heigh=1,width=2)
        if self.personnage:
            self.niveau.insert(tk.END,self.personnage["niveau"])
        tk.Label(self, text="Niveau").grid(row=0,column=4,sticky="E")
        self.niveau.grid(row=0,column=5,sticky="W")
        self.xp = tk.Text(self,heigh=1,width=2)
        if self.personnage:
            self.xp.insert(tk.END,self.personnage["xp"])
        tk.Label(self, text="Xp").grid(row=1,column=4,sticky="E")
        self.xp.grid(row=1,column=5,sticky="W")
        self.destin = tk.Text(self,heigh=1,width=2)
        if self.personnage:
            self.destin.insert(tk.END,self.personnage["destin"])
        tk.Label(self, text="Pts. Destin").grid(row=2,column=4,sticky="E")
        self.destin.grid(row=2,column=5,sticky="W")
        self.PV = [0]
        self.PA = [0]
        self.image = None

    def save(self):
        if self.personnage:
            print("TODO : Editer perso")
        else :
            self.database.insert({"nom" : self.nom.get("1.0",tk.END),
                                  "origine" : self.origine.get("1.0",tk.END),
                                  "metiers" : [i.get("1.0",tk.END) for i in self.metiers_fields],
                                  "genre" : self.genre.get("1.0",tk.END),
                                  "niveau" : self.niveau.get("1.0",tk.END),
                                  "xp" : self.xp.get("1.0",tk.END),
                                  "destin" : self.destin.get("1.0",tk.END),})
                       #"PV" : valueGET(self.PV.get())
                       #"PA" : valueGET(self.PA.get())
                       #"image" : valueGET(self.image.get()) })
            self.personnage = self.nom.get("1.0",tk.END)

class CaracRichessesPerso(tk.Frame):
    pass

class ArmesCompPerso(tk.Frame):
    pass
class StuffPerso(tk.Frame):
    pass
