import mapnik
m = mapnik.Map(256,256)
mapnik.load_map(m, 'data/phoenix.osm')
m.zoom_all()
mapnik.render_to_file(m, 'phoenix.png')