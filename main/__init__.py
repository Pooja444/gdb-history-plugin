import atexit

from save_history.SpreadsheetHandlerFactory import getSpreadsheetHandler
from breakpoint.BreakPointHandlerFactory import getBreakpointHandler
from registers.RegistersHandlerFactory import getRegistersHandler

print("Starting custom GDB plugin...")
print("The GDB history spreadsheet will be generated and stored in your home directory")

spreadsheetHandler = getSpreadsheetHandler()

spreadsheetName = spreadsheetHandler.createSpreadsheet()
getBreakpointHandler()
getRegistersHandler()

def exit_handler():
    print(f"Saving spreadsheet at {spreadsheetName}...")
    spreadsheetHandler.saveSpreadsheet()

atexit.register(exit_handler)