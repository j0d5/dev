# LLDB Debugging Commands

`po [UIWindow.keyWindow recursiveDescription]`
`po [UIViewController _printHierarchy]`
`po [UIView _autolayoutTrace]`
`po [_UIViewLayoutFeedbackLoopDebugger layoutFeedbackLoopDebugger]`

```
// llbd in Swift context
expr -l objc++ -O -- [UIWindow.keyWindow recursiveDescription]
```

## Examples for `findinstances`

`findinstances UIView subviews.@count > 100`
`findinstances NSArray @count > 100`
`findinstances UIScrollViewDelegate`
`findinstances UIView window == nil || hidden == true || alpha == 0 || layer.bounds.#size.width == 0`

## .lldbinit

Use chisel!

`command alias alt expr -l objc++ -O -- [[UIWindow keyWindow] _autolayoutTrace]`


## clang

Show all enabled clang checkers:
`clang -cc1 -analyzer-checker-help`
