import os
import shapefile
from json import dumps


def shape2json(fname, outfile="states.json", country='Brazil'):
	reader = shapefile.Reader(fname)
	fields = reader.fields[1:]
	field_names = [field[0] for field in fields]

	data = []
	for sr in reader.shapeRecords():
		atr = dict(zip(field_names, sr.record))
		geom = sr.shape.__geo_interface__
		if country in sr.record[field_names.index('admin')]:
			name = sr.record[field_names.index('name')].decode('latin-1')
			if name in states:
				data.append(dict(type="Feature", geometry=geom, properties=atr))
			
	keys = ['abbrev', 'name', 'name_alt']
	for b in data:
		for key in keys:
			b['properties'][key] = b['properties'][key].decode('latin-1')

	with open(outfile, "w") as geojson:
		geojson.write(dumps({"type": "FeatureCollection",
							 "features": data}, indent=2) + "\n")


shape = 'estados.shp'
cartopy_cache = 'Documentos/2019-1/Datasma/codes/SHAPES/'
fname = os.path.join(os.path.expanduser('~'), cartopy_cache, shape)

shape2json(fname, outfile="states.json", country='Brazil')