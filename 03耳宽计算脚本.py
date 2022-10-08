import geomagic.app.v3
from geomagic.app.v3.imports import *

import math

activeModel = geoapp.getActiveModel()

def getNor(p1, p2, p3):
   a = (p2.y() - p1.y())*(p3.z() - p1.z()) - (p2.z() - p1.z())*(p3.y() - p1.y())
   b = (p2.z() - p1.z())*(p3.x() - p1.x()) - (p2.x() - p1.x())*(p3.z() - p1.z())
   c = (p2.x() - p1.x())*(p3.y() - p1.y()) - (p2.y() - p1.y())*(p3.x() - p1.x())
   return Vector3D(a, b, c)

if activeModel != None:
   features = geoapp.getFeatures(activeModel)
   for feature in features:
      if feature.name == "点 2":
         pts2 = Points()
         pts2.addPoint(feature.position)
      if feature.name == "点 3":
         pts3 = Points()
         pts3.addPoint(feature.position)
      if feature.name == "点 4":
         pts4 = Points()
         pts4.addPoint(feature.position)
      if feature.name == "点 6":
         pts6 = Points()
         pts6.addPoint(feature.position)
      if feature.name == "点 16":
         pts22 = Points()
         pts22.addPoint(feature.position)
      if feature.name == "点 17":
         pts33 = Points()
         pts33.addPoint(feature.position)
      if feature.name == "点 18":
         pts44 = Points()
         pts44.addPoint(feature.position)
      if feature.name == "点 20":
         pts66 = Points()
         pts66.addPoint(feature.position)

   line36 = Line()
   line36.start = pts3.getPosition(0)
   line36.end = pts6.getPosition(0)

   line3366 = Line()
   line3366.start = pts33.getPosition(0)
   line3366.end = pts66.getPosition(0)

   plane4 = Plane()
   plane4.normal = line36.direction
   plane4.origin = pts4.getPosition(0)

   plane44 = Plane()
   plane44.normal = line3366.direction
   plane44.origin = pts44.getPosition(0)

   d2p4 = plane4.getDistance(pts2.getPosition(0))

   d22p44 = plane44.getDistance(pts22.getPosition(0))

   v346 = getNor(pts3.getPosition(0), pts4.getPosition(0), pts6.getPosition(0))

   v334466 = getNor(pts33.getPosition(0), pts44.getPosition(0), pts66.getPosition(0))

   plane4_ = Plane()
   plane4_.normal = v346
   plane4_.origin = pts4.getPosition(0)

   plane44_ = Plane()
   plane44_.normal = v334466
   plane44_.origin = pts44.getPosition(0)

   d2p4_ = plane4_.getDistance(pts2.getPosition(0))

   d22p44_ = plane44_.getDistance(pts22.getPosition(0))

   d2 = math.sqrt(d2p4**2 + d2p4_**2)

   d22 = math.sqrt(d22p44**2 + d22p44_**2)

   line24 = Line()
   line24.start = pts2.getPosition(0)
   line24.end = pts4.getPosition(0)

   line2244 = Line()
   line2244.start = pts22.getPosition(0)
   line2244.end = pts44.getPosition(0)

   d24 = line24.length

   d2244 = line2244.length

   result_L = math.sqrt(d24**2 - d2**2) * 1000

   result_R = math.sqrt(d2244**2 - d22**2) * 1000
   
   print("(面对的)左耳结果：\n" + str(result_L))

   print("(面对的)右耳结果：\n" + str(result_R))

else:
   print("No model selected")

