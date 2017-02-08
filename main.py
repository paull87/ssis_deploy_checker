# app.py - Runs the SSIS Deployment Checker application.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os, json, pyperclip, datetime
import server, local_projects as lp
import deploy_check

from ui import SSISDeploymentChecker_ui
from about_window import AboutWindow
from deploy_window import DeployWindow

# Set path of the history file.
try:
    path = os.environ['TEMP']
except:
    path = '.'
history = 'DeployServerHistory.tmp'
history_file = os.path.join(path, history)

def find_deployment_exe():
    """Searches for the ISDeploymentWizard.exe for deployments."""
    sql_path = 'C:\\Program Files\\Microsoft SQL Server'
    exes = []
    for folder, sub, files in os.walk(sql_path):
        if os.path.basename(folder).lower() == 'binn':
            for file in files:
                if file.lower() == 'isdeploymentwizard.exe':
                    exes.append(os.path.join(folder,file))

    if exes:
        return exes[-1]
    else:
        return None

##def license_check():
##    """Checks that you can run the program."""
##    expiry = datetime.date(2017,3,28)
##
##    return expiry < datetime.date.today()

def check_server(server_name):
    """Checks that the server is accessible and returns the connection."""
    if server.ping_server(server_name):
        return server.connect(server_name)
    else:
        return 'Unable to connect to server'

def get_history(name):
    """Returns the list of servers previously used."""
    if os.path.isfile(history_file):
        try:
            with open(history_file, 'r') as file:
                data = json.load(file)
            data[name].sort()
            return data[name]
        except:
            return []
    else:
        create_history()
        return []

def create_history():
    """Creates a default ignore folder and history file."""
    FILE_ATTRIBUTE_HIDDEN = 0x02
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
        empty_file = '{"servers": [], "locals": []}'
        with open(history_file, 'w') as file:
            file.writelines(empty_file)
    except:
        pass

def add_history(item, all_items, name):
    """Adds to existing history."""
    all_items.append(item)
    try:
        with open(history_file, 'r') as file:
            data = json.load(file)
        data[name] = all_items
    except:
        return
    try:
        with open(history_file, 'w') as file:
            json.dump(data, file)
    except:
        return

def check_dupes(projects):
    """Checks if there are any duplicate projects and returns an error."""
    return sorted([k.name for k,v in projects.items() if len(v) > 1])

def get_project_folder(folder):
    """Defines the Folder/Project from the given path."""
    os.path.split(folder)

class SSISDeployCheck(QMainWindow, SSISDeploymentChecker_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.reset_app()
        self.about_window = AboutWindow(self)
        self.deploy_window = DeployWindow(self)        

        # Custom context Menu
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.showContextMenu)

        # get any history of combo boxes and reset index
        self.comboServer.addItems(get_history('servers'))
        self.comboServer.setCurrentIndex(-1)
        self.comboFile.addItems(get_history('locals'))
        self.comboFile.setCurrentIndex(-1)

        # Set action for clicking About.
        self.actionAbout.triggered.connect(self.show_about_window)

        # Set action for closing the app.
        self.actionExit.triggered.connect(self.close)

        # Set action for reseting the app.
        self.actionReset.triggered.connect(self.reset_app)

        # Set action for clicking browse button
        self.buttonBrowse.clicked.connect(self.browse_file)

        # Set action for clicking the compare button
        self.buttonCompare.clicked.connect(self.compare)

        # On change of server value, check the connection.
        self.comboServer.currentIndexChanged.connect(
            self.check_server_value)
        self.comboServer.lineEdit().editingFinished.connect(
            self.check_server_value)

        # On change of folder value, check the connection.
        self.comboFile.currentIndexChanged.connect(
            self.check_folder_value)
        self.comboFile.lineEdit().editingFinished.connect(
            self.check_folder_value)

        self.setFocus()

    def show_about_window(self):
        self.about_window.show()

    def show_deploy_window(self, cmd, source, destination):
        self.deploy_window.server = self._compare_server
        sourcefolder = source.split('"')[-2]
        self.deploy_window.source_path = '\\'.join(sourcefolder.split('\\')[-5:-3])
        self.deploy_window.deploy_path = destination.split('"')[-2]
        self.deploy_window.cmd = cmd
        self.deploy_window.update_deploy_label()
        self.deploy_window.show()

    def showContextMenu(self, position):
        """Creates a context menu for left click on tree."""
        menu = QMenu(self)
        copy = QAction('Copy', self) 
        deploy = QAction('Deploy', self)
        no_deploy = QAction('No local to deploy', self)
        menu.addAction(copy)
        

        # Add deploy option if left click is on valid Project node.
        current = self.treeWidget.currentItem()
        if not current.parent():
            menu.addSeparator()
            if current.text(1) != 'No local copy found':
                menu.addAction(deploy)
            else:
                menu.addAction(no_deploy)

        copy.triggered.connect(self.copy_text)
        deploy.triggered.connect(self.deploy_project)
        menu.popup(self.treeWidget.mapToGlobal(position))

    def deploy_project(self, project):
        """Starts window to deploy the project to the given server."""
        deploy_wizard = find_deployment_exe()

        if not deploy_wizard:
            QMessageBox.critical(self, "Deploy Error",
                'No Deploy Wizard installed. Check your SQL installation.')
            return
        
        project = self.treeWidget.currentItem()
        
        project_details = [x for x in self._projects
                           if x.name == project.text(0)][0]

        # Source Path
        fmt = '/SourcePath:"{}" '
        ispac_file = project_details.path.replace('\\obj\\','\\bin\\')
        ispac_file = ispac_file.replace('.dtproj','.ispac')
        if not os.path.isfile(ispac_file):
            QMessageBox.critical(self, "Deploy Error",
                             'No valid ispac file found to deploy.')
            return
        source_path = fmt.format(ispac_file)

        # Destination Server
        fmt = '/DestinationServer:"{}" '
        dest_server = fmt.format(self._compare_server)

        # Destination Path
        fmt = '/DestinationPath:"/{a[0]}/{a[1]}/{a[2]}" '
        dest_path = fmt.format(a = ['SSISDB',
                              project_details.folder,
                              project_details.name])

        # Command Line
        cmd_line = ' '.join(['"{}"'.format(deploy_wizard),
                            '/Silent ',
                             source_path,
                             dest_server,
                             dest_path])

        #QMessageBox.information(self, "Deploy", 'Can Deploy to:\n{}'.format(
        #    cmd_line))

        self.show_deploy_window(cmd_line, source_path, dest_path)

    def copy_text(self):
        """Copies the selected text from the tree."""
        try:
            current_item = self.treeWidget.currentItem()#.text(0)
        except:
            return

        # Lowest level of tree
        if current_item.childCount() == 0:
            text = current_item.text(0)
        # Second level of tree.
        elif current_item.parent():
            text = '{} - {}'.format(current_item.parent().text(0),
                                    current_item.text(0))
            for n in range(current_item.childCount()):
                text += '\n\t{}'.format(current_item.child(n).text(0))
        else:
            text = current_item.text(0)
            for n in range(current_item.childCount()):
                text += '\n{}'.format(current_item.child(n).text(0))
                for n1 in range(current_item.child(n).childCount()):
                    text += '\n\t{}'.format(
                        current_item.child(n).child(n1).text(0))        

        pyperclip.copy(text)      

    def compare(self):
        """Compares the local project against the deployed project."""
