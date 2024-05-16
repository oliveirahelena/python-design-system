import pytest
from .connection import db_connection_handler


@pytest.mark.skip(reason="Database interation.")
def test_connect_to_db():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
