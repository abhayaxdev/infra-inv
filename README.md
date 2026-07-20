## Project Template

### A Django starter template for any python/django related projects.

## Quick start

1. Clone the template and `cd` into it.
2. Run the setup command:

   ```bash
   make setup
   ```

   This optionally creates a virtual environment (`../.venv`), installs dependencies, and creates `.env` from `.env.example` (if it doesn't exist).

3. Configure your environment variables in `.env`:

   → To use SQLite, set `USE_SQLITE=TRUE`, otherwise configure the database env vars.

4. Apply database migrations:

   ```bash
   make migrate
   ```

5. Start the dev server:

   ```bash
   python manage.py runserver
   ```

## Available commands

| Command                | Action                                  |
|------------------------|-----------------------------------------|
| `make setup`           | Optionally create `../.venv`, install dependencies, create `.env` (prompts to configure before migrating) |
| `make install`         | Install dependencies                    |
| `make env`             | Create `.env` from `.env.example`       |
| `make migrate`         | Apply database migrations               |
| `make makemigrations`  | Create new database migrations          |
| `make collectstatic`   | Collect static files                    |
| `make test`            | Run tests                               |

## Notes

- Ensure you have a `.env` file at project root (see `.env.example`).
- Adjust `USE_SQLITE` and database-related env vars before running `make migrate`.
- `make setup` does **not** run migrations; run `make migrate` separately after configuring `.env`.
- `make env` will skip if `.env` already exists.
- When `make setup` creates a virtual environment, it is placed at `../.venv` (one level above the project root).