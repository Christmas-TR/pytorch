from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter('logs')
image_path = 'dataset/val/ants/10308379_1b6c72e180.jpg'
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)


writer.add_image('train',img_array,10,dataformats='HWC')

#for i in range(100):
    #writer.add_scalar('y = 6x',6*i,i)

writer.close()
