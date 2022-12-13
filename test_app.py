import json
import app

def test_show_characters(api):
    res = api.get('/characters')
    assert res.json == ["Bob", "Jim"]

def test_create_character(api):
    mock_data = json.dumps({'name': 'Jeff'})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/character', data=mock_data, headers=mock_headers)
    assert res.text == "You have created a cat! It's called Jeff"