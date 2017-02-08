# about.py - Creates the about window that is called from the main application.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, pyperclip
import changelog

from ui import AboutWindow_ui

class AboutWindow(QDialog, AboutWindow_ui.Ui_AboutWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.connect(self, b'2clicked()', self.showContextMenu)
        self.label_contact.connect(self.label_contact, SIGNAL('clicked()'), self.showContextMenu)
        # Custom context Menu
        #self.label_contact.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.label_contact.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self):
        """Creates a context menu for left click on Contact details."""
        menu = QMenu(self)
        copy = QAction('Copy Email', self) 
        menu.addAction(copy)
        menu.popup(QCursor().pos())
        copy.triggered.connect(self.copy_text)

    def copy_text(self):
        """Copies email from contact to clipboard."""
        details = self.label_contact.text().split('\n')
        email = details[-1].strip()
        pyperclip.copy(email)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AboutWindow()
    window.connect(window.label_change, SIGNAL('clicked()'), window.showContextMenu)
    window.show()
    sys.exit(app.exec_()) 
        
    
