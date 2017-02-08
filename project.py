# project.py - Class for the Project

class Project:
    """Class containing project details."""

    def __init__(self, name, deployed_by, deployed_time, folder, path=None):
        """Initialise the project."""
        self.name = name
        self.deployed_by = deployed_by
        self.deployed_time = deployed_time
        self.folder = folder
        self.path = path

    def __str__(self):
        return self.name

    def __repr__(self):
        fmt = 'Project(name=%r, deployed_by=%r, deployed_time=%r, folder=%r, path=%r)' %(
            self.name, self.deployed_by, self.deployed_time, self.folder,
                                          self.path)
        return fmt

    def append_path(self, projects):
        """Given a dictionary of projects, it appends the file name."""
        try:
            self.path = projects.get(self.name)
        except:
            return

    def last_deploy(self):
        """Returns format 'deployed time - deployed by'."""
        return '%s - %s' %(self.deployed_time,
                                              self.deployed_by)
