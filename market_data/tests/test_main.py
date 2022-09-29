"""Market Data Api Main Tests."""
from main import dummy_function


class TestMain:
    def test_main(self):
        resp = dummy_function()
        assert resp == 1
