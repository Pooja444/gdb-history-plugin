import xlsxwriter
from datetime import datetime

class SpreadsheetHandler:
    def __init__(self) -> None:
        pass

    def createSpreadsheet(self) -> None:
        self.workbook = xlsxwriter.Workbook(f"data/gdb_history_{datetime.now()}.xlsx")

    def saveSpreadsheet(self) -> None:
        self.workbook.close()
