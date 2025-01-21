import pytest


def test_ind_ground():
    print("Not Looking good")


def test_ind_media():
    print("Not Asking a lot of question")

@pytest.mark.xfail
def test_ind_starSport():
    print("India star sport asking a lot of question")

def test_ind_series():
    print("T20 cricket")