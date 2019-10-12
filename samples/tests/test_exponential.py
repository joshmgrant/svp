import pytest


def test_response(api, api_assert):
    r = api.default_exponential()

    api_assert.assertResponse(r, 200)

    samples = r['samples']

    assert samples is not None

def test_data(api, api_assert):
    r = api.default_exponential()

    data = r['samples']

    assert len(data) == 10

def test_posivite(api, api_assert):
    r = api.default_exponential()

    data = r['samples']

    assert all([d > 0 for d in data])