##        if license_check():
##            QMessageBox.critical(self, "Expired", 'No longer available.')
##            return
        
        # Check the server is valid
        if self._current_server == '' or not self._projects:
            QMessageBox.warning(self, "Warning", 'Please select a valid server.')
            return
        
        # Check that the folder is valid.
        if not os.path.isdir(self._current_folder):
            QMessageBox.warning(self, "Warning", 'Please select a valid folder.')
            return

        # Get dtproj files
        local_projects = lp.find_obj_path(self._current_folder)
        if not local_projects:
            QMessageBox.warning(self, "Warning",
                    'No project files found. Check folder and try again.')
            return

        # Match up the local project to server project.
        local_project_files = {x:os.path.basename(x) for x in local_projects}
        project_matches = {p:[k for k,v in local_project_files.items()
                              if p.name == v.split('.')[0]]
                           for p in self._projects}       

        duplicates = check_dupes(project_matches)
        if duplicates:
            message = 'The following projects have mulitple local versions - '
            message += '{}/n'.format('\t\n'.join(duplicates))
            message += 'Please check the folder you selected and try again.'
            QMessageBox.warning(self,message)
            return

        # Add path to server_projects
        self.append_project_path(project_matches)

        # Show message to confirm projects are being compared and set projects
        project_matches = self.projects_to_compare(project_matches)

        # Reset the tree view ahead of the reload.
        self.reset_tree()
        
        # Compare the packages between the server local
        
        for server_project, local_file in sorted(
                            project_matches.items(),
                            key=lambda x: x[0].name):
            if local_file:
                compares = deploy_check.main(self._connection,
                                             server_project.name, local_file[0])
                self.add_to_tree(server_project, compares)
            else:
                self.add_to_tree(server_project, None, no_local=True)

        # Add the successful server and folder to the history to be used again.
        self.add_server_history()
        self.add_folder_history()
        self._compare_server = self._current_server
        
        self.treeWidget.show()

    def append_project_path(self, local_projects):
        """Appends the local path to the project if available."""
        for project in self._projects:
            project.append_path({k.name:v[0] for k,v
                                 in local_projects.items() if v})

    def add_to_tree(self, server_project, compares, no_local = False):
        """Adds a new trunk to the tree view for that particular project."""       
        project_item = QTreeWidgetItem(self.treeWidget)
        project_item.setText(0,server_project.name)
        project_item.setToolTip(0,server_project.last_deploy())
        if no_local:
            project_item.setIcon(0,self.error_icon)
            project_item.setText(1,'No local copy found')
            return
        if not compares:
            project_item.setIcon(0,self.success_icon)
            project_item.setText(1,'Projects in Sync')
            return
        project_item.setIcon(0,self.project_icon)
        for comp_type, packages in [(k,v) for k,v in
                                    sorted(compares.items(), key=lambda x: x[0])
                                    if v]:
            folder_item = QTreeWidgetItem(project_item)
            folder_item.setText(0,comp_type[2:])
            folder_item.setIcon(0,self.folder_icon)
            folder_item.setToolTip(0, self.tool_tips[comp_type])
            for package in packages:
                package_item = QTreeWidgetItem(folder_item)
                package_item.setText(0,package[0])
                package_item.setIcon(0,self.package_icon)
                if comp_type == '2.No Local Version':
                    package_item.setText(2,str(package[1]))
                elif comp_type == '1.No Server Version':
                    package_item.setText(1,str(package[1]))
                else:
                    package_item.setText(1,str(package[1]))
                    package_item.setText(2,str(package[2]))
                
                package_item.setIcon(0,self.package_icon)
                            
    def projects_to_compare(self, projects):
        """Show message to confirm projects are being compared and set projects."""
        project = self.comboProject.currentText()
        if project in ['', 'All']:
            message = ('Comparing all projects on {} to local copy {}'.format(
                self._current_server, self._current_folder))
            self.statusbar.showMessage(message)
        else:
            message = ("Comparing '{}' project on {} to local copy {}".format(
                project, self._current_server, self._current_folder))
            self.statusbar.showMessage(message)
            projects = {k:v for k,v in
                        projects.items() if k.name == project}
        return projects 

    def check_server_value(self):
        """Checks the value of the server box and checks the connection."""
        if not self.comboServer.currentText():
            self.server_neutral()
            return
        new_value = self.comboServer.currentText()
        if self._current_server != new_value:
            self._current_server = new_value
            self._connection = check_server(self._current_server)
            self.statusbar.showMessage('finally here')
            if self._connection and type(self._connection) != str:
                self.successful_server()
            else:
                self.server_failure(
                    self._connection if self._connection
                    else 'Unable to connect to SSISDB')
                self._connection = None
                self.clear_projects()
                
    def successful_server(self):
        """Shows a successful connection to get projects."""
        self.server_success()
        #self.add_server_history()
        self.set_projects()

    def set_projects(self):
        self._projects = server.get_projects(self._connection)
        if self._projects:
            message = 'Projects: %s' %(', '.join(
                [x.name for x in self._projects]))
            self.add_projects()
            self.statusbar.showMessage(message)
        else:
            self.statusbar.showMessage('No projects found on server.')

    def add_projects(self):
        """Adds projects to project drop down."""
        items = ['All'] + [x.name for x in self._projects]
        self.comboProject.clear()
        self.comboProject.addItems(items)
        self.comboProject.show()

    def clear_projects(self):
        """Clears project drop down."""
        self._projects = []
        self.comboProject.clear()
        self.comboProject.hide()

    def add_server_history(self):
        """Adds to the existing history if server is successfully searched."""
        current_text = self.comboServer.currentText()
        all_items = [self.comboServer.itemText(i) for i
                     in range(self.comboServer.count())]

        if (current_text not in all_items):
            self.comboServer.addItem(current_text)
            add_history(current_text, all_items, 'servers')

    def check_folder_value(self):
        """Checks the value of the folder is a real directory."""
        if not self.comboFile.currentText():
            self.folder_neutral()
            return
        new_value = self.comboFile.currentText()
        if self._current_folder != new_value:
            self._current_folder = new_value
            if os.path.isdir(new_value):
                self.folder_success()
                #self.add_folder_history()
            else:
                self.folder_failure('The folder does not exist.')

    def check_folder(self):
        """Checks if the folder exists."""
        if os.path.isdir(self._current_folder):
            self.folder_success()
            self.add_folder_history()
        else:
            self.folder_failure('The folder does not exist.')

    def add_folder_history(self):
        """Adds to the existing history if folder exists."""
        current_text = self.comboFile.currentText()
        all_items = [self.comboFile.itemText(i) for i
                     in range(self.comboFile.count())]

        if (current_text not in all_items):
            self.comboFile.addItem(current_text)
            add_history(current_text, all_items, 'locals')
            
    def reset_app(self):
        """Sets application back to start position."""
        self.comboServer.setCurrentIndex(-1)
        self.comboFile.setCurrentIndex(-1)
        self.setFocus()
        self.reset_tree()
        self.comboProject.hide()
        self._current_server = ''
        self._current_folder = ''
        self._compare_server = ''
        self._connection = None
        self._projects = []
        self.comboProject.hide()
        self.treeWidget.hide()

    def reset_tree(self):
        """Clears the tree view and hides from window."""
        self.treeWidget.clear()
        self.treeWidget.hide()
        
    def browse_file(self):
        """Shows directory explorer to pick a folder."""
        start_folder = (self._current_folder if self._current_folder != ''
                        else 'C:\\')
        self._current_folder = str(QFileDialog.getExistingDirectory(self,
                                                         "Select Directory",
                                                         start_folder))
        self.comboFile.lineEdit().setText(
            QDir.toNativeSeparators(self._current_folder))
        self.check_folder()

app = QApplication(sys.argv)
window = SSISDeployCheck()
window.show()
sys.exit(app.exec_())
