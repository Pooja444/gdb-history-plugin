import gdb

from save_history.SpreadsheetHandlerFactory import getSpreadsheetHandler
from save_history.SpreadsheetBuilderFactory import getSheetBuilder
from util.utils import getSubstring

class RegistersHandler:
    def __init__(self) -> None:
        self.buildSheet(getSpreadsheetHandler().workbook)
        pass

    def buildSheet(self, workbook):
        self.worksheet = getSheetBuilder("registers").createSheet(workbook)
    
    def fillRegisters(self, breakpoint):
        if breakpoint.breakpointsHit == 0:
            getSheetBuilder("registers").createSheetHeaders(self.worksheet)
        
        self.worksheet.write(breakpoint.breakpointsHit + 1, 0, breakpoint.breakpointNumber)

        gdbRegisters = [register.split() for register in gdb.execute("info registers", False, True).split("\n")][:-1]
        for columnIndex, gdbRegister in enumerate(gdbRegisters):
            value = gdbRegister[1]
            try:
                resolvedValue = getSubstring(":", gdb.execute(f"x/gx ${gdbRegister[0]}", False, True))
            except gdb.MemoryError:
                resolvedValue = f"Cannot resolve address {value}"
            self.worksheet.write(breakpoint.breakpointsHit + 1, columnIndex * 2 + 1, value)
            self.worksheet.write(breakpoint.breakpointsHit + 1, columnIndex * 2 + 2, resolvedValue)