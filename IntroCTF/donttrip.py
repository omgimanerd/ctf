points = sorted([[float(coord) for coord in line.split(',')] for line in open('DontTrip.csv', 'r').read().split('\n')])
y = [point[1] for point in points]
area = 0
i = 0
while i < len(y) - 1:
    if y[i + 1] == 0:
        print 'Area under line from point {0} ({1}) to point {2} ({3}): {4}'.format(i, y[i], i + 2, y[i + 2], (y[i + 2] + y[i]) / 2)
        area += (y[i + 2] + y[i]) / 2.0
        i += 2
    else:
        print 'Area under line from point {0} ({1}) to point {2} ({3}): {4}'.format(i, y[i], i + 1, y[i + 1], (y[i + 1] + y[i]) / 2)
        area += (y[i + 1] + y[i]) / 2.0
        i += 1
print area
