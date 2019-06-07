###爬取含有图片的网页流程
1.导入模块
from scrapy .pipelines.images import ImagePipeline

2.自定义类，继承ImagePipeline
```python
class DouyuImagePipeline(ImagePipeline):
    # 重写get_media_requests方法
    def get_media_requests(self,item,info):
    
    yield scrapy.Request(url = item['link'])
    
```
3.在setting.py中添加参数
IMAGE_STORE = "PATH"

4.dont_filter参数：
```python
scrapy.Request(url,callback=self.parse,dont_filter = False)
#不去重
```
