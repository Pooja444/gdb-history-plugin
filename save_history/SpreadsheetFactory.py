from save_history.SpreadsheetGenerator import SpreadsheetGenerator

spreadsheetGenerator = None

def getSpreadsheetGenerator() -> SpreadsheetGenerator:
    global spreadsheetGenerator
    if spreadsheetGenerator is None:
        spreadsheetGenerator = SpreadsheetGenerator()
    return spreadsheetGenerator