from setuptools import setup, find_packages

setup(name='Minesweeper',
      version='1.0',
      description='Minesweeping game',
      author='BitsPlease',
      author_email='zacharyjayhawk@gmail.com',
      url='https://github.com/zatkins-school/BitsPlease-Project1-MineSweeper',
      include_package_data=True,
      packages=find_packages(exclude=['minesweeper.egg-info']),
      scripts=['__main__.py'],
      py_modules=['__main__'],
      package_data={'Minesweeper': ['assets/*']})