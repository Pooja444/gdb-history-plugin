from save_history.SpreadsheetBuilder import SpreadsheetBuilder
from xlsxwriter import worksheet

class RegistersSheetBuilder(SpreadsheetBuilder):

    def createSheet(self, workbook) -> worksheet:
        return workbook.add_worksheet("Registers")
    
    def createSheetHeaders(self, worksheet):
        registers = ["RAX", "RBX", "RCX", "RDX", "RDI", "RSI", "RSP", "RBP", "RIP"]
        headers = []
        
        for register in registers:
            headers.append(f"Value at {register}")
            headers.append(f"Resolved value at {register}")
        
        for columnNumber, header in enumerate(headers):
            worksheet.write(0, columnNumber, header)