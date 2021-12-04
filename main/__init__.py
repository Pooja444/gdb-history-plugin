from breakpoint.BreakPointHandler import BreakPointHandler
from save_history.SpreadsheetFactory import getSpreadsheetGenerator
from save_history.SpreadsheetGenerator import SpreadsheetGenerator

print("Starting custom GDB plugin...")
print("The GDB history spreadsheet will be generated and stored in your home directory")

spreadsheetGenerator = getSpreadsheetGenerator()
spreadsheetGenerator.createSpreadsheet()
BreakPointHandler()
spreadsheetGenerator.saveSpreadsheet()