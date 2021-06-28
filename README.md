# PyMessageBox
 Messagebox for userinput/useroutput WITHOUT library dependencies like tkinter



---

# Installation

Just download the file (PyMessageBox.py) and paste it in your project



---

# Styles

## Box-Style

- ERROR
- ASK
- PANIC
- INFO

## Button-Style

- OK
- OK_CANCEL
- CANCEL_RETRY_IGNORE
- YES_NO_CANCEL
- YES_NO
- RETRY_CANCEL
- CANCEL_RETRY_CONTINUE



---

# Usage

## MessageBox

`MessageBox(title: str, message: str, style: int) -> str`

```python
from PyMessageBox import MessageBox, INFO, YES_NO
MessageBox("Title", "Message", INFO | YES_NO)
```

## EventMessageBox

`EventMessageBox(title: str, message: str, style: int, **callbacks) -> None`

```py
from PyMessageBox import EventMessageBox, INFO, YES_NO

def cb_yes():
	print("I like you project")

def cb_no():
	print("I don't like your project")
	
EventMessageBox("Title", "Do you like my project", INFO | YES_NO, YES=cb_yes, NO=cb_no)
```

