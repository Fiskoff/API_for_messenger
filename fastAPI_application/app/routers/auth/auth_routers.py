"""
Задача 1.1: Реализация Регистрации/Входа (JWT)
Эндпоинты: /api/auth/register, /api/auth/login, /api/auth/logout
Защищенное хранение паролей (хэши), генерация access/refresh токенов.
Валидация входных данных (email, пароль).
"""
from fastapi import APIRouter


auth_router = APIRouter()


@auth_router.post("/register")
async def register():
    pass


@auth_router.post("/login")
async def login():
    pass


@auth_router.post("/logout")
async def logout():
    pass