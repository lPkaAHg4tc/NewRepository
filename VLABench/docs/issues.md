## Issue with using VLABench

### Issues with octo
Some experiences to create octo evaluation env:
```sh
    conda env remove -n octo
    conda create -n octo python=3.10
    conda activate octo
    pip install -e .
    pip install "jax[cuda12_pip]==0.4.20" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html flax==0.7.5 
    pip install tensorflow==2.15.0 pip install dlimp@git+https://github.com/kvablack/dlimp@5edaa4691567873d495633f2708982b42edf1972 
    pip install distrax==0.1.5 
    pip install tensorflow_probability==0.23.0 
    pip install scipy==1.12.0 
    pip install einops==0.6.1
    pip install transformers==4.34.1 
    pip install ml_collections==0.1.0 
    pip install wandb==0.12.14 
    pip install matplotlib 
    pip install gym==0.26 
    pip install plotly==5.16.1
    pip install orbax-checkpoint==0.4.0
```
Note: Line 5 "cuda12_pip" may be replaced by other proper version according to your machine. Refer to  [jax installation](https://jax.readthedocs.io/en/latest/installation.html#nvidia-gpu).

Make sure jax version=0.4.20 and flax version=0.7.5

    pip show jax flax jaxlib

Run this to verify installation successful

    python -c "from octo.model.octo_model import OctoModel; model = OctoModel.load_pretrained('hf://rail-berkeley/octo-base-1.5'); print('Model loaded successfully')"

### Failed to run VLABench on a headless server

To use the headless mode of MUJOCO, set the environment variable `MUJOCO_GL=egl`.

Please also make sure some neccessary libraries are successfully installed:
```sh
sudo apt-get install mesa-utils  
sudo apt-get install libglu1-mesa  
sudo apt-get install libgl1-mesa-dri  
sudo apt-get install libgl1-mesa-glx
```

### Issues about rlds generation
1. The error: got unexpected key `file_format`
Please refer to https://github.com/kpertsch/rlds_dataset_mod/issues/3

2. ValueError: Could not load DatasetBuilder from: xxx. Make sure the module only contains a single `DatasetBuilder'.
This issue is mainly because that the rlds relative environment lacks of some dependency packages.
To check these packages, you can build a new python file and load the tfds.builder from the target file.

For example, the builder file named `primitive.py` and the builder class is `Primitive`.
```
import tensorflow_datasets as tfds
from primitive import *

builder= Primitive()
```
Then the python will report the packages your environment doesn't have.

### Issues about Lerobot Version.
The lerobot conversion script is accomplished by referencing the openpi implementation. The openpi codebase VLABench used is [openpi](https://github.com/Shiduo-zh/openpi). Make sure the libary `datasets==3.2.0` when converting hdf5/rlds to lerobot format. Otherwise, there will be some incompatible problems. 