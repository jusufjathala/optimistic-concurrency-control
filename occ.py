# Tugas Besar 2 IF3140 2021
# Kelas K-02
# Kelompok 8

import time

class Transaction:
    def __init__(self, txNum): #constructor
        self.txNum = txNum
        self.readWriteList = []
        self.startTS = time.time()
        self.validateTS = 0
        self.finishTS = 0
        
    def validate(self, txList, validateList):
        print( str("               "*(int(self.txNum)-1)) + "T" +str(self.txNum)+": validate")
        valid = True
        self.validateTS = time.time()
        if (validateList): #if validateList not empty
            validOne = True
            validTwo = True
            for tx in txList :
                if (tx.txNum!=self.txNum) and (tx.validateTS < self.validateTS):
                    #check condition 1
                    if tx.finishTS < self.startTS : 
                        validOne = True 
                    else :
                        validOne = False
                        
                    #check condition 2
                    if (self.startTS < tx.finishTS) and (tx.finishTS < self.validateTS) : 
                        for write in tx.readWriteList :
                            for read in self.readWriteList :
                                #check intersect
                                if (write[0]=="w" and read[0]=="r" and write[1]==read[1]) :    
                                    validTwo = False
                                    break
            if (validOne) or (validTwo):
                valid = True
            else :
                valid = False
                
        if (valid):
            validateList.append(self)
            self.finishTS = time.time()
            print (str("               "*(int(self.txNum)-1))+"Validation success")
        else :
            print (str("               "*(int(self.txNum)-1))+"Validation fail, transaction must rollback")
    

def isTxInMemory(txList, txNum):
    for tx in txList:
        if tx.txNum==txNum :
            return tx

            
def main():
    txList = []
    validateList = []
    filename = input("Input filename: ")
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        num = line[1]
        if not (isTxInMemory(txList, num)) :
            txList.append(Transaction(num))
        tx = isTxInMemory(txList,num)
        if (line[3]=="r"):
            print( str("               "*(int(num)-1)) + "T" +str(num)+": read " +str(line[5]) )
            tx.readWriteList.append(("r",line[5]))
        if (line[3]=="w"):
            print( str("               "*(int(num)-1)) + "T" +str(num)+": write " +str(line[5]) )
            tx.readWriteList.append(("w",line[5]))
        if (line[3]=="v"):
            tx.validate(txList, validateList)
            
    
if __name__ == '__main__':
    main()