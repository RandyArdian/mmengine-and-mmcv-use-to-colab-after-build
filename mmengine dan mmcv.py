#masuk ke drive
from google.colab import drive
drive.flush_and_unmount()  # lepas
drive.mount('/content/gdrive', force_remount=True)

#masuk ke folder
%cd gdrive
%cd MyDrive/Riset

#karena sudah build maka tinggal buka lagi
#untuk mmengine
%cd mmengine
!pip install -e . -v

#untuk cv
%cd ..
%cd mmcv
!pip install -e .

#kedua proses tersebut sebentar
#langsung bisa pake librarynya
from mmengine.model import constant_init
from mmcv.cnn import build_activation_layer, build_norm_layer
from mmcv.ops.modulated_deform_conv import ModulatedDeformConv2d
# memetakan path agar bisa digunakan (wajib)
import sys
sys.path.append('/content/gdrive/MyDrive/Riset/mmcv')
sys.path.append('/content/gdrive/MyDrive/Riset/ultralytics')
sys.path.append('/content/gdrive/MyDrive/Riset/mmengine')

# melakukan jnstalasi pytorch agar kompatible dengan mmcv dan mmengine
!pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu126
#kedua library tersebut bisa dipanggil di modul ultralytics, sepeti contoh diatas.
#Randy_Ardiansyah_23_oktober_2025
