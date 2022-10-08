import geomagic.app.v3
from geomagic.app.v3.imports import *

N = 27
path = "I:\\OneDrive - Albert\\1耳朵测量项目\\"	#在引号中输入保存TXT文件的路径，路径中的\需改成\\，且最后以\\结尾
#################################################

activeModel = geoapp.getActiveModel()

def CreatePF(num, px, py, pz):
   pt = PointFeature()
   pt.name = str(num)
   pt.initialize(Vector3D(px, py, pz))

   geoapp.addFeature(activeModel, pt)

fname = path + str(activeModel.name) + '.txt'
f = open(fname, "r")

i = 1

while i <= N:

   line = f.readline()
   line = line[:-1]

   x = float(line)/1000

   line = f.readline()
   line = line[:-1]

   y = float(line)/1000

   line = f.readline()
   line = line[:-1]

   z = float(line)/1000

   CreatePF(i, x, y, z)
   i = i + 1

print("\n\n输入完成!")

f.close()

