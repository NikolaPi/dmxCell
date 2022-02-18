from DMXEnttecPro import Controller

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