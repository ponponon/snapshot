from mark import BASE_DIR, Path
from loggers import logger
from browser import ChromeBrowser
from utils.time_helpers import get_utc_now_timestamp, custom_timestamp
import signal

# 加上这个可以避免出现 chromedriver 僵尸进程， 参考：https://www.jianshu.com/p/160a401eabb4
# signal.SIGCLD 在 Linux 上存在
signal.signal(signal.SIGCLD, signal.SIG_IGN)

driver_path: Path = BASE_DIR/'depends'/'chromedriver'


def snapshot(url: str) -> bytes:
    with ChromeBrowser(driver_path=driver_path) as browser:
        # 截图
        jpg_stream: bytes = browser.snapshot(url)
        logger.debug(f'获取截图, 大小为 {round(len(jpg_stream)/1024,3)} KBytes')
        return jpg_stream


if __name__ == '__main__':
    url = 'https://segmentfault.com/u/ponponon/articles'
    jpg_stream = snapshot(url)

    from storage import upload_snapshot

    upload_snapshot(jpg_stream, 'ponponon-host.jpg')
    
    logger.debug(f'上传文件到 minio')
