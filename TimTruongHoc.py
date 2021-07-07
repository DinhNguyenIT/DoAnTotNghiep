import arcpy, sys, os

arcpy.env.workspace = "..\DATN.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "TruongHoc", df)[0]

#tdv = sys.argv[1]
if sys.argv[1] == '#':
    mth = 0
else:
    mth = sys.argv[1]

#ldv = sys.argv[2]
if sys.argv[2] == '#':
    tth = 0
else:
    tth = sys.argv[2]

query = "TruongHoc.MaTH LIKE '%{0}%' or TruongHoc.TenTH LIKE '%{1}%'".format(mth, tth)
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)

del mxd