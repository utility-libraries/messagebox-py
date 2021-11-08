# PyMessageBox
 Messagebox for userinput/useroutput **WITHOUT library dependencies** like tkinter


# Supported platforms [^1]

| Platform     | Supported | Tested |
| ------------ | --------- | ------ |
| Windows      | ✓         | ✓     |
| Linux/Mint   | ✓         | ✕     |
| Linux/Ubuntu | ✓         | ✕     |
| Linux/Xorg   | ✕         | ✕     |
| Linux/GNOME  | ✕         | ✕     |
| macOS        | ✕         | ✕     |

[^1]: I need tester. please report bugs etc. under your platform  

# Message-Boxes
- showinfo
- showwarning
- showerror
- askquestion
- askokcancel
- askyesno
- askretrycancel

# Usage

```python
import messagebox

messagebox.showinfo('Success', 'This package works')
```
