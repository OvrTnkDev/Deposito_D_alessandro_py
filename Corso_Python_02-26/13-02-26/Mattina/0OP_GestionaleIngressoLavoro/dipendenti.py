import random as rnd

# creazione classe Dipendente con nome e ruolo
class Dipendente():
    def __init__(self, nome, ruolo):
        self.nome = nome
        self.ruolo = ruolo
        
    def __str__(self):
        return f"{self.nome} ({self.ruolo})"
      

# creazione badge per dipendenti con badge_id casuale
class Badge(Dipendente):
  
  dip_db = {}
  # incapsulamento: badge_id è un attributo privato, accessibile solo tramite i metodi getter e setter
  def __init__(self, nome, ruolo):
      # ereditarietà: Badge è una sottoclasse di Dipendente, quindi eredita gli attributi e i metodi di Dipendente
      super().__init__(nome, ruolo)
      self.set_badge_id(rnd.randint(1000, 9999))  # badge_id è un numero casuale a 4 cifre
  
  # getter per badge_id, permette di accedere al badge_id in modo controllato
  def get_badge_id(self):
      return self.__badge_id
  
  # setter per badge_id, permette di modificare il badge_id in modo controllato
  def set_badge_id(self, badge_id):
      self.__badge_id = badge_id
  
  # polimorfismo: il metodo __str__ è sovrascritto per fornire una rappresentazione stringa specifica per la classe Badge
  def __str__(self):
      return super().__str__() +  f" - BadgeID: {self.get_badge_id()}"
    
  def salva_dipendente(self):
      # salva il dipendente in un database simulato (un dizionario)
      self.dip_db[self.get_badge_id()] = self
      print(f"Dipendente {self.nome} salvato con badge ID {self.get_badge_id()}")
  
  def recupera_dipendente(self, badge_id):
      # recupera un dipendente dal database simulato usando il badge_id
      dipendente = self.dip_db.get(badge_id, None)
      if dipendente:
          print(f"Dipendente trovato: {dipendente}")
          return dipendente
      else:
          print(f"Nessun dipendente trovato con badge ID {badge_id}")
          return None

"""#provo a creare un dipendente e un badge per quel dipendente
d_OBJ = Badge("Fabio D'alessandro", "Sviluppatore")
print(d_OBJ)
d_OBJ.salva_dipendente()
d_OBJ.recupera_dipendente(d_OBJ.get_badge_id())"""