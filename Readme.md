## Generar models con flask-sqlalchemy
```
flask-sqlacodegen --flask --outfile app/models_2.py postgresql://postgres:123@localhost:5433/manage_users
```


## Create tunnel to port 
```
ngrok http 4000
```