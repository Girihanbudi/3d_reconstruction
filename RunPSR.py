from datetime import datetime

start = datetime.now()

import subprocess
import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--bundlerOutputPath')
args=parser.parse_args()

print()


FNULL = open(os.devnull, 'w')
input = os.path.join(args.bundlerOutputPath, 'pmvs', 'models', 'pmvs_options.txt') 
output = input
depth = 8
args = str.format('AdaptiveSolvers\PoissonRecon --in {0}.ply --out {1}.pr.ply --depth {2}', input, output, depth)
subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

end = datetime.now()
print(end-start)
print('Check 3d mesh file in : bundler\output\path\pmvs\models\pmvs_options.txt.pr.ply')