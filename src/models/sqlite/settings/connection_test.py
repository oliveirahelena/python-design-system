from .connection import db_connection_handler


def test_connect_to_db():
    db_connection_handler.connect_to_db()
