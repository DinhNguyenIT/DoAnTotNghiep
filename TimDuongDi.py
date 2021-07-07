import arcpy, sys, os

arcpy.env.workspace = "..\DATN.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "DuongDi", df)[0]

#tdv = sys.argv[1]
if sys.argv[1] == '#':
    mdd = 0
else:
    mdd = sys.argv[1]

query = "DuongDi.MaDuong1 LIKE '%{0}%'".format(mdd)
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)

del mxd