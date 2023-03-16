import random
class Player:
    def __init__ (self,pseudo,nse,msepc,fait,tablescore):
        self.pseudo = pseudo
        self.nse = nse
        self.msepc = msepc
        self.fait = fait
        self.tablescore = tablescore
    
    def getname(self):
        name=input()
        self.pseudo = name
        return self.pseudo

    def getnse(self):
        self.nse = 0
        return self.nse

    def getmsepc(self):
        return self.msepc

    def getfait(self):
        fait1 = 0
        fait2 = 0
        fait3 = 0
        fait4 = 0
        fait5 = 0
        choixMusique=random.randint(0,4)
        scoreMusique=random.randint(50,100)
        if choixMusique == 0:
            fait1 = 1
            scoreMusique=random.randint(50,100)
            self.tablescore[0]=scoreMusique
            return self.tablescore
        elif choixMusique == 1:
            fait2 = 1
            scoreMusique=random.randint(50,100)
            self.tablescore[1]=scoreMusique
            return self.tablescore
        elif choixMusique == 2:
            fait3 = 1
            scoreMusique=random.randint(50,100)
            self.tablescore[2]=scoreMusique
            return self.tablescore
        elif choixMusique == 3:
            fait4 = 1
            scoreMusique=random.randint(50,100)
            self.tablescore[3]=scoreMusique
            return self.tablescore
        elif choixMusique == 4:
            fait5 = 1
            scoreMusique=random.randint(50,100)
            self.tablescore[4]=scoreMusique
            return self.tablescore
        self.fait = fait1+fait2+fait3+fait4+fait5
        print(self.fait)
        return self.fait
        

if __name__ == "__main__":
    allie = Player("allie",0,[0,0,0,0,0],0,[0,0,0,0,0])
    