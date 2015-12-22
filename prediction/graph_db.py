from models import StockTable

def getObjects(stock_name):
    open_list =[]
    close_list = []
    low_list = []
    high_list = []
    date_list =[]
    stock_set = StockTable.objects.filter(company__exact=stock_name)
    if(stock_set.exists()):
        for stock_obj in stock_set:
            open_list.append(stock_obj.open)
            close_list.append(stock_obj.close)
            low_list.append(stock_obj.low)
            high_list.append(stock_obj.high)
            date_obj = str(stock_obj.date.day) + "." + str(stock_obj.date.month)  #+ "p" + str(stock_obj.date.month) + "p" + str(stock_obj.date.day)
            date_list.append(date_obj)

    return [open_list,close_list,low_list,high_list,date_list]

def getHigh_list():
    compHighDict ={}
    loop_count = 0
    comp = ""
    while(loop_count <=23):
        compHigh_list =[]
        stock_set = StockTable.objects.all()
        count = 0
        for stock_obj in stock_set:
            if(count == 12):
                break
            comp = stock_obj.company
            compHigh_list.append(stock_obj.high)
            count = count + 1
        compHighDict[comp] = compHigh_list
        loop_count = loop_count + 1
    return compHighDict
