__author__ = 'Sourabh Khasbag'

import csv
class Attributes:
    """
    This class holds the Attributes of a user. Each attribute assigned a slot.
    """
    __slots__=('Food','MusicLover','Married','Sports','Income','Student','Bibulious','Pets','HealthFreak','PartyPerson','Intellectual','Divorced','ArtLover','Tardy','Geeky','CarOwner','MusicLover','CoffeeLover','Expense')


    def __init__(self):
        self.Student=0
        self.Pets=0
        self.HealthFreak=0
        self.PartyPerson=0
        self.Intellectual=0
        self.Divorced=0
        self.ArtLover=0
        self.Tardy=0
        self.Geeky=0
        self.CoffeeLover=0
        self.Bibulious=0
        self.Income=0
        self.Expense=0
        self.Sports=0
        self.MusicLover=0
        self.Married=0



    def quantifyfeatures(self):
        '''
        This quantifies certain properties of the extracted features. Th main aim is to find the percentage expense of a particular feature
        :return:
        '''
        self.Pets=(self.Pets/self.Expense)*100
        self.Tardy=(self.Tardy/self.Expense)*100
        self.HealthFreak=(self.HealthFreak/self.Expense)*100
        self.Bibulious=(self.Bibulious/self.Expense)*100
        self.PartyPerson=(self.PartyPerson/self.Expense)*100
        self.Intellectual=(self.Intellectual/self.Expense)*100
        self.ArtLover=(self.ArtLover/self.Expense)*100
        self.Geeky=(self.Geeky/self.Expense)*100
        self.Sports=(self.Sports/self.Expense)*100
        self.MusicLover=(self.MusicLover/self.Expense)*100
        self.CoffeeLover=(self.CoffeeLover/self.Expense)*100


    def filewriter(self,id):
        '''
        Writes the output to the file
        :param id: The id of the user whose attributes are to be written to the file
        :return:
        '''
        self.quantifyfeatures()
        path = "F:/Programming/intuit challenge/rit-challenge-master/ans/Features"
        exten = ".csv"
        counter = 0
        with open(path+exten,'a') as csvfile:
            featurewriter=csv.writer(csvfile)
            featurewriter.writerow([id,self.Income,self.Expense,self.Student,self.Married,self.Divorced,self.Pets,self.Intellectual,self.Geeky,self.ArtLover,self.CoffeeLover,self.PartyPerson,self.Tardy,self.HealthFreak,self.Bibulious,self.MusicLover,self.Sports])



