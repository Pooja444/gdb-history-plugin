import atexit

from save_history.SpreadsheetHandlerFactory import getSpreadsheetHandler
from breakpoint.BreakPointHandler import BreakPointHandler
from registers.ResgiterHandler import RegistersHandler

print("Starting custom GDB plugin...")
print("The GDB history spreadsheet will be generated and stored in your home directory")

spreadsheetHandler = getSpreadsheetHandler()

spreadsheetHandler.createSpreadsheet()
BreakPointHandler()
RegistersHandler()

def exit_handler():
    print("Exiting...")
    spreadsheetHandler.saveSpreadsheet()

atexit.register(exit_handler)