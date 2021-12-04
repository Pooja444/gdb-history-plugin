import xlsxwriter
import os

from datetime import datetime

class SpreadsheetHandler:
    def __init__(self) -> None:
        pass

    def createSpreadsheet(self) -> str:
        if not os.path.isdir("history"):
            os.mkdir("history")
        workbookName = f"history/gdb_history_{str(datetime.now()).replace(' ', '_')}.xlsx"
        self.workbook = xlsxwriter.Workbook(workbookName)
        return workbookName

    def saveSpreadsheet(self) -> None:
        self.workbook.close()
