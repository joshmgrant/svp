import pytest


def test_response(api, api_assert):
    r = api.default_normal()

    api_assert.assertResponse(r, 200)

    samples = r['samples']

    assert samples is not None

def test_length(api, api_assert):
    r = api.default_normal()

    data = r['samples']

    assert len(data) == 10

