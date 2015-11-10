// s is comprised of all different characters

from string import ascii_uppercase, ascii_lowercase
def check_flag(s):
	if len(s) != 25:
		return False
	s = list(s)
	if int(repr([s.pop(r) for r in [20, 17, 15, 13, 11, 2]][::-1])[2::5]) != 400003:
		return False
        t = [s.pop(r) for r in [7,3]]
	if s.index("h") != 2:
		return False
	y, z = [], []
	u = len(list(set([repr(y.append(s.pop(-1))) + repr(z.append(s.pop(-1))) for w in range(2)]))) - 1
	if u != len(list(set(y))) ^ len(list(set(z))):
		return False
	if (ord(y[u]) ^ ord(z[u])) ^ 0x1e != 0:
		return False
	if v.index(s.pop()) ^ len(s) ^ 0x1e != 0:
		return False
	a, i = filter(lambda c: c in v, s), filter(lambda c: c in k, s)
	if map(lambda a: a + 0x50, [7, 2, 4, -8]) + [0x4f] * 4 != map(ord, a):
		return False
	i[1:3] = i[2:0:-1]
	if i != list("hate"):
		return False
	return True
