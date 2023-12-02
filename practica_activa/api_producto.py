from fastapi import FastAPI

app= FastAPI()
productos= []
@app.get('/')
def index():
    return {'mensaje':'Binevenh'}
