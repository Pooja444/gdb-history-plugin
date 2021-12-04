from breakpoint.BreakPointHandler import BreakPointHandler

breakpointHandler = None

def getBreakpointHandler() -> BreakPointHandler:
    global breakpointHandler
    if breakpointHandler is None:
        breakpointHandler = BreakPointHandler()
    return breakpointHandler