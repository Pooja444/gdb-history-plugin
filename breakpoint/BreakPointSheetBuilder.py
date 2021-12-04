from spreadsheet.SpreadsheetBuilder import SpreadsheetBuilder
from xlsxwriter import worksheet

class BreakPointSheetBuilder(SpreadsheetBuilder):

    def createSheet(self, workbook) -> worksheet:
        return workbook.add_worksheet("Breakpoints")
    
    def createSheetHeaders(self, worksheet) -> int:
        headers = [
            "Breakpoint Number",
            "Address at Breakpoint",
            "Trigger command",
            "Instruction at breakpoint",
            "Next 4 instructions",
            "Backtrace",
            "Link to register states"
        ]
        for columnNumber, header in enumerate(headers):
            worksheet.write(0, columnNumber, header)
        
        return len(headers)