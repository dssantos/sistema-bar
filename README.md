## To Dev

1. Clone repo
2. Create a virtualenv
3. Active virtualenv
4. Install dependences
5. Copy and edit your .env file

```console
git clone https://github.com/dssantos/sampleproject.git sampleproject
cd sampleproject
python -m venv .sampleproject
source .sampleproject/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
cat .env
```

## To Use

1. Migrate tables
2. Create a user
3. Run server
4. Access admin panel <http://127.0.0.1:8000/admin>

```console
python manage.py migrate
python manage.py createsuperuser && python manage.py runserver
```
