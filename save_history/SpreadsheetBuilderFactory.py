from breakpoint.BreakPointSheetBuilder import BreakPointSheetBuilder
from registers.RegistersSheetBuilder import RegistersSheetBuilder
from save_history.SpreadsheetBuilder import SpreadsheetBuilder

sheetBuilders = {}

def getSheetBuilder(sheet) -> SpreadsheetBuilder:
    if len(sheetBuilders) == 0:
        sheetBuilders["breakpoint"] = BreakPointSheetBuilder()
        sheetBuilders["registers"] = RegistersSheetBuilder()
    return sheetBuilders[sheet]