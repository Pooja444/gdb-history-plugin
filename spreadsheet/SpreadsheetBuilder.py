from abc import ABC, abstractmethod
from xlsxwriter import worksheet

class SpreadsheetBuilder:

    def buildSheet(self, workbook, shoudCreateHeaders) -> worksheet:
        worksheet = self.createSheet(workbook)
        if shoudCreateHeaders:
            numberOfColumns = self.createSheetHeaders(worksheet)
            self.styleColumns(worksheet, numberOfColumns)
        return worksheet

    @abstractmethod
    def createSheet(self, workbook) -> worksheet:
        pass

    @abstractmethod
    def createSheetHeaders(self, worksheet) -> int:
        pass

    def styleColumns(self, worksheet, numberOfColumns):
        print(f"Styling {numberOfColumns} columns...")
        print(worksheet.set_column(0, numberOfColumns - 1, 20))