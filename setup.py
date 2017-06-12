from setuptool import setup,find_packages

setup(name = "Data_Science_Python",
      version = '0.0.1',
      url = 'https://github.com/deepak223098/Data_Science_Python'
      license = 'BSD',
      author = 'deepak'
      packagees = find_packages(),
      install_requires = ['Pyqt5',
                          'pandas',
                          'sqlalchemy',
                          'nltk',
                          'numpy',
                          'jupyter',
                          'python-twitter'],
      entry_points ={},
      extras_require = {'dec':['flake8']},)
