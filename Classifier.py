__author__ = 'Sourabh Khasbag'
import userClass as nf
import csv

#the primary keywords that the program identifies in the file. These keywords were identified after careful study of the dataset
targetwords = ['sporting', 'nfl', 'nba', 'negative', 'overdraft', 'brewery', 'wine', 'membership', 'library', 'late',
               'concert', 'mathematics', 'science', 'star', 'gym', 'paycheck', 'coffee', 'movie', 'student',
               'education', 'course', 'lessons', 'pet', 'book', 'music', 'art', 'restaurant', 'museum', 'loan', 'gym',
               'groceries', 'bar', 'club', 'divorce', 'wedding']
#the final attributes of the user to be targeted
Headinglist = ['UID', 'Income', 'Expense', 'Student', 'Married', 'Divorced', 'Pets', 'Intellectual', 'Geeky',
               'ArtLover', 'CoffeeLover', 'PartyPerson', 'Tardy', 'HealthFreak', 'Bibulious', 'MusicLover']


def startclassifer():
    '''
    function which creates the 'User' object and passes the read properties and the cost to the user object
    :return: userList-A list containing user objects, userDict- a Dictionary containing user objects (key-UID,value-User object)
    '''
    userdict={}
    path = "F:/Programming/intuit challenge/rit-challenge-master/transaction-data/user-"
    exten = ".csv"
    id = 0
    flag=1
    userList=[]
    while id is not 100:                        #Continues till all 100 files have been parsed
        expense=0
        income=0
        filePath = path + str(id) + exten

        with open(filePath) as file:
            file.readline()
            for line in file:
                wlist = line.split(",")
                if flag==1:                     #if it is a new user(create User object and pass UID)
                    uid=int(wlist[0])
                    user=nf.User(uid,id)
                    flag=0
                store=wlist[2]
                amt=float(wlist[3])
                if amt>0:
                    income = + amt
                elif amt<0:
                    amt=amt*-1
                    expense= + amt
                vendorName=store.split()
                for word in vendorName:
                    word=word.lower()
                    if word in targetwords:
                        user.updatemap(word,amt)
        userList.append(user)
        userdict[str(uid)]=user
        id=id+1
        user.setIncomeExpense(income,expense)
        flag=1
    return userList,userdict

def fileinitiator():
    '''
    Initiates the file and writes the header coloums to the file
    :return: None
    '''
    path = "F:/Programming/intuit challenge/rit-challenge-master/ans/Features"
    exten = ".csv"
    with open(path+exten,'w') as csvfile:
        featurewriter = csv.writer(csvfile)
        featurewriter.writerow(Headinglist)

def findUsers(userdict,uid1,uid2):
    '''

    :param userdict: Dictionary which contains keys as UID and values as User class objects
    :param uid1: the first person's user id
    :param uid2: Second person's user id
    :return:
    '''
    if uid1 not in userdict:
        print("First person not  found! Please try again")
        return None,None
    if uid2 not in userdict:
        print("Second person not found! Please try again")
        return None,None
    user1=userdict[uid1]
    user2=userdict[uid2]
    return user1,user2

def main():
    userList,userDict=startclassifer()
    fileinitiator()
    for user in userList:
        user.inference()
        user.updatefile()
    print("Done!")
    user1=None
    user2=None
    while(user1==None and user2==None):
        uid1=input("Enter the UID of the first person: ").strip()
        uid2=input("Enter the UID of the Second person: ").strip()
        user1,user2=findUsers(userDict,uid1,uid2)
    print("Score:"+str(user1.findCompatiblity(user2)))





if __name__ == '__main__':
    main()