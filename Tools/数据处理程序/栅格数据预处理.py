# ---------------------------------------------------------------------------
# 功能：1、统计栅格信息
#       2、对栅格数据进行投影
#		3、提取出LAI栅格中”<100"的有效值
# Created on: 星期日 十二月 18 2011 02:37:43 下午
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

#循环开始
for n in xrange(2001,2010):
#	for m in xrange(1,13):
#		m=range(1,13)
#		m="%02d" % m
		i=0
		for d in xrange(1,365,8):
			d="%03d" % d
##########################-----操作目录---------##############################################
			input_mulu="D:\\MODIS_LAI\\"		#输入TIF文件目录		
			out_mulu="d:\\output\\linshi\\"	#输出有效值文件目录
			out_mulu_lai="D:\\\WASSI\\\ChangJiang\\"	#输出LAI计算结果目录
			input_mulu_basin="D:\\WASSI\\ChangJiang\\VEG_CJ\\"
##########################-----输入文件---------##############################################
			input_tif = input_mulu+"MOD15A2.A"+str(n)+d+".Lai_1km.tif"  
			output_extra = out_mulu+"MOD15A2.A"+str(n)+d+".Lai_1km.extra.tif"	#提取后输出的tif文件
			
##########################-----输入basin文件---------##############################################			
			
			
			print output_extra,output_data_basin_1,input_basin_1
# Process: 计算统计数据
			arcpy.CalculateStatistics_management(input_tif, "1", "1", "")
			print "成功统计栅格信息！"
			
# Process: 重新定义投影到Albers定义投影
			arcpy.DefineProjection_management(input_tif, "PROJCS['Albers',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',105.0],PARAMETER['Standard_Parallel_1',25.0],PARAMETER['Standard_Parallel_2',47.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")
			print "定义投影为albers！"
			
# Process: Extract by Attributes...
			arcpy.gp.ExtractByAttributes_sa(input_tif ,"\"value\" < 100 ", output_extra)
			print "成功提取出“<100“的值！"
			

