Perform point cloud and camera calibration :
$ RunBundler.py --photos="./examples/MyPhotos" 
===
python RunBundler.py --photos="C:\Users\ghanb\OneDrive\Documents\development\3d_reconstruction\osm-bundler\examples\kermit"


You could test various option... $ RunBundler.py

In a second step you could compute the dense 3D point cloud in one step if the dataset have a reasonable size.

$ RunPMVS.py --bundlerOutputPath="C:/temp/PreviousLineTempDirectoryPath"
RunPMVS.py --bundlerOutputPath="C:\Users\ghanb\AppData\Local\Temp\osm-bundler-tnpa25o7" 

If you have a lot of images, it better to use CMVS cluster computation.
It performs dense 3D point could computation by using Cluster 3D representation of the scene :

$ RunCMVS.py --bundlerOutputPath="C:/temp/PreviousLineTempDirectoryPath" --ClusterToCompute ="Number of Desired Cluster".
Example :
$ RunCMVS.py --bundlerOutputPath="C:/temp/osm-Result" --ClusterToCompute ="10".
"