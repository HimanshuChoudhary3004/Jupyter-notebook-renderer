from IPython.display import display, IFrame
from ensure import ensure_annotations
import urllib.request
from jupyter_notebook_renderer.custom_exception import InvalidURLException
from jupyter_notebook_renderer.logger import logger
import warnings


@ensure_annotations
def is_valid(url: str) -> bool:
    try:
        response_status = urllib.request.urlopen(url).getcode()
        assert response_status == 200
        logger.debug(f"response status: {response_status}")
        return True
    except Exception as e:
        logger.exception(e)
        return False


@ensure_annotations
def render_site(url: str, width: str = "100%", height: str = "600") -> str:
    try:
        if is_valid(url):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = IFrame(src=url, width=width, height=height)
                display(response)
            return "success"
        else:
            raise InvalidURLException
    except Exception as e:
        raise e
