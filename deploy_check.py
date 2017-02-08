# deploy_check.py - Checks the current deployed SSIS projects against
# the users current local versions.

import local_projects as lp
import server


def compare_packages(local_packages, server_packages):
    """Compares the packages in the two given lists."""
    #remove packages that are the same in both as these are ok.
    local = [x for x in local_packages if x not in server_packages]
    server = [x for x in server_packages if x not in local_packages]
    compares = {}
    
    if len(local) + len(server) == 0:
        return None
    else:
        # Upgrades
        compares['3.Upgraded Version'] = compare_versions(local,server, 'local')
        # Downgrades
        compares['4.Downgraded Version'] = compare_versions(server,local, 'server')
        # Added
        compares['1.No Server Version'] = compare_missing(local,server)
        # Missing
        compares['2.No Local Version'] = compare_missing(server,local)
        return compares
    
def compare_versions(local, server, master):
    """Prints packages where version is higher in the first list."""
    if master == 'local':
        return [(local_package,local_version,server_version)
                for local_package,local_version in local
                for server_package, server_version in server
                    if local_package == server_package
                    and local_version > server_version]
    else:
        return [(local_package,server_version,local_version)
                for local_package,local_version in local
                for server_package, server_version in server
                    if local_package == server_package
                    and local_version > server_version]

def compare_missing(local,server):
    """Prints packages in the first list that are not in the second."""
    return [(l,v) for l,v in local if l not in [s for s, _ in server]]

def main(connection, project, folder):
    local_packages = lp.parse_xml(folder)
    server_packages = server.get_packages(connection, project)
    compares = compare_packages(local_packages,server_packages)
    return compares
