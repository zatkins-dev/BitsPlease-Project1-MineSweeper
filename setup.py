from distutils.core import setup

setup(name='minesweeper',
      version='1.0',
      description='Minesweeping game',
      author='BitsPlease',
      author_email='zacharyjayhawk@gmail.com',
      url='https://github.com/zatkins-school/BitsPlease-Project1-MineSweeper',
      packages=['minesweeper'],
      package_data={'minesweeper': ['assets/*']})