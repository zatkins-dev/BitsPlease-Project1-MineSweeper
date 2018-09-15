pip install sphinx
rm Minesweeper.rst
rm modules.rst
rm Minesweeper.Graphics.rst
rm -r _build/
sphinx-apidoc -l -o . ../ 
make html
