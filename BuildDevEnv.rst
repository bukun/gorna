gorna
==============================

Getting Started
-----------------------------

- Change directory into your newly created project.

::

    mkdir ~/github
    cd ~/github
    git clone https://github.com/bukun/gorna.git
    cd gorna

- Create a Python virtual environment.

::

    python3 -m venv vpy_gorna
    source ~/vpy_gorna/bin/activate

- Upgrade packaging tools.

::

    pip install --upgrade pip setuptools wheel

- Install the project in editable mode with its testing requirements.

::

    pip install -e ".[testing]"

- Configure the database.

::

    initialize_gorna_db development.ini

- Run your project's tests.

::

    pytest

- Run your project.

::

    pserve development.ini --reload
