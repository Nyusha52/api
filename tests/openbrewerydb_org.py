from jsonschema import validate

import pytest
import requests


def test_new_post():
    res = requests.post('https://jsonplaceholder.typicode.com/posts')

    schema = {"type": ['object'],
              "id": {"type": "string"},
              "name": {"type": "string"},
              'address_2': {"type": "string"},
              'address_3': {"type": "string"},
              'city': {"type": "string"},
              'brewery_type': {"type": "string"},
              'street': {"type": "string"},
              'state': {"type": "string"},
              'county_province': {"type": "string"},
              'postal_code': {"type": "string"},
              'country': {"type": "string"},
              'longitude': {"type": "string"},
              'latitude': {"type": "string"},
              'phone': {"type": "string"},
              'website_url': {"type": "string"},
              'updated_at': {"type": "string"},
              'created_at': {"type": "string"},
              "required": ["id", "name", "street", 'phone']
              }
    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize('input_count, expected_count',
                         [('san_diego', 'san diego'),
                          ('fayetteville', 'fayetteville'),
                          ('windsor', 'windsor')
                          ])
def test_filter_sity(input_count, expected_count):
    res = requests.get('https://api.openbrewerydb.org/breweries?by_city={}'.format(input_count))
    d = res.json()
    assert res.status_code == 200
    for i in range(len(d)):
        assert expected_count in d[i]['city'].lower()


@pytest.mark.parametrize('input_count, expected_count',
                         [('micro', 'micro'),
                          ('large', 'large'),
                          ('closed', 'closed')
                          ])
def test_filter_type(input_count, expected_count):
    res = requests.get('https://api.openbrewerydb.org/breweries?by_city={}'.format(input_count))
    d = res.json()
    assert res.status_code == 200
    for i in range(len(d)):
        assert expected_count in d[i]['brewery_type']


@pytest.mark.parametrize('input_count, expected_count',
                         [('west_virginia', 'west virginia'),
                          ('california', 'california'),
                          ('florida', 'florida')
                          ])
def test_filter_state(input_count, expected_count):
    res = requests.get('https://api.openbrewerydb.org/breweries?by_state={}'.format(input_count))
    d = res.json()
    assert res.status_code == 200
    for i in range(len(d)):
        assert expected_count in d[i]['state'].lower()


@pytest.mark.parametrize('input_count, expected_count',
                         [('dog', 'dog'),
                          ('cat', 'cat'),
                          ('closed', 'closed')
                          ])
def test_filter(input_count, expected_count):
    res = requests.get('https://api.openbrewerydb.org/breweries/autocomplete?query={}'.format(input_count))
    d = res.json()
    assert res.status_code == 200
    for i in range(len(d)):
        assert expected_count in d[i]['name'].lower()