class User:
    __slots__=('id','qualities','income','expense','featuremap','priority')

    def __init__(self,id,number):
        self.id=id
        self.qualities=Attributes()
        self.featuremap={}
        self.priority={}
        self.setpriorities()


    def setpriorities(self):
        self.priority["Maximum"]=['Income','Expense','Divorced',"Student",'Married']
        self.priority["Medium"]=[]
        self.priority["Lowest"]=['PartyPerson','Pets','Tardy','HealthFreak','Bibulious','Intellectual','ArtLover','Geeky','Sports','MusicLover','CoffeeLover']



    def updatemap(self,keyword,value):
        flag=0
        extra=[]
        if keyword in self.featuremap:
            cost,counter=self.featuremap[keyword]
            cost=cost+value
            counter=counter+1
            self.featuremap[keyword]=(cost,counter)
        else:
            self.featuremap[keyword]=(value,1)


    def findCompatiblity(self, partner):
        '''
        Finds the compatibility score with another user
        :param partner: The user with whom compatibility score is to be measured
        :return: compatibility Score which is calculated
        '''
        maxweight=12
        mediumweight=4
        lowestweight=1
        maxamt=0
        medamt=0
        minamt=0
        maxscale=0
        midscale=0
        minscale=0
        maximumPriority=self.priority["Maximum"]
        for feature in maximumPriority:
            partnerValue=partner.get(feature)
            uservalue=self.get(feature)
            maxscale=maxscale+max(partnerValue,uservalue)
            maxamt=maxamt+abs((partnerValue-uservalue))
        medPriority=self.priority["Medium"]
        for feature in medPriority:
            partnerValue=partner.get(feature)
            uservalue=self.get(feature)
            midscale=midscale+max(partnerValue,uservalue)
            medamt=medamt+abs((partnerValue-uservalue))
        minPriority=self.priority["Lowest"]
        for feature in minPriority:
            partnerValue=partner.get(feature)
            uservalue=self.get(feature)
            minscale=minscale+max(partnerValue,uservalue)
            minamt=minamt+abs((partnerValue-uservalue))
        totalscore=maxamt*maxweight+medamt*mediumweight+minamt*lowestweight
        totalscale=maxscale*maxweight+midscale*mediumweight+minscale*lowestweight
        compatiblityScore=1-(totalscore/totalscale)
        return compatiblityScore

    def get(self,attributeName):
        '''
        Getter method for all the features that have been extracted
        :param attributeName: Name of the attribute to be extracted
        :return: the specified Attribute variable
        '''
        if attributeName=="Income":
            return self.qualities.Income
        elif attributeName=="Expense":
            return self.qualities.Expense
        elif attributeName=="MusicLover":
            return self.qualities.MusicLover
        elif attributeName=="Tardy":
            return self.qualities.Tardy
        elif attributeName=="Student":
            return self.qualities.Student
        elif attributeName=="Divorced":
            return self.qualities.Divorced
        elif attributeName=="Geeky":
            return self.qualities.Geeky
        elif attributeName=="ArtLover":
            return self.qualities.ArtLover
        elif attributeName=="Intellectual":
            return self.qualities.Intellectual
        elif attributeName=="Bibulious":
            return self.qualities.Bibulious
        elif attributeName=="HealthFreak":
            return self.qualities.HealthFreak
        elif attributeName=="PartyPerson":
            return self.qualities.PartyPerson
        elif attributeName=="CoffeeLover":
            return self.qualities.CoffeeLover
        elif attributeName=="Sports":
            return self.qualities.Sports
        elif attributeName=="Pets":
            return self.qualities.Pets
        elif attributeName=='Married':
            return self.qualities.Married


    def setIncomeExpense(self,income,expense):
        '''
        Sets the Total income and the total expense of the user
        :param income: Total income of User
        :param expense: Total expense of User
        :return:
        '''
        self.income=income
        self.expense=expense


    def inference(self):
        '''
        Fucntion which derives the inference from the raw data.
        :return: None
        '''
        self.qualities.Income=self.income
        self.qualities.Expense=self.expense
        for key in self.featuremap:
            if key=="course" or key=='education':
                self.qualities.Student=1
            elif key=="book" :
                self.qualities.Intellectual=self.qualities.Intellectual+self.featuremap['book'][0]
            elif key=='museum':
                self.qualities.Intellectual=self.qualities.Intellectual+self.featuremap['museum'][0]
            elif key=='library':
                self.qualities.Intellectual=self.qualities.Intellectual+self.featuremap['library'][0]
            elif key=='pet' :
                self.qualities.Pets=self.qualities.Pets+self.featuremap['pet'][0]
            elif key=='gym':
                self.qualities.HealthFreak=self.qualities.HealthFreak+self.featuremap['gym'][0]
            elif key=='club':
                self.qualities.PartyPerson=self.qualities.PartyPerson+self.featuremap['club'][0]
            elif key=='divorce':
                self.qualities.Divorced=1
            elif key=='art':
                self.qualities.ArtLover=self.qualities.ArtLover+self.featuremap['art'][0]
            elif key=='late' in self.featuremap:
                self.qualities.Tardy=self.qualities.Tardy+self.featuremap['late'][0]
            elif key=='negative' in self.featuremap:
                self.qualities.Tardy=self.qualities.Tardy+self.featuremap['negative'][0]
            elif key=='overdraft' in self.featuremap:
                self.qualities.Tardy=self.qualities.Tardy+self.featuremap['overdraft'][0]
            elif key=='star':
                self.qualities.Geeky=self.qualities.Geeky+self.featuremap['star'][0]
            elif key=='thinkgeek':
                self.qualities.Geeky=self.qualities.Geeky+self.featuremap['thinkgeek'][0]
            elif key=='concert':
                self.qualities.MusicLover=self.qualities.MusicLover+self.featuremap['concert'][0]
            elif key=='music':
                self.qualities.MusicLover=self.qualities.MusicLover+self.featuremap['music'][0]
            elif key=="wine":
                self.qualities.Bibulious=self.qualities.Bibulious+self.featuremap['wine'][0]
            elif key=='brewery':
                self.qualities.Bibulious=self.qualities.Bibulious+self.featuremap['brewery'][0]
            elif key=='coffee':
                self.qualities.CoffeeLover=self.qualities.CoffeeLover+self.featuremap['coffee'][0]
            elif key=='married':
                self.qualities.Married=1
            elif key=='nba':
                self.qualities.Sports=self.qualities.Sports+self.featuremap['nba'][0]
            elif key=='nfl':
                self.qualities.Sports=self.qualities.Sports+self.featuremap['nfl'][0]
            elif key=='sporting':
                self.qualities.Sports=self.qualities.Sports+self.featuremap['sporting'][0]


    def updatefile(self):
        """
        Function to initiate the filewriter
        :return: None
        """
        self.qualities.filewriter(self.id)