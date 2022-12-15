import matplotlib.pyplot as plt
import numpy as np
import api
import math
import time

pos = (250, 150)
face = math.pi / 4
rad = 20
d0 = 7

def go(fwd, step = 10):
	global pos
	dy = math.cos(fwd) * step
	dx = math.sin(fwd) * step

	x, y = int(dx + pos[0] + 0.5), int(dy + pos[1] + 0.5)
	if api.hit((x, y)):
		print('go Failed.')
		return False
	else:
		pos = (x, y)
		return True

def goPos(fwd, step = 10):
	dy = math.cos(fwd) * step
	dx = math.sin(fwd) * step

	x, y = int(dx + pos[0] + 0.5), int(dy + pos[1] + 0.5)
	return (x, y)

def getDis():
	faceNew = api.fitAngle(face + math.pi / 2)
	return api.getD(pos, faceNew)

def adjustAngle():
	global face
	face = api.fitAngle(face - api.hitAngle(pos))
	ar = np.linspace(-math.pi / 20, math.pi / 20, 40)

	best, di = 20, 1000
	for ag in ar:
		ft = api.fitAngle(face + ag)
		qwq = abs(d0 - api.maxDis(goPos(step = 10, fwd = ft)))
		if qwq < di:
			best = ft
			di = qwq

	face = best
	print('face is {}'.format(face))

colors = ['b', 'b', 'b', 'b']
def main():
	global face
	# Ts = time.clock()
	# plt.show()
	for index in range(20):
		# if time.clock() - Ts >= 1000:
		# 	break
		face = np.random.uniform(low = -math.pi, high = math.pi)
		print(pos, face, goPos(fwd = face), api.hit(goPos(fwd = face)))

		while not api.hit(goPos(fwd = face, step = 11)):
			print('before go, pos = {0}, face = {1}'.format(pos, face))
			go(fwd = face)
			print('after go, pos = {}'.format(pos))
			plt.plot(pos[0], pos[1], '{}.-'.format(colors[index % 4]))

		for fasdfdsa in range(10 ** 9):
			print(pos)
			adjustAngle()
			faceSide = api.fitAngle(face + math.pi / 2)

			if getDis() > 1.5 * d0:
				go(step = 3, fwd = faceSide)
			elif getDis() < 0.5 * d0:
				go(step = 3, fwd = api.fitAngle(faceSide + math.pi))

			plt.plot(pos[0], pos[1], '{}.-'.format(colors[index % 4]), linewidth = 3)
			status = go(fwd = face, step = 10)
			if not status:
				break


	plt.show()


main()

# face = np.random.uniform(low = -math.pi, high = math.pi)
# print('pos = {0}, face = {1}, next pos = {2}'.format(pos, face, goPos(face)))
# plt.show()