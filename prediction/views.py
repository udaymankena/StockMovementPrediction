from django.shortcuts import render

import graph_db
from .forms import StockForm
from Sentiment.buildClassifier import getAnalysis

# Create your views here.
points = {}
def index(request):
    global points
    if request.method == 'POST':
        stock_form = StockForm(request.POST)

        if stock_form.is_valid():
            data = stock_form.cleaned_data
            stock_name = data['stock_name']
            total_list = graph_db.getObjects(stock_name)
            result = getAnalysis(stock_name)
            decision = ""
            if(result['sentiment'] == 'positive'):
                decision = "Safe to Invest on " + stock_name
            else:
                decision = "Better not to Invest on " + stock_name + "at this time"

            points = {
                'stock_name':stock_name,
                'open_list': total_list[0],
                'close_list': total_list[1],
                'low_list': total_list[2],
                'high_list': total_list[3],
                'date_list': total_list[4],
                'gen_pos_percent':int(result['gen_pos_percent']),
                'gen_neg_percent':int(result['gen_neg_percent']),
                'anal_pos_percent':int(result['anal_pos_percent']),
                'anal_neg_percent':int(result['anal_neg_percent']),
                'sentiment': result['sentiment'],
                'decision': decision
            }

        return render(request, "analysis.html", points)
    else:
        stock_form = StockForm()

    return render(request, 'index.html', {'stock_form':stock_form})

def accessform(request):
    return render(request,"visualization2.html",points)