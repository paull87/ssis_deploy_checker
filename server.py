# server.py - checks the connection to the server and connects to the SSISDB,
# returning the deployed projects and their packages.

import pyodbc, subprocess, sqlscripts
from collections import namedtuple
from project import Project

# Create a Package class 
Package = namedtuple('Package', ['name', 'version'])

def get_packages(connection, project):
    """Queries the DB to get the projects and their last deployment details."""
    results = connection.cursor()
    results.execute(sqlscripts.package_sql)
    # Output the results
    packages = output_packages(results, project)
    return packages
    
def output_packages(project_packages, project):
    """Output the list of packages and their version."""
    packages = [Package(row.Package, int(row.DeployedVersion))
                for row in project_packages if row.Project == project]
    return packages

def get_projects(connection):
    """Queries the DB to get the projects and their last deployment details."""
    project_names = []
    results = connection.cursor()
    try:
        results.execute(sqlscripts.project_sql)
        for row in results:
            #row.Project, row.DeployedBy, row.DeployedTime
            project_names.append(Project(
                row.Project, row.DeployedBy, row.DeployedTime, row.Folder))
        return project_names
    except:
        return []

def deploy_project(cmd):
    result = subprocess.call(cmd, shell=True)

    if result == 0:
        return 'Deployment Successful'
    else:
        return 'Deployment Failed'

def ping_server(server):
    """Checks that server is available."""
    return subprocess.call('ping -n 1 -w 1 %s' %(server),
                           shell=True#,
                           #stdout=subprocess.PIPE
                           ) == 0

def connect(server):
    """Attempts to connect to the given server and returns the connection."""
    connect_string = ('DRIVER={SQL Server};SERVER=%s;PORT=1433;DATABASE=SSISDB'
                      %(server))
    try:
        connection = pyodbc.connect(connect_string, timeout=2)
        return connection
    except:
        return None


