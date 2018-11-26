from distutils.core import setup

setup (name = 'pynuklear',
       version = '0.0.1',
       description = 'Bindings to the nuklear immediate mode GUI library',
       author = 'William Emerison Six',
       author_email = 'billsix@gmail.com',
       url = 'https://github.com/billsix/pyNuklear',
       keywords = "nuklear imgui",
       license = "MIT",
       packages=['pynuklear',
                 'pynuklear/demo',
                 'pynuklear/demo/glfw_opengl2',
                 'pynuklear/demo/glfw_opengl3'],
       package_dir={'pynuklear': 'src/pynuklear',
                    'pynuklear/demo': 'src/pynuklear/demo/',
                    'pynuklear/demo/glfw_opengl2': 'src/pynuklear/demo/glfw_opengl2',
                    'pynuklear/demo/glfw_opengl3': 'src/pynuklear/demo/glfw_opengl3'},
       package_data={'pynuklear/demo/glfw_opengl3': ['triangle*'],
                     '' : ["*.so"]},
       classifiers=[
           "Development Status :: 3 - Alpha",
           "Topic :: Utilities",
           "License :: OSI Approved :: MIT License",
       ],
       long_description = '''
Bindings to the nuklear immediate mode GUI library.  The only way to GUI.
''')
