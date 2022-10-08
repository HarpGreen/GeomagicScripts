import geomagic.app.v3
from geomagic.app.v3.imports import *

#################################################
path = "F:\\1耳朵测量项目\\5.特征提取\\TXT\\"	#在引号中输入保存TXT文件的路径，路径中的\需改成\\，且最后以\\结尾
#################################################

# Get the currently selected model in the model manager.
activeModel = geoapp.getActiveModel()

import time

def text(name, msg, pa):
    pa = pa + name + '.txt' 
    file = open(pa, 'a+')
    file.write(msg+"\n")
    file.close()

# Make sure there is a model selected.
if activeModel != None:
	planes = []
	features = geoapp.getFeatures(activeModel)
	p=path + str(activeModel.name) + '.txt'
	file = open(p, 'w')
	file.write("")
	print("\n\n输出完成!\n文件"+str(activeModel.name)+".txt已保存在"+path+"目录下！\n时间： "+time.strftime('%Y-%m-%d %H:%M:%S'))
	for feature in features:
		text(str(activeModel.name), str(feature.position.x()*1000), path) 
		text(str(activeModel.name), str(feature.position.y()*1000), path) 
		text(str(activeModel.name), str(feature.position.z()*1000), path) 
		if isinstance(feature, Plane):
			planes.append(feature)

else:
	print("No model selected")

