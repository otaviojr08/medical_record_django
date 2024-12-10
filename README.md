# Medical-Record_Django

Trabalho prático da disciplina de Programação Web da Universidade Federal de Lavras (UFLA).

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/otaviojr08/medical_record_django.git
   cd medical_record_django
   ```

2. Crie um ambiente virtual e ative-o:

   ```sh
    python -m venv .venv
    source .venv/bin/activate # Para Windows, use `venv\Scripts\activate`
    ```

    Ou

    ```sh
    virtualenv medical_record
    source medical_record/bin/activate
    ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Execute as migrações:

   ```sh
    python manage.py makemigrations
    ```
    ```sh
    python manage.py migrate
    ```

5. Crie um superusuário:

   ```sh
    python manage.py createsuperuser
    ```

6. Execute o servidor de desenvolvimento:

   ```sh
    python manage.py runserver
    ```

8. Acesse `http://localhost:8000/`

