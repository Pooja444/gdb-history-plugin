from save_history.SpreadsheetHandlerFactory import getSpreadsheetHandler
from save_history.SpreadsheetBuilderFactory import getSheetBuilder

class RegistersHandler:
    def __init__(self) -> None:
        self.buildSheet(getSpreadsheetHandler().workbook)
        pass

    def buildSheet(self, workbook):
        registerSheetBuilder = getSheetBuilder("registers")
        worksheet = registerSheetBuilder.createSheet(workbook)
        registerSheetBuilder.createSheetHeaders(worksheet)