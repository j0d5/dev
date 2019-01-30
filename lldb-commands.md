# LLDB Debugging Commands

- `po [UIWindow.keyWindow recursiveDescription]`
- `po [UIViewController _printHierarchy]`
- `po [UIView _autolayoutTrace]`
- `po [_UIViewLayoutFeedbackLoopDebugger layoutFeedbackLoopDebugger]`

```
// llbd in Swift context
expr -l objc++ -O -- [UIWindow.keyWindow recursiveDescription]
```

## .lldbinit

`command alias alt expr -l objc++ -O -- [[UIWindow keyWindow] _autolayoutTrace]`

## Chisel
|Command          |Description     |iOS    |OS X   |
|-----------------|----------------|-------|-------|
|pviews           |Print the recursive view description for the key window.|Yes|Yes|
|pvc              |Print the recursive view controller description for the key window.|Yes|No|
|visualize        |Open a `UIImage`, `CGImageRef`, `UIView`, `CALayer`, `NSData` (of an image), `UIColor`, `CIColor`, or `CGColorRef` in Preview.app on your Mac.|Yes|No|
|fv               |Find a view in the hierarchy whose class name matches the provided regex.|Yes|No|
|fvc              |Find a view controller in the hierarchy whose class name matches the provided regex.|Yes|No|
|show/hide        |Show or hide the given view or layer. You don't even have to continue the process to see the changes!|Yes|Yes|
|mask/unmask      |Overlay a view or layer with a transparent rectangle to visualize where it is.|Yes|No|
|border/unborder  |Add a border to a view or layer to visualize where it is.|Yes|Yes|
|caflush          |Flush the render server (equivalent to a "repaint" if no animations are in-flight).|Yes|Yes|
|bmessage         |Set a symbolic breakpoint on the method of a class or the method of an instance without worrying which class in the hierarchy actually implements the method.|Yes|Yes|
|wivar            |Set a watchpoint on an instance variable of an object.|Yes|Yes|
|presponder       |Print the responder chain starting from the given object.|Yes|Yes|

### Examples for `findinstances`

- `findinstances UIView subviews.@count > 100`
- `findinstances NSArray @count > 100`
- `findinstances UIScrollViewDelegate`
- `findinstances UIView window == nil || hidden == true || alpha == 0 || layer.bounds.#size.width == 0`

## clang

Show all enabled clang checkers:
`clang -cc1 -analyzer-checker-help`


## All Commands

- apropos           -- List debugger commands related to a word or subject.
- breakpoint        -- Commands for operating on breakpoints (see 'help b' for
                       shorthand.)
- bugreport         -- Commands for creating domain-specific bug reports.
- command           -- Commands for managing custom LLDB commands.
- disassemble       -- Disassemble specified instructions in the current
                       target.  Defaults to the current function for the
                       current thread and stack frame.
- expression        -- Evaluate an expression on the current thread.  Displays
                       any returned value with LLDB's default formatting.
- frame             -- Commands for selecting and examing the current thread's
                       stack frames.
- gdb-remote        -- Connect to a process via remote GDB server.  If no host
                       is specifed, localhost is assumed.
- gui               -- Switch into the curses based GUI mode.
- help              -- Show a list of all debugger commands, or give details
                       about a specific command.
- kdp-remote        -- Connect to a process via remote KDP server.  If no UDP
                       port is specified, port 41139 is assumed.
- language          -- Commands specific to a source language.
- log               -- Commands controlling LLDB internal logging.
- memory            -- Commands for operating on memory in the current target
                       process.
- platform          -- Commands to manage and create platforms.
- plugin            -- Commands for managing LLDB plugins.
- process           -- Commands for interacting with processes on the current
                       platform.
- quit              -- Quit the LLDB debugger.
- register          -- Commands to access registers for the current thread and
                       stack frame.
- script            -- Invoke the script interpreter with provided code and
                       display any results.  Start the interactive interpreter
                       if no code is supplied.
- settings          -- Commands for managing LLDB settings.
- source            -- Commands for examining source code described by debug
                       information for the current target process.
- statistics        -- Print statistics about a debugging session
- target            -- Commands for operating on debugger targets.
- thread            -- Commands for operating on one or more threads in the
                       current process.
- type              -- Commands for operating on the type system.
- version           -- Show the LLDB debugger version.
- watchpoint        -- Commands for operating on watchpoints.

