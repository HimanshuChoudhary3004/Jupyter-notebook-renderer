from IPython import display
from ensure import ensure_annotations
from jupyter_notebook_renderer.custom_exception import InvalidURLException
from jupyter_notebook_renderer.logger importlogger
from py_youtube import Data


@ensure_annotations
def get_time_info(url: str)->int:
    def _verify_vid_id_len(vid_id,_expected_len=11):
        vid_id_len=len(vid_id)
        if vid_id_len!=_expected_len:
            raise InvalidURLException(f"Invalid video id with length :{vid_id_len}, expected video id length is {_expected_len}")
    
    try:
        split_val=url.split('=')
        if "watch" in url:
            if ("&t" in url):
                vid_id,time=split_val[-2][:-2]
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at {time}")
                return time
            else:
                vid_id,time=split_val[-1],0
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at {time}")
                return time
        else:
            


@ensure_annotations
def render_youtube_video(url:str,width: int=780,height: int=160) -> str:
    try:
        if url is None:
            raise InvalidURLException("URL can not be empty")
        data=Data(url).data()
        if data["publishdate"] is not None:
            time=get_time_info(url)
            vid_ID=data["id"]
            embeded_url=f"https:/www.youtube.com/embed/{vid_ID}?start={time}"
            logger.info(f"embed url : {embed_url}")

            iframe = f"""<iframe 
            width="{width}" height="{height}" 
            src="embeded_url" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; clipboard-write; 
            encrypted-media; gyroscope; 
            picture-in-picture; web-share" allowfullscreen>
            </iframe> """

            display.display(display.HTML(iframe))
            return "success"
        pass
    except Exception as e:
        raise e