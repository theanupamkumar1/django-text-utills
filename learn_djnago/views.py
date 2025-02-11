#dev created file

from django.http import HttpResponse
from django.shortcuts import render

    
# def index(request):
#     return HttpResponse("""<h1><a href="https://example.com/tag1">Tag 1</a></h1>
#     <h2><a href="https://example.com/tag2">Tag 2</a></h2>
#     <h3><a href="https://example.com/tag3">Tag 3</a></h3>
#     <h4><a href="https://example.com/tag4">Tag 4</a></h4>
#     <h5><a href="https://example.com/tag5">Tag 5</a></h5>""")



def index(request):
    # return HttpResponse("home page")
    params = {'name':'anupam','place':'earth'}
    return render(request, 'index.html', params)


def analyze(request):
    text = request.POST.get('ip_text', '')
    analyzed_text = text
    capitalize = None
    smallcase = None
    removespaces = None
    rmpunct = None   
    style = None
    if request.POST.get('capitalize') == 'on':
        capitalize = analyzed_text.upper()
        
    if request.POST.get('smallcase') == 'on':
        smallcase = analyzed_text.lower()
        
    if request.POST.get('removespaces') == 'on':
        removespaces = "".join(analyzed_text.split())
        
    if request.POST.get('rmpunct') == 'on':
        rmpunct = ''.join(char for char in analyzed_text if char.isalnum() or char.isspace())
        
    if request.POST.get('style') == 'on':
        style = f'<span style="color:blue; font-size:20px; font-style:italic;">{analyzed_text.title()}</span>'
    
    params = {
        'original_text': text,
        # 'analyzed_text': analyzed_text,
        'length': len(text) if request.POST.get('length') == 'on' else None,
        'capitalize': capitalize,
        'smallcase': smallcase,
        'removespaces': removespaces,
        'rmpunct': rmpunct,
        'style': style,


    }
    
    return render(request, 'analyze.html', params)

# def capitlize(request):
#     dj_text=request.POST.get("ip_text",'default')
#     print(dj_text)
#     return render(request, 'capitalize.html')
# def smallcase(request):
#     return render(request, 'smallcase.html')
# def length(request):
#     return render(request, 'length.html')
# def style(request):
#     return render(request, 'style.html')
# def removespaces(request):
#     return render(request, 'removespaces.html')