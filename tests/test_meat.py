from dotenv import load_dotenv

from api.meat import do_something


def test_meat_response():
    # Test main functionality disconnected from endpoints
    result = do_something("test")
    assert result
    assert isinstance(result, str)
