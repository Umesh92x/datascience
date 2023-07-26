# this editorial will help you to check and install python dependenciy while working on differnt different machines/operation systems where python required
# libraries are not preinstalled and user dont need to install them manually, the code will automacially take care of them.

import importlib
def check_library_first():
    # Define the required libraries
    libraries = ['numpy', 'matplotlib', 'seaborn', 'statsmodels', 'docx','tsfeatures']
    # Iterate over the libraries
    for library in libraries:
        try:
            # Try importing the library
            importlib.import_module(library)
            print(f"{library} is already installed.")
        except ImportError:
            # If import fails, install the library
            print(f"{library} is not installed. Installing...")
            try:
                import pip
                pip.main(['install', library])
                print(f"{library} has been successfully installed.")
            except Exception as e:
                print(f"Error occurred while installing {library}: {str(e)}")
    return None
check_library_first()

Output
'''
numpy is already installed.
matplotlib is already installed.
seaborn is already installed.
statsmodels is already installed.
docx is already installed.
tsfeatures is already installed.
'''

  
