# henrietta.morgan.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

parede1 = "https://i.imgur.com/Yn75ZF2.jpg"
parede2 = "https://i.imgur.com/4Xx7uox.jpg"
parede3 = "https://i.imgur.com/icYyd5H.jpg"

class Cenatectonica():
   def __init__(self):
    self.parede1 = Cena(img = parede1)
    self.parede2 = Cena(parede2, direita=self.parede1)
    self.parede3 = Cena(parede3, esquerda=self.parede2)
    
    
    self.parede2.vai()
   def vai(self, *_):
    self.parede2.vai()
    
def Game():
  parede2 = Cenatectonica()
  parede2.vai()

if __name__ == "__main__":
	Game()
    
