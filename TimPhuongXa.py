import arcpy, sys, os

arcpy.env.workspace = "..\DATN.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "PhuongXa", df)[0]

#tdv = sys.argv[1]
if sys.argv[1] == '#':
    mpx = 0
else:
    mpx = sys.argv[1]

query = "PhuongXa.MaPhuongXa LIKE '%{0}%'".format(mpx)
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)

del mxd