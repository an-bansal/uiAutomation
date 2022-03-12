
# Author: Anubhav
#

echo 'cd to the location for installing python venv'
cd $1

echo 'Removing Existing virtualenv'
rm -rf pyenv

echo 'Creating and Activating virtualenv with dependencies'
python -m venv pyenv
#virtualenv pyenv -p python  --no-site-packages
source pyenv/bin/activate

python --version

#pyenv/bin/python -m pip install krb5
pyenv/bin/python -m pip install --upgrade pip
#pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org certifi
#pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org flask
#pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org concurrent-utils
#pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests
#pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests-kerberos --no-cache-dir
#pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests-negotiate
pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org python-logstash
#pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pyjwt
pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pytest
pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pytest-selenium
pyenv/bin/python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pandas

pyenv/bin/python -m pip list
