points = [{'x':2, 'y':3},
          {'x':4, 'y':1},
          {'x':4, 'y':10}]
points.sort(key=lambda i: i['y'])
print(points)
