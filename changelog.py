# changelog.py - Contains the version history for the program.


def main():
    """Returns the ordered dictionary of version changes."""
    changelog = {
        '1.0.0' : 'Console based program to compare projects.',
        '2.0.0' : 'Window based GUI for easier user experience.',
        '2.1.0' : 'Added option to copy compare data.',
        '2.2.0' : 'Ability to deploy project directly from the program.'

        }

    return sorted(changelog.items(), key = lambda x: x[0])
