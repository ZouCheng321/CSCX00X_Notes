import math


time = 4015
seconds = time % 60
minutes = time // 60
hours = minutes // 60
minutes = minutes % 60
print(hours,'hours',minutes,'minutes',seconds,'seconds',sep='')

a = 5
b = 4
c = 6
angleC = math.acos((a*a+b*b-c*c)/(2*a*b))
area = 1/2*a*b*math.sin(angleC)
print(area)

