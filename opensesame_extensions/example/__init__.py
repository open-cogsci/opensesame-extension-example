"""A docstring for the namespace package that contains the extension(s)"""

__version__ = '0.0.1'

# This information is used by the update checker to see if updates are
# available. Both pip and packages are supported
update_sources = [
    {'type': 'conda',
     'pkg': 'opensesame-extension-example',
     'channel': 'conda-forge'},
    {'type': 'pip',
     'pkg': 'opensesame-extension-example',
     'server': 'https://pypi.org'}]
