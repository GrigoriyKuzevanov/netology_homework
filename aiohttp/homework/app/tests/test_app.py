import requests

from tests.config import API_URL


def test_root():
    assert requests.get(API_URL).status_code == 404

def test_get_adv_not_exists():
    resp = requests.get(f'{API_URL}/advs/10000000')
    assert resp.status_code == 404
    assert resp.json() == {'Status': 'error', 'description': 'adv not found'}


def test_get_adv_exists(create_adv):
    adv_id = create_adv['id']
    resp = requests.get(f'{API_URL}/advs/{adv_id}')
    assert resp.status_code == 200
    adv = resp.json()
    assert create_adv['header'] == adv['header']
    assert create_adv['id'] == adv['id']
    assert create_adv['description'] == adv['description']
    assert create_adv['owner'] == adv['owner']
    
def test_create_adv():
    resp = requests.post(
        f'{API_URL}/advs/',
        json={
            'header': 'test_create_header',
            'description': 'test_create_description',
            'owner': 'test_create_owner'
        }
    )
    assert resp.status_code == 200
    adv_post_data = resp.json()
    assert 'id' in adv_post_data
    assert isinstance(adv_post_data['id'], int)
    assert adv_post_data['header'] == 'test_create_header'
    assert adv_post_data['description'] == 'test_create_description'
    assert adv_post_data['owner'] == 'test_create_owner'

def test_create_adv_2():
    resp = requests.post(
        f'{API_URL}/advs/',
        json={
            'header': 'test_create_header',
            'description': 'test_create_description',
            'owner': 'test_create_owner'
        }
    )
    assert resp.status_code ==  409
    assert resp.json() == {
        'status': 'error',
        'description': 'adv already exists'
    }

def test_patch_adv(create_adv):
    adv_id = create_adv['id']
    resp = requests.patch(
        f'{API_URL}/advs/{adv_id}',
        json={
            'header': 'test_patch_header',
            'owner': 'test_patch_owner'
        }
    )
    assert resp.status_code == 200
    assert resp.json() == {'patch status': 'success'}
    resp = requests.get(f'{API_URL}/advs/{adv_id}')
    assert resp.status_code == 200
    adv_header = resp.json()['header']
    adv_owner = resp.json()['owner']
    assert adv_header == 'test_patch_header'
    assert adv_owner == 'test_patch_owner'

def test_delete_adv(create_adv):
    adv_id = create_adv['id']
    resp = requests.delete(f'{API_URL}/advs/{adv_id}')
    assert resp.status_code == 200
    assert resp.json() == {'delete status': 'success'}
    resp = requests.get(f'{API_URL}/advs/{adv_id}')
    assert resp.status_code == 404
    assert resp.json() == {'Status': 'error', 'description': 'adv not found'}
