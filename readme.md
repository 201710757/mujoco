## install free version.  
python - 3.9   
pip install gym   
pip install free-mujoco-py   
sudo apt install libosmesa6-dev   
sudo apt install patchelf   
   
python -c "import mujoco_py"   

## Else Error
conda install -c conda-forge gcc=12.1.0
  
  
## GLEW Error   
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGL.so:/usr/lib/x86_64-linux-gnu/libGLEW.so   

## gym rom Error  
! wget http://www.atarimania.com/roms/Roms.rar   
! mkdir /content/ROM/   
! unrar e /content/Roms.rar /content/ROM/   
! python -m atari_py.import_roms /content/ROM/   
   