Current command abbreviations (type 'help command alias' for more info):
  add-dsym  -- Add a debug symbol file to one of the target's current modules
               by specifying a path to a debug symbols file, or using the
               options to specify a module to download symbols for.
  attach    -- Attach to process by ID or name.
  b         -- Set a breakpoint using one of several shorthand formats.
  bt        -- Show the current thread's call stack.  Any numeric argument
               displays at most that many frames.  The argument 'all' displays
               all threads.
  c         -- Continue execution of all threads in the current process.
  call      -- Evaluate an expression on the current thread.  Displays any
               returned value with LLDB's default formatting.
  continue  -- Continue execution of all threads in the current process.
  detach    -- Detach from the current target process.
  di        -- Disassemble specified instructions in the current target.
               Defaults to the current function for the current thread and
               stack frame.
  dis       -- Disassemble specified instructions in the current target.
               Defaults to the current function for the current thread and
               stack frame.
  display   -- Evaluate an expression at every stop (see 'help target
               stop-hook'.)
  down      -- Select a newer stack frame.  Defaults to moving one frame, a
               numeric argument can specify an arbitrary number.
  env       -- Shorthand for viewing and setting environment variables.
  exit      -- Quit the LLDB debugger.
  f         -- Select the current stack frame by index from within the current
               thread (see 'thread backtrace'.)
  file      -- Create a target using the argument as the main executable.
  finish    -- Finish executing the current stack frame and stop after
               returning.  Defaults to current thread unless specified.
  image     -- Commands for accessing information for one or more target
               modules.
  j         -- Set the program counter to a new address.
  jump      -- Set the program counter to a new address.
  kill      -- Terminate the current target process.
  l         -- List relevant source code using one of several shorthand formats.
  list      -- List relevant source code using one of several shorthand formats.
  n         -- Source level single step, stepping over calls.  Defaults to
               current thread unless specified.
  next      -- Source level single step, stepping over calls.  Defaults to
               current thread unless specified.
  nexti     -- Instruction level single step, stepping over calls.  Defaults to
               current thread unless specified.
  ni        -- Instruction level single step, stepping over calls.  Defaults to
               current thread unless specified.
  p         -- Evaluate an expression on the current thread.  Displays any
               returned value with LLDB's default formatting.
  parray    -- Evaluate an expression on the current thread.  Displays any
               returned value with LLDB's default formatting.
  po        -- Evaluate an expression on the current thread.  Displays any
               returned value with formatting controlled by the type's author.
  poarray   -- Evaluate an expression on the current thread.  Displays any
               returned value with LLDB's default formatting.
  poc       -- Evaluate an expression on the current thread.  Displays any
               returned value with LLDB's default formatting.
  print     -- Evaluate an expression on the current thread.  Displays any
               returned value with LLDB's default formatting.
  q         -- Quit the LLDB debugger.
  r         -- Launch the executable in the debugger.
  rbreak    -- Sets a breakpoint or set of breakpoints in the executable.
  repl      -- Evaluate an expression on the current thread.  Displays any
               returned value with LLDB's default formatting.
  run       -- Launch the executable in the debugger.
  s         -- Source level single step, stepping into calls.  Defaults to
               current thread unless specified.
  si        -- Instruction level single step, stepping into calls.  Defaults to
               current thread unless specified.
  sif       -- Step through the current block, stopping if you step directly
               into a function whose name matches the TargetFunctionName.
  step      -- Source level single step, stepping into calls.  Defaults to
               current thread unless specified.
  stepi     -- Instruction level single step, stepping into calls.  Defaults to
               current thread unless specified.
  t         -- Change the currently selected thread.
  tbreak    -- Set a one-shot breakpoint using one of several shorthand
               formats.
  undisplay -- Stop displaying expression at every stop (specified by stop-hook
               index.)
  up        -- Select an older stack frame.  Defaults to moving one frame, a
               numeric argument can specify an arbitrary number.
  x         -- Read from the memory of the current target process.
Current user-defined commands:
  alamborder    -- Put a border around views with an ambiguous layout
  alamunborder  -- Removes the border around views with an ambiguous layout
  bdisable      -- Disable a set of breakpoints for a regular expression
  benable       -- Enable a set of breakpoints for a regular expression
  binside       -- Set a breakpoint for a relative address within the
                   framework/library that's currently running. This does the
                   work of finding the offset for the framework/library and
                   sliding your address accordingly.
  bmessage      -- Set a breakpoint for a selector on a class, even if the
                   class itself doesn't override that selector. It walks the
                   hierarchy until it finds a class that does implement the
                   selector and sets a conditional breakpoint there.
  border        -- Draws a border around <viewOrLayer>. Color and width can be
                   optionally provided. Additionally depth can be provided in
                   order to recursively border subviews.
  caflush       -- Force Core Animation to flush. This will 'repaint' the UI
                   but also may mess with ongoing animations.
  dcomponents   -- Set debugging options for components.
  dismiss       -- Dismiss a presented view controller.
  fa11y         -- Find the views whose accessibility labels match labelRegex
                   and puts the address of the first result on the clipboard.
  findinstances -- Find instances of specified ObjC classes.
  flicker       -- Quickly show and hide a view to quickly help visualize where
                   it is.
  fv            -- Find the views whose class names match classNameRegex and
                   puts the address of first on the clipboard.
  fvc           -- Find the view controllers whose class names match
                   classNameRegex and puts the address of first on the
                   clipboard.
  heapfrom      -- Show all nested heap pointers contained within a given
                   variable.
  hide          -- Hide a view or layer.
  mask          -- Add a transparent rectangle to the window to reveal a
                   possibly obscured or hidden view or layer's bounds
  mwarning      -- simulate a memory warning
  pa11y         -- Print accessibility labels of all views in hierarchy of
                   <aView>
  pa11yi        -- Print accessibility identifiers of all views in hierarchy of
                   <aView>
  pactions      -- Print the actions and targets of a control.
  paltrace      -- Print the Auto Layout trace for the given view. Defaults to
                   the key window.
  panim         -- Prints if the code is currently execution with a UIView
                   animation block.
  pbcopy        -- Print object and copy output to clipboard
  pblock        -- Print the block`s implementation address and signature
  pbundlepath   -- Print application's bundle directory path.
  pca           -- Print layer tree from the perspective of the render server.
  pcells        -- Print the visible cells of the highest table view in the
                   hierarchy.
  pclass        -- Print the inheritance starting from an instance of any class.
  pcomponents   -- Print a recursive description of components found starting
                   from <aView>.
  pcurl         -- Print the NSURLRequest (HTTP) as curl command.
  pdata         -- Print the contents of NSData object as string.
  pdocspath     -- Print application's 'Documents' directory path.
  pinternals    -- Show the internals of an object by dereferencing it as a
                   pointer.
  pinvocation   -- Print the stack frame, receiver, and arguments of the
                   current invocation. It will fail to print all arguments if
                   any arguments are variadic (varargs).
  pivar         -- Print the value of an object's named instance variable.
  pjson         -- Print JSON representation of NSDictionary or NSArray object
  pkeywinlevel  -- An incredibly contrived command that prints the window level
                   of the key window.
  pkp           -- Print out the value of the key path expression using
                   -valueForKeyPath:
  pmethods      -- Print the class and instance methods of a class.
  poobjc        -- Print the expression result, with the expression run in an
                   ObjC++ context. (Shortcut for "expression -O -l ObjC++ -- " )
  pproperties   -- Print the properties of an instance or Class
  present       -- Present a view controller.
  presponder    -- Print the responder chain starting from a specific responder.
  psjson        -- Print JSON representation of Swift Dictionary or Swift Array
                   object
  ptv           -- Print the highest table view in the hierarchy.
  pvc           -- Print the recursion description of <aViewController>.
  pviews        -- Print the recursion description of <aView>.
  rcomponents   -- Synchronously reflow and update all components.
  sequence      -- Run commands in sequence, stopping on any error.
  setinput      -- Input text into text field or text view that is first
                   responder.
  settext       -- Set text on text on a view by accessibility id.
  show          -- Show a view or layer.
  slowanim      -- Slows down animations. Works on the iOS Simulator and a
                   device.
  taplog        -- Log tapped view to the console.
  unborder      -- Removes border around <viewOrLayer>.
  unmask        -- Remove mask from a view or layer
  unslowanim    -- Turn off slow animations.
  visualize     -- Open a UIImage, CGImageRef, UIView, or CALayer in
                   Preview.app on your Mac.
  vs            -- Interactively search for a view by walking the hierarchy.
  wivar         -- Set a watchpoint for an object's instance variable.
  xdebug        -- Print debug description the XCUIElement in human readable
                   format.
  xnoid         -- Print XCUIElement objects with label but without identifier.
  xobject       -- Print XCUIElement details.
  xtree         -- Print XCUIElement subtree.
  zzz           -- Executes specified lldb command after delay.
