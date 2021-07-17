# Python DZI 转码工具

## 说明

支持JPG，PNG，TIF,PhotoShop文件数据转码，转码目录为0-9,a-z二叉树目录结构。

## 安装说明
将deepzoom目录拷贝至工作目录内


## 依赖
```bash
Pillow==8.3.1  
psd-tools==1.9.17
```

## 示例说明

```bash
# 引入deepzoom
import deepzoom
# 输入文件
_TARGET_FILE = f"2.psb"
# deepzoom配置
creator = deepzoom.ImageCreator(
    tile_size=128,
    tile_overlap=2,
    tile_format="png",
    image_quality=0.8,
    resize_filter="bicubic",
)
# 生成主目录为release的二叉树目标目录，RELEASE_DIR可自定义
RELEASE_DIR = deepzoom.MakeStorgePath('release').make()
# 设置目录对象
creator.setsavepath(RELEASE_DIR)
# 生成DIZ文件，默认dzi文件为index.dzi
r = creator.create(_TARGET_FILE,'index.dzi')
# 返回目录URI
print(r)
```

## License

Power by:YeQing  
QQ:215777  
Version:1.0
