# 🐾 API de Cadastro de Animais

API REST simples para cadastrar, consultar, atualizar e remover animais, construída com **FastAPI** e **Pydantic**.

## 🎯 Objetivo

Este projeto foi criado para praticar os fundamentos de construção de APIs em Python:

- Criação de rotas HTTP (GET, POST, PUT, DELETE)
- Validação automática de dados com Pydantic
- Uso de parâmetros de rota (path params) e corpo da requisição (body)
- Tratamento de erros com códigos HTTP (404, 422)
- Operações CRUD completas (Create, Read, Update, Delete)

## 🛠️ Tecnologias

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/): framework para criação de APIs
- [Pydantic](https://docs.pydantic.dev/): validação de dados
- [uv](https://docs.astral.sh/uv/): gerenciador de pacotes e ambiente virtual

## 📋 Modelo de dados

Cada animal possui os seguintes campos (todos obrigatórios):

| Campo     | Tipo    | Exemplo      |
|-----------|---------|--------------|
| `id`      | texto   | `"A001"`     |
| `nome`    | texto   | `"Ursula"`   |
| `especie` | texto   | `"Gato"`     |
| `raca`    | texto   | `"SRD"`      |
| `sexo`    | texto   | `"F"`        |
| `idade`   | inteiro | `10`         |
| `peso`    | decimal | `4.7`        |
| `pelagem` | texto   | `"Cinza"`    |

Se algum campo estiver faltando ou com o tipo errado, a API responde automaticamente com **422 Unprocessable Entity**.

## 🔗 Rotas

| Método   | Rota                   | Descrição                           | Resposta de sucesso |
|----------|------------------------|-------------------------------------|---------------------|
| `GET`    | `/`                    | Mensagem inicial                    | 200                 |
| `GET`    | `/animais`             | Lista todos os animais cadastrados  | 200                 |
| `GET`    | `/animais/{animal_id}` | Busca um animal pelo id             | 200                 |
| `POST`   | `/animais`             | Cadastra um novo animal             | 201                 |
| `PUT`    | `/animais/{animal_id}` | Atualiza todos os dados de um animal| 200                 |
| `DELETE` | `/animais/{animal_id}` | Remove um animal                    | 200                 |

As rotas que recebem `animal_id` retornam **404 Not Found** quando o animal não existe.

## 🚀 Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/SEU-USUARIO/API_based_projects.git
cd API_based_projects
```

**2. Instale as dependências**
```bash
uv sync
```

**3. Inicie o servidor**
```bash
uv run fastapi dev first-projectAPI/main.py
```

**4. Acesse a documentação interativa**

Abra no navegador: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Na página `/docs` é possível testar todas as rotas: clique na rota, depois em **Try it out** e em **Execute**.

## 🧪 Exemplo de uso

**Cadastrar um animal** (`POST /animais`):
```json
{
  "id": "A001",
  "nome": "Ursula",
  "especie": "Gato",
  "raca": "SRD",
  "sexo": "F",
  "idade": 10,
  "peso": 4.7,
  "pelagem": "Cinza"
}
```

**Resposta** (`201 Created`):
```json
{
  "id": "A001",
  "nome": "Ursula",
  "especie": "Gato",
  "raca": "SRD",
  "sexo": "F",
  "idade": 10,
  "peso": 4.7,
  "pelagem": "Cinza"
}
```

**Deletar um animal** (`DELETE /animais/A001`):
```json
{
  "mensagem": "Animal A001:Ursula deletado com sucesso"
}
```

## ⚠️ Limitações

- Os dados ficam armazenados **em memória** (numa lista Python). Ao reiniciar o servidor, todos os cadastros são perdidos.
- Não há verificação de `id` duplicado no cadastro.
- O `PUT` substitui o animal inteiro, então é necessário enviar todos os campos.
