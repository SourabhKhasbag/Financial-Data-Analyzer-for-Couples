'''
This program was used initially to study the data
'''
def keyfinder():
    '''
    Finds all the unique keys in the data
    :return:
    '''
    path = "F:/Programming/intuit challenge/rit-challenge-master/transaction-data/user-"
    exten = ".csv"
    id = 0
    counter = 0
    read = []
    linecounter = 0;
    while id is not 100:
        fpath = path + str(id) + exten
        with open(fpath) as file:
            file.readline()
            for line in file:
                cline = line.strip()
                wlist = line.split(",")
                if wlist[2] not in read:
                    read.append(wlist[2])
        id = id + 1
    return read



def similaritygrouping():
    '''
    Groups similar words together. Eg types of restarants , Types of books ,etc
    :return: Dictionary mapping target words to the similar word list
    '''
    wordmap={}
    keys1=keys
    targetwords=['sprouts','ticket','student','lessons','education','course','book','movies','restaurant','babies','baby','uber','transportation','art','museum']
    for phrase in keys1:
        cphrase=phrase.strip()
        wlist=cphrase.split()
        for word in wlist:
            word=word.lower()
            if word in targetwords:
                if word not in wordmap:
                    wordmap[word]=[phrase]
                else:
                    plist=wordmap[word]
                    plist.append(phrase)
                    wordmap[word]=plist
    return wordmap,targetwords




def preprocessor():
    keys=keyfinder()
    wordmap,targets=similaritygrouping(keys)


if __name__ == '__main__':
    preprocessor()
