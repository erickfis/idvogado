# idvogado

An android app meant to connect *Employment Law Attorneys* with workers in need. Built with love in Python.

## Installing kivy

In order to contribute, you will need to install kivy in your virtual environment. Please run the following:

    pip install --upgrade pip wheel setuptools
    pip install kivy
    pip install docutils pygments pypiwin32 kivy-deps.sdl2 kivy-deps.glew
    pip install kivy-deps.gstreamer
    pip install kivy-deps.angle
    pip install –-upgrade kivy


## Dev team

[Erick Medeiros Anastácio](https://www.linkedin.com/in/erick-medeiros-anastácio-15241717) - erickfis@gmail.com

[Mateus Alberto Ferreira](https://www.linkedin.com/in/mateusalberto/) - mateusalberto@hotmail.co.uk

[Italo Marques](https://www.linkedin.com/in/italo-marques-966298b9/) - italo_aas@hotmail.com

[Sarah Ribeiro](https://www.linkedin.com/in/sarah-c-ribeiro/) - sarinhah@gmail.com


## Rules for development

### Code Style

- everything inside code must be in English
- write code following PEP8 & PEP256 conventions
- always provide proper docstrings for your methods / functions and scripts
- ATOM will aid you in almost everything
- always comment your code to explain your logic and decisions
- always provide notebooks for demonstrating your development and how to use it
- always try/except
- always avoid nesting by splitting tasks into functions
- try always using auxiliary scripts, for writing cleaner code


### Unit tests

- In this project we will be always writing unit test scripts for our code.
- for each method/function, please write the respective unit test

#### Pytest guide

- install pytest packages:

        pip install pytest
        pip install pytest-html

- clone the repo
- inside your folder (ie: scrapy) create a folder test/
- write your test_*.py there
- write your marks on src/pytest.ini
- navigate the terminal to src/
- pip install the path:

        pip install -e .

- run the testing routine as

        pytest -m scores --html="scoring/test/testing_scores.html"

- profit!
