from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from mark import BASE_DIR, Path
from uuid import uuid4
from abc import abstractmethod
import base64
from loguru import logger
from utils.image_helpers import *


class TranscodingMixin:
    """
    用于处理图片的编解码
    """

    def base64_into_stream(self, string: str) -> bytes:
        """
        将 base64 编码的 image 变为字节流
        """
        stream: bytes = base64.b64decode(string)

        return stream

    def compress(self, raw_image: bytes) -> bytes:
        """
        压缩图片提体积，节约 GCS 的存储空间
        """
        return raw_image


class BaseBrowser(TranscodingMixin):
    def __init__(self, driver_path: Path):
        from selenium.webdriver.remote.webdriver import WebDriver
        from selenium.webdriver.common.service import Service

        self.driver: WebDriver
        self.service: Service
        self.driver.maximize_window()

    def snapshot(self, url: str) -> bytes:
        """
        截图
        """
        self.driver.maximize_window()
        self.driver.get(url)

        img: str = self.driver.get_screenshot_as_base64()
        png_stream: bytes = self.base64_into_stream(img)
        jpg_stream = png_stream_2_jpg_stream(png_stream, quality=50)

        return jpg_stream

    def close(self):
        try:
            self.driver.quit()
            self.service.stop()
        except Exception as error:
            logger.exception(error)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        try:
            self.close()
            logger.debug(f'浏览器已关闭')
        except Exception as error:
            logger.exception(error)


class ChromeBrowser(BaseBrowser):
    def __init__(self, driver_path: Path, proxy: tuple[str, int] | None = None):
        """
        代理的格式为 ip+port: ('149.28.24.224',60000)
        """
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.webdriver import WebDriver

        options = Options()
        # 设置代理
        options.add_argument(
            f'--proxy-server={proxy[0]}:{proxy[1]}') if proxy else ...

        # 其他参数
        options.add_argument(f'--headless')  # 无头模式
        options.add_argument(f'--no-sandbox')  # 容器中，如果用 root 跑，就要加这个
        options.add_argument(f'--window-size=1920,1080')  # 设置窗口大小

        # 创建浏览器对象

        self.service = Service(executable_path=driver_path)
        self.driver: WebDriver = webdriver.Chrome(
            service=self.service,
            options=options
        )

        super().__init__(driver_path)

    # def snapshot(self, url: str, is_compress: bool = False) -> bytes:
    #     return super().snapshot(url)


class FirefoxBrowser(BaseBrowser):
    def __init__(self, driver_path: Path):
        super().__init__(driver_path)

    # def snapshot(self, url: str, is_compress: bool = False) -> bytes:
    #     return super().snapshot(url)
