from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView

from services.ts_squad import *

class MySquadView(TemplateView):
    # Target template
    template_name = 'mysquad/mysquad_home.html'

    # NOTE: Test squad will eventually be replaced with a way for users to input on the site
    squad = Squad()
    squad.initialize(TEST_SQUAD_LIST_01, DEF_MATCH_HISTORY_COUNT)

    sqData = squad.get_squad_data()
    extra_context = {'sqDATA' : sqData,
                     'ARAMAssWRs' : sqData["ARAM_highestWinrate_Assasin"],
                     'ARAMEncWRs' : sqData["ARAM_highestWinrate_Enchanter"],
                     'ARAMFigWRs' : sqData["ARAM_highestWinrate_Fighter"],
                     'ARAMMagWRs' : sqData["ARAM_highestWinrate_Mage"],
                     'ARAMMarWRs' : sqData["ARAM_highestWinrate_Marksman"],
                     'ARAMSupWRs' : sqData["ARAM_highestWinrate_Support"],
                     'ARAMTanWRs' : sqData["ARAM_highestWinrate_Tank"]}
    #data = json.dumps(EXE_META_DATA, indent=3)
    #print(data)
    

