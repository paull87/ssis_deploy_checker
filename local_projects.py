# local_projects.py - Formats the local project xml to determine package versions
# to compare against the deployed project.

import os
import sys
from lxml import etree as et
from collections import namedtuple

# Create a Package class 
Package = namedtuple('Package', ['name', 'version'])

#Get the folder of the packages to be checked
def find_obj_path(foldername):
    """Looks for the folder containing the relevant project file(s)."""
    files = []
# Find path for folder containing DW-ACDSv2 folder
    for folder, subfolder, file in os.walk(foldername):
        if os.path.basename(folder).lower() == 'obj':
            file = find_project_file(folder)
            if file:
                files.append(file)

    return files

def find_project_file(foldername):
    """Returns the latest built project file path."""
    files = []
    for folder, subfolder, file in os.walk(foldername):
            for filename in file:
                if filename.lower().endswith('.dtproj'):
                    files.append(os.path.join(folder, filename))

    if files:
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return files[0]
    else:
        return None

def parse_xml(path):
    """Parses the xml of the dtproj file."""
    ns = {'SSIS': "www.microsoft.com/SqlServer/SSIS",}
    proj_xml = et.parse(path)
    proj_packages = get_packages(proj_xml, ns)

    packages = [Package(*package_properties(package, ns))
                for package in proj_packages]
    
    #package_props = {}
    #for package in packages:
    #    name, version = package_properties(package, ns)
    #    package_props[name] = version

    return packages
    

def get_packages(xml, ns):
    """Extracts all executable (task) nodes of the package xml."""
    execs = []
    for x in xml.iter():
        if x.xpath('./SSIS:PackageMetaData', namespaces = ns):
            for x_exec in x:
                execs.append(x_exec)

    return execs

def package_properties(package, ns):
    """Extracts all executable (task) nodes of the package xml."""
    #name_path = './SSIS:Properties/SSIS:Property[@SSIS:Name="Name"]'
    version_path = './SSIS:Properties/SSIS:Property[@SSIS:Name="VersionBuild"]'
    #name = package.xpath(name_path, namespaces = ns)[0].text
    name = package.values()[0][:-5]
    version = int(package.xpath(version_path, namespaces = ns)[0].text)

    return name, version
    
