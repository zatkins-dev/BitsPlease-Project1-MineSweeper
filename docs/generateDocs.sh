rm Minesweeper.rst
rm modules.rst
rm Minesweeper.Graphics.rst
sphinx-apidoc -o . ../Minesweeper
make html
