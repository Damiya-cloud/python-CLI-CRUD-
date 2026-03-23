# Python Click User Manager

Simple CLI app to manage users (create, read, update, delete) using Click and JSON file.

## Setup

1. Create virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. install click :
   ```bash
   pip install click
   ```

## Run app (every new terminal session)

1. Activate environment:
   ```bash
   source venv/bin/activate
   ```
2. Use the CLI commands:
   - Add new user:
     ```bash
     python3 cli.py new --name "Alice" --age 30
     ```
   - List users:
     ```bash
     python3 cli.py users
     ```
   - Show one user by id:
     ```bash
     python3 cli.py user 1
     ```
   - Update user by id (name and/or age):
     ```bash
     python3 cli.py update 1 --name "Alice New" --age 31
     ```
   - Delete user by id:
     ```bash
     python3 cli.py delete 1
     ```

## How it works

- `cli.py` defines commands with Click.
- `json_manager.py` reads and writes `data.json`.
- If `data.json` is missing, it is created automatically as `[]`.
- Each user is stored as a JSON object with `id`, `name`, `age`.

## Example workflow

```bash
python3 -m venv venv
source venv/bin/activate
pip install click
python3 cli.py new --name "Bob" --age 25
python3 cli.py users
python3 cli.py user 1
python3 cli.py update 1 --age 26
python3 cli.py delete 1
```

## Notes

- Always keep `venv` active when running the app.
- In the same terminal session, `deactivate` ends that environment.
- You can run `python cli.py --help` for help with commands.
