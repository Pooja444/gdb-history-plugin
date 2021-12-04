from save_history.SpreadsheetHandler import SpreadsheetHandler

spreadsheetHandler = None

def getSpreadsheetHandler() -> SpreadsheetHandler:
    global spreadsheetHandler
    if spreadsheetHandler is None:
        spreadsheetHandler = SpreadsheetHandler()
    return spreadsheetHandler