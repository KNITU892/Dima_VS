from PySide import QtCore, QtGui
import sys
from ui import Ui_Dialog

app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
