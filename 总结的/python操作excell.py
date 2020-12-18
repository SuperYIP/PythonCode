import xlwt
import xlrd
#创建excell冰箱其中写入数据
file = xlwt.Workbook(encoding = 'utf-8') #创建Workbook，设置字符编码为utf-8，默认是ascii
sheet = file.add_sheet('data',cell_overwrite_ok=True)	#创建一个sheet对象，一个sheet对应excell中的一张表
														#cell_overwrite_ok，表示是否可以覆盖单元格，默认值是False
sheet.write(0,1,'ss')	#向excell中写入数据，0：第0行，i：第一列，ss：写入的数据
for i in range(5):
	sheet.write(0,i,'test')	#此处又向0,1处写入了数据，如果cell_overwrite_ok不指定为True，会报错
file.save('F:\\学习相关\\大四上\\毕设\\数据\\t.xlsx')	#保存文件

#读取excell
workbook = xlrd.open_workbook('F:\\学习相关\\大四上\\毕设\\数据\\t.xlsx')  #打开excell文件，道理同写入
sheet2 = workbook.sheets()[0]	#获取excell的第一张表
rows = sheet2.nrows	#获取excell行数
cols = sheet2.ncols	#获取excell列数
print('行数为：%s'%rows)	#%s为占位符，输出行数
print('列数为：%s'%cols)
str1 = sheet2.cell_value(0,1)	#获取第0行，第一列数据
print(str1)