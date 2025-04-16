class Skolens:
    def __init__(self, vards, klase):
        self.vards = vards
        self.klase = klase

class Skolotajs:
    def __init__(self, vards, uzvards,prieksmets):
        self.vards = vards
        self.uzvards = uzvards
        self.prieksmets = prieksmets
        
class Skola:
    def __init__(self, nosaukums, adrese):
        self.nosaukums = nosaukums
        self.adrese = adrese
        
        
class Klase:
    def __init__(self, nosaukums, skolotajs):
        self.nosaukums = nosaukums
        self.skolotajs = skolotajs
        
class Prieksmets:
    def __init__(self, nosaukums, klase):
        self.nosaukums = nosaukums
        self.klase = klase
        
       