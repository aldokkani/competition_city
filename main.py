import csv

with open('cities.csv') as f:
    cities = [city for city in csv.DictReader(f)]

with open('points.csv') as f:
    points = []
    for point in csv.DictReader(f):
        for city in cities:
            city_xrange = range(int(city['TopLeft_X']), int(city['BottomRight_X']) + 1)
            city_yrange = range(int(city['TopLeft_Y']), int(city['BottomRight_Y']) + 1)
            if int(point['X']) in city_xrange and int(point['Y']) in city_yrange:
                point['City'] = city['Name']
                break
        if point.get('City') is None:
            point['City'] = 'None'
        points.append(point)

with open('output_points.csv', 'w') as f:
    fieldnames = ['ID', 'X', 'Y', 'City']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(points)
