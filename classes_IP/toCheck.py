#It will be used for the Birthday
import datetime

# Class use uppercase, object lowercase (Best Practices)
class Person:
    #The attribute "birthday" has a default (if we do not provide a value when we start the object)
    #The __init__ is used whenever an object of the class is constructed
    def __init__(self,name,birthday='2000/05/12'):
        # the attribute "name"  it's a private attribute, try to access it later
        self.__name = name
        #self.birthday = birthday
        self.birthday = datetime.datetime.strptime(birthday, '%Y/%m/%d')
        self.color = None
        
    #Attribute color, it was defined on the construction of the object with the None value
    def setColor(self, color):
        self.color = color
            
    def getColor(self):
        #Because the attribute was defined (empty) this piece of code works!
        if self.color == None:
            raise ValueError('Please define the color')
        return self.color
    
    
    
    #Create an attribute "Weight"
    #This attribute is added later on
    def setWeight(self, Weight):
        self.Weight = Weight
    
    
    #to get the error, it is not looking at the attribute error, but at the attribute existence
    def getWeight(self):
        if hasattr(self, "Weight"):
            return self.Weight
        else:
            raise Exception('Set Weight first')
            
    
    #Similar to Weight we will add a new Attribute later on
    #The attribute Job
    def setJob(self, job):
        self.job = job
    
    
    #to get the error, it is looking at the attribute value, but instead give a standar error it looks for the exception in case of it didn't exist
    def getJob(self):
        try:
            return self.job
        except:
            raise ValueError('You must define a Job / Occupation first')
            
    
    