all: install dist

install:
	sudo pip install -e .

dist:
	sudo python setup.py sdist

upload: dist
	twine upload dist/*

clean:
	sudo rm -rf dist surbtc.egg-info surbtc/__pycache__ surbtc/*.pyc
