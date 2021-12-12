# GDB History plugin project

## Need for this plugin

This project aims to store the entire breakpoints history that was generated during a GDB session. Usually, during a GDB session, we hit a number of breakpoints. Every breakpoint allows us to see the current state of the program, e.g. current value of registers, stack information, information related to current and next instructions, etc. While this is useful when analysing a program, the downside is that we can only see one (the current) program state at a time. That's when this plugin comes into picture. After the GDB session ends, all the breakpoints and the program states at these breakpoints will be dumped in a spreadsheet so that all the states could be looked at, at once. This will make analysing complicated programs easier when we need to set a number of breakpoints. In one file, all the data generated at every breakpoint can be seen and the program can be easily reversed.

Also, this project is part of a course curriculum: CSE598 (Applied Program Analysis and Debugging) at Arizona State University.

## What exactly does the spreadsheet store?

The spreadsheet will have two sheets

* Breakpoints - Basic information for every breakpoint, as follows:
    * Breakpoint number - The number of the breakpoint that was registered
    * Breakpoint address - The address at which the breakpoint was hit
    * Trigger command - The command that was used to trigger the breakpoint (e.g. `b *main+100` or `break 0x1875`)
    * Instruction at breakpoint - The instruction that will be executed on the breakpoint
    * Next 4 instructions - The next 4 instructions that will be executed after this breakpoint
    * Backtrace - The curren backtrace
    * Link to register states - A link to all the register states at this breakpoint, present on the next sheet, for easy reference

* Registers - When the first breakpoint hits, this plugin extracts all the registers present on the current architecture by running a GDB `info registers` command, making the plugin architecture indepenent. For every extracted register, whenever a breakpoint is hit, below two values will be stored:
    * Value at the register
    * If the value at the register can be resolved (i.e. potential memory address), then the resolved value will also be stored



## How does the plugin work?

The plugin essentially follows the below algorithm - 

1. As soon as the GDB sessin begins, a spreadsheet is created
1. An exit handler is registered that will store the spreadsheet as soon as the session ends. Note that this is a python exit handler and not a GDB exit handler. This ensures that even if the GDB session didn't exit with a valid exit code, or just abruptly ended, the session information isn't lost and the spreadsheet is still saved.
1. A breakpoint handler is invoked so that -
    * A "breakpoints" sheet is created in the spreadsheet, filled will appropriate columns
    * A "breakpoint event handler" is registered using Python's gdb library
    * An "exit event handler" is registered using Python's gdb library
1. A registers handler is invoked so that - 
    * A "registers" sheet is created in the spreadsheet, to which columns would be added when the first breakpoint is hit, as mentioned above
1. Whenever a breakpoint is hit, a new row is created in the breakpoints sheet and it is filled using gdb commands, e.g. `x/i $rip` to get current instruction
1. The breakpoint event handler invokes a fillRegisters method in the registers handler, to fill all the registers' values present at that point
1. As soon as the session ends, the spreadsheet is stored inside a "history" directory, at the current path

## How to install this plugin?

* Make sure you have Python installed as the plugin runs on Python
* Run ./setup.sh and you're good to go!

This project will have more improvements in the future. Please reach out for any bug reports.