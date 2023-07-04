# Dynamic_Import_Tst.py
# You can import a module dynamically using the importlib module.
# This can be useful when you want to import a module based on user input or configuration.


import importlib

module_name = 'math'
module = importlib.import_module(module_name)
result = module.sqrt(9)



















