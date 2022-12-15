import matplotlib.pyplot as plt
import numpy as np
import math

imgPath = '2.png'
img = plt.imread(imgPath)

def dist(pa, pb):
	return ((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2) ** 0.5

def val(x, y):
	try:
		return 1 - int(img[y, x, 0])
	except:
		return 1

def getD(pos, angle):
	slope = math.tan(abs(angle))
	marker = 1

	if angle < 0:
		marker = -1

	for i in range(500):
		x = pos[0] + i * marker
		y = pos[1] + i * slope
		x, y = int(x), int(y)
		# print(x, y)
		if val(x, y) == 1:
			print(x, y)
			return dist(pos, (x, y))

def hit(pos):
	if val(pos[0], pos[1]) == 1:
		return True
	else:
		return False

def at(p1, p2):
	if p1[1] == p2[1]:
		return 10 ** 9 * ((p2[0] - p1[0]) // abs(p1[0] - p2[0]))

	# print((p2[0] - p1[0]) / (p1[1] - p2[1]))
	tmp = math.atan((p2[0] - p1[0]) / (p1[1] - p2[1]))
	if (p2[0] < p1[0]):
		if tmp > 0:
			tmp = tmp - math.pi
	else:
		if tmp < 0:
			tmp = tmp + math.pi

	return tmp

def maxDis(pos):
	res, dis = (0, 0), 114514

	for i in range(max(0, pos[0] - 40), min(500, pos[0] + 40)):
		for j in range(max(0, pos[1] - 40), min(300, pos[1] + 40)):
			if val(i, j) == 1 and dist((i, j), pos) < dis:
				dis = dist((i, j), pos)
				res = (i, j)

	return dis

def hitAngle(pos):
	res, dis = (0, 0), 114514

	for i in range(max(0, pos[0] - 40), min(500, pos[0] + 40)):
		for j in range(max(0, pos[1] - 40), min(300, pos[1] + 40)):
			if val(i, j) == 1 and dist((i, j), pos) < dis:
				dis = dist((i, j), pos)
				res = (i, j)
	
	print('hitAngle = {}'.format(at(pos, res)))
	return at(pos, res)
	# return (res,at(pos, res))

def fitAngle(angle):
	return (angle + math.pi) % (2 * math.pi) - math.pi

def mark(pos):
	img[pos[1], pos[0],:] = np.array([0., 0., 0., 1.])

plt.imshow(img)
print(getD((300, 150), (math.pi / 6)))
print(hitAngle((375, 190)))
# plt.show()
