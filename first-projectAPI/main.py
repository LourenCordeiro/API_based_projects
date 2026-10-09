from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Animal(BaseModel):
    id: str
    nome: str
    especie: str
    raca: str
    sexo: str
    idade: int
    peso: float
    pelagem: str
    

animais: list[Animal] = []

@app.get("/")
def read_root():
    return {"Iniciar Cadastro de": "Animais"}


@app.get("/animais")
def listar_animais():
    return animais


@app.get("/animais/{animais_id}")
def buscar_animal(animal_id: str):
    for animal in animais:
        if animal.id == animal_id:
            return animal
    raise HTTPException(status_code=404, detail="Animal não encontrado")


@app.put("/animais/{animal_id}")
def atualizar_animal(animal_id: str, dados: Animal):
    for posicao, animal in enumerate(animais):
        if animal.id == animal_id:
            animais[posicao] = dados
            return dados
    raise HTTPException(status_code=404, detail="Animal não encontrado")


@app.post("/animais", status_code=201)
def cadastrar_animal(animal: Animal):
    animais.append(animal)
    return animal

@app.delete("/animais/{animal_id}")
def deletar_animal(animal_id: str):
    for posicao, animal in enumerate(animais):
        if animal.id == animal_id:
            animais.pop(posicao)
            return {"mesagem": f"Animal {animal_id}:{animal.nome} deletado com sucesso "}
    raise HTTPException(status_code=404, detail="Animal não encontrado") 
