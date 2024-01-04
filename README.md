# 3D Reconstruction Using SFM-PMVS-PSR

![image](https://github.com/Girihanbudi/3d_reconstruction/assets/41041312/3724b9a6-bb6d-4516-8636-9793b359a9cc)
![image](https://github.com/Girihanbudi/3d_reconstruction/assets/41041312/67a40f27-2d21-4525-9953-0d5fd00ec5a5)


This repository is to do 3D Reconstruction using OSM-Bundler(64 bit) todo SFM-MVS section and PoissonRecon from Adaptive Solvers to solve Surface Reconstruction

You can check their link here :
> OSM Bundler
> https://code.google.com/archive/p/osm-bundler/downloads

> Adaptive Solvers
> https://www.cs.jhu.edu/~misha/Code/PoissonRecon/Version13.74/

I tweak a code in OSM-Bundler a litte bit to be able to work on python 3

# How To Install
1. Clone this repository
2. Create virtual env in root project (or you can skip this)
3. Install used dependency in requirements.txt

# How To Use
You could test various option... RunBundler.py
Perform sparse point cloud and camera calibration :
```
python RunBundler.py --photos="path\to\your\images\folder"
# Example
python RunBundler.py --photos="dataset\sweater-p24"
```

After run bundler, temporary folder will be generated and you will get file need to do PMVS from SFM process. Use that folder as a path in PMVS or CMVS proses. In a second step you could compute the dense 3D point cloud in one step if the dataset have a reasonable size.
Perform PMVS :
```
python RunPMVS.py --bundlerOutputPath="path\to\temporary\folder"
# Example
python RunPMVS.py --bundlerOutputPath="path\to\temporary\osm-bundler-y777pm_2"
```

After run it, you will get a dense point cloud and you can generate 3d mesh through RunPSR.py
Perform PSR :
```
python RunPSR.py --bundlerOutputPath="path\to\temporary\folder\osm-bundler-y777pm_2"
# Example
python RunPSR.py --bundlerOutputPath="path\to\temporary\folder\Temp\osm-bundler-y777pm_2"
```
3D mesh will generated and you can open it with 3d software, I use meshlab to view the model. You can combine by your self the 3D mesh result with other adaptive solver function as you need

> Note : I use my camera phone to capture sample images in dataset folder, if you want to use your own camera. You can check cameras database in cameras.sqlite and see if your camera registered. If its not you can add it by your self. You can inspect your image exif metadata using exif pilot or whatever to check your camera model name.
