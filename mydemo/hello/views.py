from django.core.validators import validate_email
from django.shortcuts import render
import os
import random
import string
from django.db import connection
from django.contrib.auth.models import User

from .models import Client


# Create your views here.

def index(request):
    return render(request, "index.html")

# Создание пользователей
# for i in range(1, 15):
#     username = f"user{i}"
#     password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
#     user = User.objects.create_user(username, f"{username}@example.com", password)
#     user.save()
#     break

# Создание баз данных
# for i in range(1, 15):
#     db_name = f"Bs{i}"
#     with connection.cursor() as cursor:
#         cursor.execute(f"CREATE DATABASE {db_name}")
#     break

# Настройка прав доступа пользователей к базам данных
# for i in range(1, 15):
#     username = f"user{i}"
#     db_name = f"Bs{i}"
#     with connection.cursor() as cursor:
#         cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {username}")
#         cursor.execute(f"REVOKE CREATE DATABASE, REVOKE, GRANT FROM {username}")
#

# # Создание базы данных BsAll и таблицы Users
# with connection.cursor() as cursor:
#     cursor.execute("CREATE DATABASE BsAll")
#     cursor.execute("CREATE TABLE Users (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")

# # Заполнение таблицы Users данными созданных пользователей и паролях
# for i in range(1, 15):
#     username = f"user{i}"
#     password = User.objects.get(username=username).password
#     with connection.cursor() as cursor:
#         cursor.execute(f"INSERT INTO Users (username, password) VALUES ('{username}', '{password}')")

#
def decrypt_password(encrypted_password):
    # Реализация алгоритма расшифровки пароля
    # В этом примере мы используем простой алгоритм расшифровки, но в реальном приложении вам нужно использовать более безопасный алгоритм
    decrypted_password = encrypted_password[::-1]
    return decrypted_password
#
# # отображение паролей
def display_users_with_decrypted_passwords():
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, password FROM Users")
        users = cursor.fetchall()
        for user in users:
            username, encrypted_password = user
            decrypted_password = decrypt_password(encrypted_password)
            print(f"Username: {username}, Password: {decrypted_password}")

display_users_with_decrypted_passwords()
#
#
# # копирование
def backup_database():
    db_name = "BsAll"
    backup_file = f"{db_name}_backup.sql"
    command = f"pg_dump -U sa {db_name} > {backup_file}"
    os.system(command)
    print(f"Backup file created: {backup_file}")

backup_database()
#
# # восстановление бд
def restore_database():
    db_name = "BsAll"
    backup_file = f"{db_name}_backup.sql"
    command = f"psql -U sa {db_name} < {backup_file}"
    os.system(command)
    print(f"Database restored from backup file: {backup_file}")

restore_database()

# валидность эл почт
def validate_emails(request):
    clients = Client.objects.all()
    for client in clients:
        email = client.email
        validity = validate_email(email)
        print(f"Email: {email}, Validity: {validity}")