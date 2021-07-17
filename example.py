
import deepzoom
# 输入文件
_TARGET_FILE = f"12786608.jpg"
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
