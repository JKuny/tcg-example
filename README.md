# TCG-Example

A Django-based website for a fake TCG store. Contains player tracking,
tournament and store functionality for learning
purposes.

## Running

```shell
# Install targeted Python version
pyenv install 3.10.11

# Setup venv
uv venv --seed

# Start the Postgres database
docker compose up -d

# Run the development server on 8080 (less likely for conflicts)
python manage.py runserver 8080

# Run the tailwindcss development server (django-tailwind)
python manage.py tailwind start
```

The site will be available at:

- [Main page](http://127.0.0.1:8080/)
- [Admin page](http://127.0.0.1:8080/admin/)

## Seeding the Database

For seeding sample data into the website, you can run the script found in `bin`.

```shell
bin/seed.sh
```
