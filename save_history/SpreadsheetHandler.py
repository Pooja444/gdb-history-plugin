import xlsxwriter
from datetime import datetime

class SpreadsheetHandler:
    def __init__(self) -> None:
        pass

    def createSpreadsheet(self) -> str:
        workbookName = f"data/gdb_history_{datetime.now()}.xlsx"
        self.workbook = xlsxwriter.Workbook(workbookName)
        return workbookName

    def saveSpreadsheet(self) -> None:
        self.workbook.close()
