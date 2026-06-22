from fastapi import FastAPI
from datetime import datetime

# Crear aplicacion fastapi
app = FastAPI(
    title="Hello Backend API",
    description="My first API REST as Backend Engineer in Training",
    version="0.1.0",
)


# endpoint raiz
@app.get("/")
def read_root():
    return {
        "message": "Hey,universe! This is my first API REST",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
    }


# endpoint con mi perfil
@app.get("/profile")
def get_profile():
    return {
        "name": "SentiosTech",
        "role": "Backend Engineer in Training",
        "background": "Electromechanical Engineer",
        "current_role": "Data Analyst",
        "learning_stack": ["Python", "FastAPI", "Postgresql", "Docker", "Git"],
        "goal": "Become a Senior Backend Engineer in Five years",
        "started_learning": "06-20-26",
    }


# endpoint con un mensaje personalizado
@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello, {name}! Welcome to Backend Engineering world",
        "timestamp": datetime.now().isoformat(),
    }
