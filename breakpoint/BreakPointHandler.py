import gdb
from save_history.SpreadsheetHandlerFactory import getSpreadsheetHandler
from save_history.SpreadsheetBuilderFactory import getSheetBuilder
from registers.RegistersHandlerFactory import getRegistersHandler
from util.utils import getSubstring


class BreakPointHandler:
    def __init__(self) -> None:
        self.breakpointsHit = 0
        self.buildSheet(getSpreadsheetHandler().workbook)
        self.registerAllHandlers()
        pass

    def buildSheet(self, workbook):
        breakpointSheetBuilder = getSheetBuilder("breakpoint")
        self.worksheet = breakpointSheetBuilder.createSheet(workbook)
        breakpointSheetBuilder.createSheetHeaders(self.worksheet)

    def registerAllHandlers(self):
        gdb.events.exited.connect(self.exit_handler)
        gdb.events.stop.connect(self.breakpoint_handler)

    def exit_handler(self, event):
        print("event type: exit")
        if hasattr(event, "exit_code"):
            print("exit code: %d" % (event.exit_code))
        else:
            print("exit code not available")

    def breakpoint_handler(self, event):
        if hasattr(event, "breakpoints"):
            breakpoint = event.breakpoints[0]
            self.breakpointNumber = breakpoint.number

            # TODO: For call instructions, we can try to find function name using info symbol <addr>
            breakpointValues = [
                self.breakpointNumber, 
                getSubstring("=", gdb.execute("p/x $rip", False, True)),
                breakpoint.location,
                getSubstring(":", gdb.execute("x/i $rip", False, True)),
                "\n".join([getSubstring(":", instruction) for instruction in gdb.execute("x/5i $rip", False, True).split("\n")][1:]),
                gdb.execute("bt", False, True)
            ]

            for columnIndex, breakpointValue in enumerate(breakpointValues):
                self.worksheet.write(self.breakpointsHit + 1, columnIndex, breakpointValue)

            getRegistersHandler().fillRegisters(self)
            self.breakpointsHit += 1
