from reader import *

class Log:
    
    logData = []
        
    def logger(stamp):
        Log.logData.append(stamp)
        
        
    def printLog():
        for i in Log.logData:
            print(i)
        