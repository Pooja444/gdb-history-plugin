import gdb

class BreakPointHandler:
    
    def __init__(self) -> None:
        self.registerAllHandlers()
        pass

    def registerAllHandlers(self):
        gdb.events.exited.connect(self.exit_handler)
        gdb.events.stop.connect(self.breakpoint_handler)

    def exit_handler (self, event):
        print ("event type: exit")
        if hasattr (event, 'exit_code'):
            print ("exit code: %d" % (event.exit_code))
        else:
            print ("exit code not available")
    
    def breakpoint_handler(self, event):
        if hasattr(event, "breakpoints"):
            breakpoint = event.breakpoints[0]
            print("OMG a breakpoint has been detected!")
            print(breakpoint.is_valid())
            print(breakpoint.number)
            print(breakpoint.location)
            registers = [register.split() for register in gdb.execute("info registers", False, True).split("\n")]
            print(registers)