import pytest
from jupyter_notebook_renderer.custom_exception import InvalidURLException
from jupyter_notebook_renderer import render_youtube_video
import warnings


@pytest.mark.filterwarnings(
    "always:Importing display from IPython.core.display is deprecated", action="record"
)
class TestYTvideorenderer:
    URL_test_sucess_data = [
        ("https://www.youtube.com/watch?v=AZ29DXaJ1Ts", "success"),
        ("https://youtu.be/AZ29DXaJ1Ts?feature=shared", "success"),
        ("https://youtu.be/AZ29DXaJ1Ts?feature=shared&t=60", "success"),
        ("https://www.youtube.com/watch?v=AZ29DXaJ1Ts&t=60s", "success"),
        ("https://youtu.be/AZ29DXaJ1Ts?feature=shared10", "success"),
    ]

    URL_test_bad_data = [
        ("https://www.youtube.com/watch?v=AZ29DddXaJ1Ts"),
        ("https://youtu.be/AZ29DXaJ1Ts?feature=shared&t=60_"),
        ("https://www.youtube.com/watch?v==AZ29DXaJ1Ts&t=60s"),
    ]

    @pytest.mark.parametrize("url,response", URL_test_sucess_data)
    def test_render_yt_sucess(self, url, response):
        assert render_youtube_video(url) == response

    @pytest.mark.parametrize("url", URL_test_bad_data)
    def test_render_yt_failed(self, url):
        with pytest.raises(InvalidURLException):
            render_youtube_video(url)
