from Die import Die

# DiceGame Class
class DiceGame (object):
    # constructor makes 2 instances of the die with d1 and d2 name 
    def __init__(self):
        self.D1= Die()
        self.D2 = Die()
        
     # class play to roll and display values. 
    def Play(self):
        self.D1.Roll()
        fv1 = self.D1.GetFaceValue()
        print ("face value 1 : " + str(fv1))
        self.D2.Roll()
        fv2 = self.D2.GetFaceValue()
        print ("face value 2: " + str(fv2))
        fvSum = fv1 + fv2
        if fvSum==7:
            print("**********Hurra you win*********")
        else:
            print("************You loose************")    



