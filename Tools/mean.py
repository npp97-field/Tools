# ---------------------------------------------------------------------------
# mean.py
# Created on: 2014-11-17 12:51:28.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

path="D:\\AU\\SPEI\\mon\\no\\SPEI_"
outpath="D:\\AU\\SPEI\\year\\tab\\"

for n in xrange(2000,2014):
    n="%02d" % n

    # Local variables:
    NDVI_1 = path+n+"01.tif"
    NDVI_2 = path+n+"02.tif"
    NDVI_3 = path+n+"03.tif"
    NDVI_4 = path+n+"04.tif"
    NDVI_5 = path+n+"05.tif"
    NDVI_6 = path+n+"06.tif"
    NDVI_7 = path+n+"07.tif"
    NDVI_8 = path+n+"08.tif"
    NDVI_9 = path+n+"09.tif"
    NDVI_10 = path+n+"10.tif"
    NDVI_11 = path+n+"11.tif"
    NDVI_12 = path+n+"12.tif"
    mean_tif = outpath+n+"-mean.tif"
    max_tif = outpath+n+"-max.tif"
    min_tif = outpath+n+"-min.tif"
    range_tif = outpath+n+"-range.tif"
    std_tif = outpath+n+"-STD.tif"
    sum_tif = outpath+n+"-SUM.tif"
    # Process: Cell Statistics
    arcpy.gp.CellStatistics_sa([NDVI_1,NDVI_2,NDVI_3,NDVI_4,NDVI_5,NDVI_6,NDVI_7,NDVI_8,NDVI_9,NDVI_10,NDVI_12], sum_tif, "SUM", "DATA")
    arcpy.gp.CellStatistics_sa([NDVI_1,NDVI_2,NDVI_3,NDVI_4,NDVI_5,NDVI_6,NDVI_7,NDVI_8,NDVI_9,NDVI_10,NDVI_12], max_tif, "MAXIMUM", "DATA")
    arcpy.gp.CellStatistics_sa([NDVI_1,NDVI_2,NDVI_3,NDVI_4,NDVI_5,NDVI_6,NDVI_7,NDVI_8,NDVI_9,NDVI_10,NDVI_12], min_tif, "MINIMUM", "DATA")
    arcpy.gp.CellStatistics_sa([NDVI_1,NDVI_2,NDVI_3,NDVI_4,NDVI_5,NDVI_6,NDVI_7,NDVI_8,NDVI_9,NDVI_10,NDVI_12], mean_tif, "MEAN", "DATA")
    arcpy.gp.CellStatistics_sa([NDVI_1,NDVI_2,NDVI_3,NDVI_4,NDVI_5,NDVI_6,NDVI_7,NDVI_8,NDVI_9,NDVI_10,NDVI_12], range_tif, "RANGE", "DATA")
    arcpy.gp.CellStatistics_sa([NDVI_1,NDVI_2,NDVI_3,NDVI_4,NDVI_5,NDVI_6,NDVI_7,NDVI_8,NDVI_9,NDVI_10,NDVI_12], std_tif, "STD", "DATA")
    print n
 
