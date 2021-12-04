from registers.ResgiterHandler import RegistersHandler

registersHandler = None

def getRegistersHandler() -> RegistersHandler:
    global registersHandler
    if registersHandler is None:
        registersHandler = RegistersHandler()
    return registersHandler