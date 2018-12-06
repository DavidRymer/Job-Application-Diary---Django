from django.shortcuts import render
from JobDiary.scraper import milkroundscraper

records = []


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})


def search(request):

    a = request.GET.get('q', "")
    print(a)

    if a is not "":
        credentials = milkroundscraper.MilkroundScraper(a).get_credentials()
        if credentials not in records:
            credentials.append(a)
            records.append(credentials)
    print(records)

    return render(request, 'personal/basic.html',
                  {'records': records,
                   'range': range(0, len(records)),
                   })

