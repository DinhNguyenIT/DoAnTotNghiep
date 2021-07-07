import arcpy, sys, os

arcpy.env.workspace = "..\DATN.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "NhaGV", df)[0]

#tdv = sys.argv[1]
if sys.argv[1] == '#':
    mnh = 0
else:
    mnh = sys.argv[1]

query = "NhaGV.MaNha LIKE '%{0}%'".format(mnh)
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)

del mxd