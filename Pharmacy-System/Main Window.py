import  sys
from PyQt5.QtWidgets import QApplication
from function import function
app = QApplication (sys.argv)
function = function()
sys.exit(app.exec())