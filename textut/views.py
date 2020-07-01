# I have created this file - Aditi
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Adi', 'place': 'Earth'}
    return render(request, 'index2.html', params)
    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    # checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    lowercase = request.GET.get('lowercase', 'off')

    # print(djtext)
    # print(removepunc)

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_`~||='''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return HttpResponse("remove punc")
        # return render(request, 'analyze.html', params)

    # CHECK IF fullcaps IS ON
    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    # CHECK IF lowercase IS ON
    if lowercase == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Convert to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed


    # Check if newlineremover is on
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}



    #  Count the no of characters
    if charcount == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'The No of characters are', 'analyzed_text': analyzed}
        djtext = analyzed



    if removepunc != "on" and fullcaps != 'on' and charcount != 'on' and lowercase != 'on' and newlineremover != 'on' and extraspaceremover == "on":
        return HttpResponse("Error! no operation selected")

    return render(request, 'analyze.html', params)

