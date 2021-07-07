import arcpy, sys, os

arcpy.env.workspace = "..\DATN.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "DiaVat", df)[0]

#tdv = sys.argv[1]
if sys.argv[1] == '#':
    mdv = 0
else:
    mdv = sys.argv[1]

query = "DiaVat.MaDV LIKE '%{0}%'".format(mdv)
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)

del mxd