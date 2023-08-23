from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView

from services.ts_squad import *

class MySquadSubmission(TemplateView):
    template_name = 'mysquad/mysquad_submit.html'

class MySquadView(TemplateView):
    # Target template
    template_name = 'mysquad/mysquad_home.html'

    # NOTE: Test squad will eventually be replaced with a way for users to input on the site
    squad = Squad()
            #MIN_MATCH_HISTORY_COUNT = "0"
            #REC_MATCH_HISTORY_COUNT = "90"
            #MAX_MATCH_HISTORY_COUNT = "100"
            #DEF_MATCH_HISTORY_COUNT = "20"
    squad.initialize(TEST_SQUAD_LIST_3, DEF_MATCH_HISTORY_COUNT)

    # ADD FUNCTION TO CHECK FOR NEW CHAMPIONS.
    sqData = squad.get_squad_data()
    extra_context = {'sqDATA' : sqData,
                     'ARAMTotal' : sqData["ARAM_matchesPlayed"],
                     'ARAMWon' : sqData["ARAM_matchesWon"],
                     'ARAMLost' : sqData["ARAM_matchesLost"],
                     'ARAMWR' : sqData["ARAM_winrate"],
                     'ARAMAssWRs' : sqData["ARAM_highestWinrate_Assasin"],
                     'ARAMEncWRs' : sqData["ARAM_highestWinrate_Enchanter"],
                     'ARAMFigWRs' : sqData["ARAM_highestWinrate_Fighter"],
                     'ARAMMagWRs' : sqData["ARAM_highestWinrate_Mage"],
                     'ARAMMarWRs' : sqData["ARAM_highestWinrate_Marksman"],
                     'ARAMTanWRs' : sqData["ARAM_highestWinrate_Tank"],
                     'SRTotal' : sqData["SR_matchesPlayed"],
                     'SRWon' : sqData["SR_matchesWon"],
                     'SRLost' : sqData["SR_matchesLost"],
                     'SRWR' : sqData["SR_winrate"],
                     'SRAssWRs' : sqData["SR_highestWinrate_Assasin"],
                     'SREncWRs' : sqData["SR_highestWinrate_Enchanter"],
                     'SRFigWRs' : sqData["SR_highestWinrate_Fighter"],
                     'SRMagWRs' : sqData["SR_highestWinrate_Mage"],
                     'SRMarWRs' : sqData["SR_highestWinrate_Marksman"],
                     'SRTanWRs' : sqData["SR_highestWinrate_Tank"],
                     'SRBotWRs' : sqData["SR_highestWinrateBot"],
                     'SRJunWRs' : sqData["SR_highestWinrateJung"],
                     'SRMidWRs' : sqData["SR_highestWinrateMid"],
                     'SRSupWRs' : sqData["SR_highestWinrateSup"],
                     'SRTopWRs' : sqData["SR_highestWinrateTop"],
                     }

    

