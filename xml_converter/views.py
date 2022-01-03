from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.xmltojson import XMLToJson


def upload_page(request):

    if request.method == 'POST':
        xmlfile = request.FILES.get('file')
        if xmlfile:
            parser = XMLToJson(xmlfile)
            return JsonResponse(parser.result)
       
    return render(request, "upload_page.html")
