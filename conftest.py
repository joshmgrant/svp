import pytest
from samples.corsica_api import CorsicaAPI
from api_object import APIAssert


@pytest.fixture(scope="function")
def api(request):
    yield CorsicaAPI()

@pytest.fixture(scope="function")
def api_assert(request):
    yield APIAssert()
