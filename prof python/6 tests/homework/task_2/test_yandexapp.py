import pytest
import fixtures
from yandexapp import YandexApi

#поставить свой токен
TOKEN = 'AQAAAAAJ-R0DAADLWzHHwCQoAU-6q05TNALMfEc'

my_example = YandexApi(TOKEN)
dir_count = my_example.disk_info()


@pytest.mark.parametrize('result', fixtures.fixture_create_dir)
def test_create_dir(result):
    assert my_example.create_dir() == result


def test_dir_count():
    assert my_example.disk_info() == dir_count + 1


@pytest.mark.parametrize('result', fixtures.fixture_remove_dir)
def test_remove_dir(result):
    assert my_example.remove_dir() == result
