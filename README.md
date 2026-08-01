## InfraInv

### A management platform for all your deployments.

## Quick start

1. Clone the repo and `cd` into it.

2. Create a virtual environment at `../.venv` (one level above the project):

   ```bash
   python3 -m venv ../.venv
   source ../.venv/bin/activate
   ```

3. Run the setup command:

   ```bash
   make setup
   ```

   This installs dependencies and creates `.env` from `.env.example` (if it doesn't exist).

4. Configure your environment variables in `.env`:

   → To use SQLite, set `USE_SQLITE=TRUE`, otherwise configure the database env vars.

5. Apply database migrations:

   ```bash
   make migrate
   ```

6. Start the dev server:

   ```bash
   python manage.py runserver
   ```

## Available commands

| Command                | Action                                  |
|------------------------|-----------------------------------------|
| `make setup`           | Install dependencies and create `.env` from `.env.example` |
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
- Create a virtual environment at `../.venv` before running `make setup`. The Makefile will auto-detect and use it.