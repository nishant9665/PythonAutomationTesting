import pytest
@pytest.mark.usefixtures('setup')
class Test_Login:

    def test_confMethod(self):
        print("This is conf method in pytest")
    def test_conf2Method(self):
        print("This is conf2 method in pytest")
    def test_failMethod(self):
        assert 2==3 , "this is not matched"