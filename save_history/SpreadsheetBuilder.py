from abc import ABC, abstractmethod
from xlsxwriter import worksheet

class SpreadsheetBuilder:

    @abstractmethod
    def createSheet(self, workbook) -> worksheet:
        pass

    @abstractmethod
    def createSheetHeaders(self, worksheet):
        pass