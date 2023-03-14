"""No rights reserved. All files in this repository are released into the
public domain.
"""
from libopensesame.py3compat import *
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension


class ExampleExtension(BaseExtension):
    """An example extension that lists several common events. The class name
    should be the CamelCase version of the folder_name and file_name. So in
    this case both the extension folder (which is a Python package) and the
    .py file (which is a Python module) are called example_extension, whereas
    the class is called ExampleExtension.
    """

    def activate(self):
        """Is called when the extension is activated through the menu/ toolbar
        action.
        """
        oslogger.debug('example_extension extension activated')

    # Below is a list of event handlers, which you can implement to have your
    # extension react to specific events. A complete list of events can be
    # found in the developer documentation:
    # - <https://osdoc.cogsci.nl/3.3/dev/extension/>

    def event_startup(self):
        oslogger.debug('Event fired: startup')

    def event_prepare_regenerate(self):
        oslogger.debug('Event fired: prepare_regenerate')

    def event_regenerate(self):
        oslogger.debug('Event fired: regenerate')

    def event_run_experiment(self, fullscreen):
        oslogger.debug(f'Event fired: run_experiment(fullscreen={fullscreen})')

    def event_end_experiment(self, ret_val):
        oslogger.debug('Event fired: end_experiment')

    def event_save_experiment(self, path):
        oslogger.debug(f'Event fired: save_experiment(path={path})')

    def event_open_experiment(self, path):
        oslogger.debug(f'Event fired: open_experiment(path={path})')

    def event_close(self):
        oslogger.debug('Event fired: close')

    def event_prepare_rename_item(self, from_name, to_name):
        oslogger.debug(f'Event fired: prepare_rename_item(from_name={from_name}, to_name={to_name})')

    def event_rename_item(self, from_name, to_name):
        oslogger.debug(f'Event fired: rename_item(from_name={from_name}, to_name={to_name})')

    def event_new_item(self, name, _type):
        oslogger.debug(f'Event fired: new_item(name={name}, _type={_type})')

    def event_change_item(self, name):
        oslogger.debug(f'Event fired: change_item(name={name})')

    def event_prepare_change_experiment(self):
        oslogger.debug('Event fired: prepare_change_experiment')

    def event_change_experiment(self):
        oslogger.debug('Event fired: change_experiment')

    def event_prepare_delete_item(self, name):
        oslogger.debug(f'Event fired: prepare_delete_item(name={name})')

    def event_delete_item(self, name):
        oslogger.debug(f'Event fired: delete_item(name={name})')

    def event_prepare_purge_unused_items(self):
        oslogger.debug('Event fired: prepare_purge_unused_items')

    def event_purge_unused_items(self):
        oslogger.debug('Event fired: purge_unused_items')

    def event_process_data_files(self, data_files):
        oslogger.debug('Event fired: process_data_files')
