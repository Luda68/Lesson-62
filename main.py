# from fastapi import FastAPI
#
# app  = FastAPI()
#
#
# @app.get("/")
# async def welcome():
#     return {'message': 'Главная страница'}
#
#
# @app.get('/user/admin')
# async def admin():
#     return {'message': 'Вы вошли как администратор'}
#
#
# @app.get('/user/{user_id}')
# async def user(user_id):
#     return {'message': f'Вы вошли как пользователь №{user_id}'}
#
#
# @app.get('/user')
# async def user_info(username, age):
#     return f'Информация о пользователе, Имя: {username}, Возраст: {age}'

#
# from fastapi import FastAPI, Path
# from typing import Annotated
#
# app = FastAPI()
#
#
# @app.get('/')
# async def welcome() -> str:
#     return (f'Главная страница')
#
#
# @app.get('/user/admin')
# async def administrator() -> str:
#     return (f'Вы вошли как администратор')
#
#
# @app.get('/user/{user_id}')
# async def user_number(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]):
#     return (f'Вы вошли как пользователь № {user_id}')
#
#
# @app.get('/user/{username}/{age}')
# async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
#                     age: Annotated[int, Path(ge=18, le=120, description='Enter age')]):
#     return (f'Информация о пользователе. Имя: {username}, Возраст: {age}')



from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=3, max_length=15, description='Введите Ваше имя', example=' Сергей')]
                      , age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = username, age
    return f'Пользователь {current_index} зарегистрирован!'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(ge=1, le=100, description='Введите возраст', example= '1')
                      , username: str =Path(min_length=3, max_length=20, description=' Введите Ваше имя', example= 'Сергей')
                      , age: int = 30) -> str:
    users[user_id] = user_id, username, age
    return f'Информация о пользователе id# {user_id} обновлена'

@app.delete('/user/{user_id}')
async def delite_user(user_id: str) -> str:
    users.pop(user_id)
    return f'Пользователь {user_id} удалён'


