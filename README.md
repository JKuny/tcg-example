# TCG-Example

A Django-based website for a fake TCG store. Contains player tracking,
tournament and store functionality for learning
purposes.

## Running

```shell
# Start the Postgres database
docker compose up -d

# Run the development server
python manage.py runserver

# Run the tailwindcss development server (django-tailwind)
python manage.py tailwind start
```

The site will be available at:

- [Main page](http://127.0.0.1:8000/)
- [Admin page](http://127.0.0.1:8000/admin/)