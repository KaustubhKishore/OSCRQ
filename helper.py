class Helper:

    nc = '\033[91m' + "[NC]" + '\033[0m' + " "
    c = '\33[32m' + "[C]" + '\033[0m' + " "
    info = '\33[94m' + "[INFO]" + '\033[0m' + " "

    def __init__(self):
        self.id = "unique id"
        
        self.score = 0
        self.infoScore = 0

        self.ncScore = 0
        self.ncInfoScore = 0
    

    def Compliant(self, audit):
        print("\n" + self.c + audit)
        print("-----------------")
        self.score += 1
    
    def NotCompliant(self, audit):
        print("\n" +self.nc + audit)
        print("-----------------")
        self.ncScore += 1

    def InfoCompliant(self, audit):
        print("\n" +self.info + self.c + audit)
        print("-----------------")
        self.infoScore +=1
    
    def InfoNotCompliant(self, audit):
        print("\n" +self.info + self.nc + audit)
        print("-----------------")
        self.ncInfoScore += 1   
    
    def score_getter(self):
        return self.score
    
    def infoScore_getter(self):
        return self.infoScore
    
    def ncScore_getter(self):
        return self.ncScore
    
    def ncInfoScore_getter(self):
        return self.ncInfoScore