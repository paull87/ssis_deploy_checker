# about.py - Creates the about window that is called from the main application.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, pyperclip
import server

from ui import DeployWindow_ui

class DeployWindow(QDialog, DeployWindow_ui.Ui_DeployWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.deploy_path = ''
        self.source_path = ''
        self.server = ''
        self.cmd = ''
        
        self.buttonAccept.clicked.connect(self.deploy_project)

        self.buttonCancel.clicked.connect(self.close_window)

    def update_deploy_label(self):
        """Updates the label to show deployment."""
        text = '\n'.join(['You are deploying',
                          '\t{}',
                          'to overwrite Project',
                          '\t{}',
                          'on Server {}'])

        self.label_warning.setText(text.format(self.source_path,
                                               self.deploy_path, self.server))

    def close_window(self):
        """Close the window in event of cancel."""
        self.deploy_path = ''
        self.source_path = ''
        self.close()
        
    def deploy_project(self):
        """Deploy the project if user is happy."""
        result = server.deploy_project(self.cmd)
        if result == 'Deployment Successful':
            QMessageBox.information(self, "Deploy Project", result)
            self.close()
        else:
            QMessageBox.critical(self, "Deploy Project", result)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeployWindow()
    window.show()
    sys.exit(app.exec_()) 
        
    
