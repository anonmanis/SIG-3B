import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal1.shp") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
sp = sf.shapes() # membaca shapes nya
anu = sp[0].shapeType # membaca shape type dari sp index 0
print(anu) # menampilkan isi dari variable anu