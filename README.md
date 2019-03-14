# 微信表情包批量生成脚本

由于微信表情包要求太麻烦，写了个脚本批量搞定这些格式、尺寸、命名的问题。

## 代码说明

- cropfaces.py，批量裁切表情主图用的脚本，把表情原图都丢到 `faces` 目录存放即可
- cropmisc.py，批量裁切横幅、封面、引导图等，命名按 `misc` 目录的名字存放即可
- croputils.py，封装的保持宽高比、自动适应的裁切算法

经过裁切后，图片会保存到 `faces_cropped` 目录和 `misc_cropped` 目录。

## 尺寸列表

微信官方文档的说明不包括引导赞赏图和感谢图，下面这些就是上传微信表情全部的尺寸要求了。

| 素材名称     | 数量           | 格式      | 尺寸(像素)                              | 文件大小                                                     | 文件名        |
| ------------ | -------------- | --------- | --------------------------------------- | ------------------------------------------------------------ | ------------- |
| 表情主图     | 16/24          | GIF       | 240 x 240                               | 截屏表情/真人拍摄表情 ：不大于500KB 卡通表情及其它：不大于100KB | 脚本自动生成  |
| 表情缩略图   | 与主图数目一致 | PNG       | 表情专辑：120 X 120 表情单品：240 x 240 | 表情专辑：不大于50KB 表情单品：不大于60KB                    | 脚本自动生成  |
| 详情页横幅   | 1              | PNG或JPEG | 750 X 400                               | 不大于80KB                                                   | banner.jpg    |
| 表情封面图   | 1              | PNG       | 240 X 240                               | 不大于80KB                                                   | cover.png     |
| 聊天面板图标 | 1              | PNG       | 50 X 50                                 | 不大于30KB                                                   | chatpanel.png |
| 引导赞赏图片 | 1              | PNG       | 750 X 560                               | 随缘吧                                                       | payguide.jpg  |
| 赞赏感谢图片 | 1              | PNG       | 750 X 750                               | 随缘吧                                                       | thanks.jpg    |

个人意见，除了聊天面板图标因为需要做成透明，所以必须用 PNG，但其他的格式要求都是瞎 jb 扯淡，懂不懂压缩啊喂。

## 其他说明

代码实现就用到了 PIL 库，可以看下保持宽高比、自适应裁切的代码，感觉这种裁切需求很常见，但标准库里又没封装，以后应该用的比较多。

```python
from PIL import Image


# img is PIL Image
# size is like this (120,120)
def cropfit(img, newsize):
    curwidth, curheight = img.size
    curratio = curwidth / curheight
    tarratio = newsize[0] / newsize[1]
    # do crop
    if tarratio > curratio:
        tempsize = (curwidth, curwidth / tarratio)
        zeropoint = (0, (curheight - curwidth / tarratio) / 2)
    else:
        tempsize = (curheight * tarratio, curheight)
        zeropoint = ((curwidth - curheight * tarratio)/2, 0)
    tempimg = img.crop((
        zeropoint[0], zeropoint[1],
        zeropoint[0] + tempsize[0],
        zeropoint[1] + tempsize[1]))
    # do zoom
    finalimg = tempimg.resize(newsize, Image.ANTIALIAS)
    return finalimg

```

