from setuptools import setup, find_packages

setup(name='minesweeper',
      version='1.0',
      description='Minesweeping game',
      author='BitsPlease',
      author_email='zacharyjayhawk@gmail.com',
      url='https://github.com/zatkins-school/BitsPlease-Project1-MineSweeper',
      packages=find_packages(exclude=['minesweeper.egg-info']),
      scripts=['main.py'],
      package_data={'minesweeper': ['assets/*']})