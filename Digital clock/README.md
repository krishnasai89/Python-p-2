# Digital clock

## Installing required python packages
```terminal
pip install PyQt5
```
If you’re using Python 3, you can also use pip3:
```terminal
pip3 install PyQt5
```
*Now that we have the packages, we are ready to import it in our python script.*
```py
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
```
