import pytest


def test_response(api, api_assert):
    r = api.default_uniform()

    api_assert.assertResponse(r, 200)

    samples = r['samples']

    assert samples is not None

def test_data(api, api_assert):
    r = api.default_uniform()

    data = r['samples']

    assert len(data) == 10

def test_posivite(api, api_assert):
    r = api.default_uniform()

    data = r['samples']

    assert all([0 < d < 1 for d in data])
