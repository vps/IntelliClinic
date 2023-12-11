# scripts/init_db.py

from app.models import db
from app.utils.db_helpers import init_db
from config.settings import DATABASES

def main():
    # Set up the database
    db_uri = f"postgresql://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"
    db.init_app(db_uri)

    # Create tables
    init_db()

if __name__ == "__main__":
    main()
