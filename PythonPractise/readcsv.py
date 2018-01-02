#coding=utf-8  
import xlwt  
import csv
file='./test.csv'
def read():
    data=list(csv.reader(open(file,'r')))
    length=len(data)
    data=data[0:1]+sorted(data[1:length])
    print(data) 
    return data 
def writeToexcel(data):
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('库存状态')
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            style0 = xlwt.XFStyle()
            print (data[i][j])
            if i==0:
                style0.pattern = setBackgroud(4)
                style0.font=setfont()
            elif j==1:
                #判断 状态是否为 '无货'
                if data[i][j+1]=='无货':
                    style0.pattern = setBackgroud(5)
                #价格是否为 '无货'
                elif data[i][j+2]=="":
                    style0.pattern = setBackgroud(2)    
            ws.write(i, j,data[i][j],style0)
    wb.save('test.xls')  
def setBackgroud(colour):
    pattern = xlwt.Pattern() # Create the Pattern
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = colour # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
    return pattern
def setfont():
    font = xlwt.Font()
    #font0.colour_index = 2
    font.bold = True
    return font
    
    
    
if __name__ == '__main__':
    data=read()
    writeToexcel(data)
    