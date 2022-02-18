from DMXEnttecPro import Controller

def calculateTransition(beginValue, endValue, decimalDistance):
    difference = endValue-beginValue
    valueDistance = decimalDistance*difference
    rawChannelValue = beginValue + valueDistance

    #round to nearest int
    returnValue = round(rawChannelValue)
    return returnValue

def dmxInit(controllerPort):
    isDummy = True

    if isDummy:
        pass
    else:
        dmxController = Controller(controllerPort)
        return dmxController 

def dmxUpdate(dmxController, dmxData):
    isDummy = True

    if isDummy:
        pass
    else:
        for iterator in range(len(dmxData)):
            dmxController.setChannel(iterator+1, dmxData[iterator]) 
            dmxController.submit()