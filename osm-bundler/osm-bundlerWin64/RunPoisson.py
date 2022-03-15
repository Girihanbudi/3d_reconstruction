from datetime import datetime

start = datetime.now()

from surface_reconstruction import SurfaceReconstruction
import os

# Pass a method/library that contains a Poisson algorithm implementation
surface = SurfaceReconstruction(
  method_type='open3d',
  point_cloud_file="C:\\Users\\ghanb\\AppData\\Local\\Temp\\osm-bundler-i4vib_xc\\pmvs\\models\\pmvs_options.txt.ply",
  output_file="C:\\Users\\ghanb\\AppData\\Local\\Temp\\osm-bundler-i4vib_xc\\pmvs\\models\\model1.ply"
)

parameters = {
        'estimate_normals': [
            {
                'name': 'fast_normal_computation',
                'description': 'Fast normal estimation',
                'value': False
            },
            {
                'name': 'normals',
                'description': 'Points normals',
                'value': (1, 3)
            }
        ],
        'orient_normals_consistent_tangent_plane': [
            {
                'name': 'k',
                'description': 'Nearest neighbors',
                'value': 1000
            }
        ],
        'surface_reconstruction_screened_poisson': [
            {
                'name': 'depth',
                'description': 'Maximum depth of the tree',
                'value': 20
            },
            {
                'name': 'width',
                'description': 'Target width',
                'value': 50
            },
            {
                'name': 'scale',
                'description': 'Ratio between the diameter of the cube',
                'value': 1.1
            },
            {
                'name': 'linear_fit',
                'description': 'Use linear interpolation?',
                'value': False
            },
            {
                'name': 'n_threads',
                'description': 'Number of threads used for reconstruction',
                'value': -1
            }
        ]
    }

# Call the method from the specific library, and export a mesh file
surface.poisson_mesh()
# surface.poisson_mesh(**{'filters': parameters})

end = datetime.now()
print(end-start)