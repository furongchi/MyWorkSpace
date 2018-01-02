# _*_ coding:utf-8 _*_
import xlwt   

file='./case_log.txt'
actiondict={}

def count_average():
    averageList=[]
    for action in actiondict:
        sum=0.0
        for i in actiondict[action]:
            #print (i)
            sum+=i
        averagetime=round(sum/len(actiondict[action]),3)
        #print ('%s:%s'%(action,averagetime))
        averageList.append((len(actiondict[action]),averagetime,action))
    averageList.sort(reverse=True)
    #averageList=sorted(averageList)
    return averageList
        
def writeAvgTimeToexcel(data):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Action average time')
    ws.col(0).width = 5000
    ws.col(1).width = 4000
    ws.col(2).width = 4500
    for i in range(len(data)+1):
        style0 = xlwt.XFStyle()
        if i==0:
            style0.pattern = setBackgroud(4)
            ws.write(i,0,'ActionName',style0)
            ws.write(i,2,'AverageTime',style0)
            ws.write(i,1,'ExecuteTimes',style0)
            continue
        executeTimes,averagetime,actionname=data[i-1]
        if averagetime>=2.0:
            style0.pattern = setBackgroud(5)
        ws.write(i,0,actionname)
        ws.write(i,1,executeTimes)
        ws.write(i,2,averagetime,style0)
        
    wb.save('averageTime.xls')  
def setBackgroud(colour):
    pattern = xlwt.Pattern() # Create the Pattern
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = colour # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
    return pattern
    
def parseFile():
    f = open(file,mode='r+',encoding='UTF-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        if '[finished]' in line and 'ACTION' in line:
            #print (line)
            posStart=line.find('ACTION')+6
            posEnd=line.find('[finished]')
            action=line[posStart:posEnd].strip()
            #print(action)
            posDuration=line.find('duration=')
            posSec=line[posDuration+9:].find('sec')
            durationTime=line[posDuration+9:(posDuration+9+posSec)]
            #print(durationTime)
            if not action in actiondict:
                actiondict[action]=[]
            actiondict[action].append(float(durationTime))   
        f.write(line)
            
if __name__ == '__main__':
    parseFile()
    print (actiondict)
    averageList=count_average()
    print (averageList)
    writeAvgTimeToexcel(averageList)
    