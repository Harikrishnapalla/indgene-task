# followed BY PEP-8
import pandas as pd
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.utils.translation import gettext as _

# Home
def home(request):
    # msg = _("home_page")
    return render(request, 'html/index.html')

# By using pandas
def exceldata(request):
    import os.path, json
    SITE_ROOT = os.path.abspath(os.path.dirname(__name__))
    a = os.path.join(SITE_ROOT,"files","Technical_assessment_source_data.xlsx")
    all_dfs = pd.read_excel(a, sheet_name=None, engine='openpyxl')
    data = list(all_dfs.keys())
    dt = len(data)
    json_str=""
    for x in range(dt):
        s = data[x]
        xls = pd.ExcelFile(a)
        df1 = pd.read_excel(xls, s)
        json_str += df1.to_json(orient='records')
    return HttpResponse(json_str.split())


# By using REST
@api_view()
def apidatas(request):
    import os.path
    SITE_ROOT = os.path.abspath(os.path.dirname(__name__))
    a = os.path.join(SITE_ROOT, "files", "Technical_assessment_source_data.xlsx")
    all_dfs = pd.read_excel(a, sheet_name=None, engine='openpyxl')
    data = list(all_dfs.keys())
    dt = len(data)
    l=[]
    for x in range(dt):
        s = data[x]
        xls = pd.ExcelFile(a) # file
        df1 = pd.read_excel(xls, s) # reading file
        df1.dropna(inplace=True) # if cell is 0. wont consider
        data_dict = df1.to_dict(orient='records') # coonverting list of dictionary
        l.append(data_dict)
    return Response({"data": l})






