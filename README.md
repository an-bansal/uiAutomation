# uiAutomation
Author : Anubhav


The project is coded on linux and uses firefox for testing

Dependencies
- Python 3.9.7
- pytest 7.0.1
- pytest-selenium 2.0.1


Setup
it is recommended to use pycharm

Else, you can use 
Use the setup/setup.sh to create python virtual environment with the dependencies
Note: you should have python 3.9.7 already installed on the system.

Launching from commandline


got to folder uiAutomation

    pytest test_aspireapp.TestAspireapp -m slow --html

Note: remove -m slow to run the full suite.

After test execution open following file in a browser for the report of the test execution

    uiAutomation/test_aspireapp.py::TestAspireapp


