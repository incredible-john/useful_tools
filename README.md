# useful_tools
这个仓库保存一些常用的工具性代码，例如图片转视频、批量复制文件等。

以下是一些常用的命令：

1.列出一个文件夹下的所有图片
ls -R  /dir/*.ipg > file.txt 

2.Darknet Convertion

convert darknet cfg/weights to pytorch model

$ python3  -c "from models import *; convert('cfg/yolov3-spp.cfg', 'weights/yolov3-spp.weights')"

Success: converted 'weights/yolov3-spp.weights' to 'weights/yolov3-spp.pt'

convert cfg/pytorch model to darknet weights

$ python3  -c "from models import *; convert('cfg/yolov3-spp.cfg', 'weights/yolov3-spp.pt')"

Success: converted 'weights/yolov3-spp.pt' to 'weights/yolov3-spp.weights'
