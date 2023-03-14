"""A docstring with a description of the extension"""

# A standard icon name
# - <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>
icon = 'applications-accessories'
# The label and the tooltip are used to create the default action, which is
# insert into the menu and/ or toolbar (or neither)
label = "Example extension"
tooltip = "Example tooltip"
menu = {
    "index": -1,
    "separator_before": True,
    "separator_after": True,
    "submenu": "Example"
}
toolbar = {
    "index": -1,
    "separator_before": True,
    "separator_after": True
}
# Settings are perstistently stored in the cfg object
settings = {
    "example_setting": "example value"
}
