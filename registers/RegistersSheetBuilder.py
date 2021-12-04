from spreadsheet.SpreadsheetBuilder import SpreadsheetBuilder
from xlsxwriter import worksheet
import gdb

class RegistersSheetBuilder(SpreadsheetBuilder):

    def createSheet(self, workbook) -> worksheet:
        print("Creating registers worksheet...")
        return workbook.add_worksheet("Registers")
    
    def createSheetHeaders(self, worksheet) -> int:
        worksheet.write(0, 0, "Breakpoint number")
        
        gdbRegisters = [register.split() for register in gdb.execute("info registers", False, True).split("\n")][:-1]
        registers = []

        for gdbRegister in gdbRegisters:
            registers.append(gdbRegister[0])

        headers = []
        
        for register in registers:
            headers.append(f"Value at {register}")
            headers.append(f"Resolved value at {register}")
        
        for columnNumber, header in enumerate(headers):
            worksheet.write(0, columnNumber + 1, header)
        
        self.styleColumns(worksheet, len(headers) + 1)
        
        return len(headers) + 1