import shapefile
w=shapefile.Writer('Soal10', shapeType=shapefile.POLYGON)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.record("crot","dua")
w.record("ngok","tiga")
w.record("nguk","empat")
w.record("wawawa","lima")
w.poly([[[8,2],[12,2],[12,3],[8,3],[8,2]]])
w.poly([[[8,4],[12,4],[12,5],[8,5],[8,4]]])
w.poly([[[2,2],[6,2],[6,3],[2,3],[2,2]]])
w.poly([[[2,4],[6,4],[6,5],[2,5],[2,4]]])
w.poly([[[5,6],[9,6],[9,7],[5,7],[5,6]]])
w.close()