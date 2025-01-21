import pytest


def test_aus_ground():
    print("Looking good")

def test_aus_media():
    print("Asking a lot of question")

@pytest.mark.mediaTV
def test_aus_starSport():
    print("star sport Asking a lot of question")

def test_aus_series():
    print("test cricket")