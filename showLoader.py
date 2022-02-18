from Scene import *
import json, os, sys, dmxHandler
#clear screen function

def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def loadShow(filepath, dmxInterfacePort): 
    with open(filepath, 'r') as jsonFile:
        jsonString = jsonFile.read()
        jsonData = json.loads(jsonString)
    
    #load data into scenes
    scenes = []
    for sceneIndex in range(len(jsonData)):
        currentSceneName = jsonData[sceneIndex][0]
        currentFadeTime = jsonData[sceneIndex][1]
        currentDMX = jsonData[sceneIndex][2:] 

        currentScene = Scene(currentSceneName, currentFadeTime, currentDMX)
        scenes.append(currentScene)

    #Presentation mode
    clearScreen()

    #Print the names of the scenes
    def printScenes(sceneList, currentScene):
        for sceneIndex in range(len(scenes)):
            if sceneIndex == currentScene:
                print("*" + str(sceneIndex) + ") " + sceneList[sceneIndex].sceneName)
            else:
                print(str(sceneIndex) + ") " + sceneList[sceneIndex].sceneName)
    
    def redrawShowMenu(sceneList, currentScene):
        clearScreen()
        printScenes(sceneList, currentScene)
    
    quitRequested = False
    currentScene = 0 

    #Initialize DMX Device
    dmxController = dmxHandler.dmxInit(dmxInterfacePort)

    #Main Loop
    while quitRequested == False:
        redrawShowMenu(scenes, currentScene)
        dmxHandler.dmxUpdate(dmxController, scenes[currentScene].dmxData)
        rawCommand = input("What scene should be played next? (# or \"n\" to play next, \"p\" to play previous): ")

        commandNumber = -1
        try:
            commandNumber = int(rawCommand)
        except ValueError:
            #reset command number
            commandNumber = -1

            #check for textual commands
            if rawCommand == 'quit':
                sys.exit()
            elif rawCommand == 'clear':
                clearScreen()
                printScenes(scenes, currentScene)
            elif rawCommand == 'p':
                if currentScene > 0:
                    currentScene = currentScene - 1
                else:
                    print("cannot move to previous cue")
            elif rawCommand == 'n':
                if currentScene < (len(scenes) - 1):
                    currentScene = currentScene + 1
                else:
                    print("cannot move to next cue")
                pass
            else:
                print("invalid command")
        if commandNumber != -1:
            if commandNumber in range(len(scenes)):
                currentScene=commandNumber