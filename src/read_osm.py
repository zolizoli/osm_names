import shapefile
from os import listdir
from os.path import isfile, join

in_path = 'data'
out_path = 'geo_data'

shps = [f for f in listdir(in_path) if isfile(join(in_path, f))]
shps = [f for f in shps if f.endswith('.shp')]

of = open(join(out_path, 'hungarian_geonames.tsv'), 'w')
h = 'Id\tLocation\tType\n'
of.write(h)

i = 0
for shp in shps:
    shape = shapefile.Reader(join(in_path, shp))
    fields = shape.fields[1:]
    field_names = [field[0] for field in fields]
    for r in shape.shapeRecords():
        atr = dict(zip(field_names, r.record))
        location_type = atr['fclass']
        location_name = atr['name']
        if len(location_name) > 3:
            o = str(i).zfill(5) + '\t' + location_name + '\t' + location_type + '\n'
            of.write(o)
            i += 1
