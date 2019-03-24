apt-get -qqy update
DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
apt-get -qqy install postgresql python-pyscopg2
apt-get -qqy install python-sqlalchemy
apt-get -qqy install python3-pip
pip3 install --upgrade pip
pip install werkzeug==0.8.3
pip install flask==0.9
pip install Flask-Login==0.1.3
pip install oauth2client
pip install requests
pip install httpblib2
pip install SQLAlchemy
