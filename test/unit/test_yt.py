import pytest
from jupyter_notebook_renderer import get_time_info
from jupyter_notebook_renderer.custom_exception import InvalidURLException


good_url_data = [
    ("https://www.youtube.com/watch?v=Y8KdR-AyyyA", 0),
    ("https://youtu.be/Y8KdR-AyyyA?feature=shared", 0),
    ("https://youtu.be/Y8KdR-AyyyA?feature=shared&t=60", 60),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&t=61s", 61)
]

bad_url_data = [
    ("https://www.youtube.com/watch?v==Y8KdR-AyyyyyyA"),
    ("https://youtu.be/Y8KdR-AyyyA?feature=shared&t"),
    ("https://youtu.be/Y8KdR-AyyyA?feature=shared&t==60"),
    ("https://www.youtube.com/watch?v==1-68pFs_HIE&t=61s")
]

@pytest.mark.parametrize("url,response", good_url_data)
def test_get_time_info(url, response):
    assert get_time_info(url) == response

@pytest.mark.parametrize("url", bad_url_data)
def test_get_time_info_failed(url):
    with pytest.raises(InvalidURLException):
        get_time_info(url)
