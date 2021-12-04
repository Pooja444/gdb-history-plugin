import xlsxwriter
from datetime import datetime

class SpreadsheetGenerator:
    def __init__(self) -> None:
        pass

    def createSpreadsheet(self) -> None:
        self.workbook = xlsxwriter.Workbook(f"gdb_history_{datetime.now()}.xlsx")

    def saveSpreadsheet(self) -> None:
        self.workbook.close()
