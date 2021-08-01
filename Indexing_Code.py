import pandas as pd
from Dataset_Complete import *
i = 0
#Atlanta
P_Atlanta = 0
Y_Atlanta = 0
#Austin
P_Austin = 0
Y_Austin = 0
#Boston
P_Boston = 0
Y_Boston = 0
#Chicago
P_Chicago = 0
Y_Chicago = 0
#Dallas
P_Dallas = 0
Y_Dallas = 0
#Denver
P_Denver = 0
Y_Denver = 0
#Los Angeles
P_Los_Angeles = 0
Y_Los_Angeles = 0
#Miami
P_Miami = 0
Y_Miami = 0
#Nashville
P_Nashville = 0
Y_Nashville = 0
#New York
P_New_York = 0
Y_New_York = 0
#Orange County
P_Orange_County = 0
Y_Orange_County = 0
#Phoenix
P_Phoenix = 0
Y_Phoenix = 0
#Pittsburgh
P_Pittsburgh = 0
Y_Pittsburgh = 0
#Sacramento
P_Sacramento = 0
Y_Sacramento = 0
#San Diego
P_San_Diego = 0
Y_San_Diego = 0
#San Francisco
P_San_Francisco = 0
Y_San_Francisco = 0
#Seattle
P_Seattle = 0
Y_Seattle = 0
#Silicon Valley
P_Silicon_Valley = 0
Y_Silicon_Valley = 0
#Tucson
P_Tucson = 0
Y_Tucson = 0
#Washington
P_Washington = 0
Y_Washington = 0

while i < len(City):
    if City[i] == 'ATLANTA GA':
        if Com[i] == 'Pink Cab':
            P_Atlanta += 1
        else:
            Y_Atlanta += 1
    elif City[i] == 'AUSTIN TX':
        if Com[i] == 'Pink Cab':
            P_Austin += 1
        else:
            Y_Austin += 1
    elif City[i] == 'BOSTON MA':
        if Com[i] == 'Pink Cab':
            P_Boston += 1
        else:
            Y_Boston += 1
    elif City[i] == 'CHICAGO IL':
        if Com[i] == 'Pink Cab':
            P_Chicago += 1
        else:
            Y_Chicago += 1
    elif City[i] == 'DALLAS TX':
        if Com[i] == 'Pink Cab':
            P_Dallas += 1
        else:
            Y_Dallas += 1
    elif City[i] == 'DENVER CO':
        if Com[i] == 'Pink Cab':
            P_Denver += 1
        else:
            Y_Denver += 1
    elif City[i] == 'LOS ANGELES CA':
        if Com[i] == 'Pink Cab':
            P_Los_Angeles += 1
        else:
            Y_Los_Angeles += 1
    elif City[i] == 'MIAMI FL':
        if Com[i] == 'Pink Cab':
            P_Miami += 1
        else:
            Y_Miami += 1
    elif City[i] == 'NASHVILLE TN':
        if Com[i] == 'Pink Cab':
            P_Nashville += 1
        else:
            Y_Nashville += 1
    elif City[i] == 'NEW YORK NY':
        if Com[i] == 'Pink Cab':
            P_New_York += 1
        else:
            Y_New_York += 1
    elif City[i] == 'ORANGE COUNTY':
        if Com[i] == 'Pink Cab':
            P_Orange_County += 1
        else:
            Y_Orange_County += 1
    elif City[i] == 'PHOENIX AZ':
        if Com[i] == 'Pink Cab':
            P_Phoenix += 1
        else:
            Y_Phoenix += 1
    elif City[i] == 'PITTSBURGH PA':
        if Com[i] == 'Pink Cab':
            P_Pittsburgh += 1
        else:
            Y_Pittsburgh += 1
    elif City[i] == 'SACRAMENTO CA':
        if Com[i] == 'Pink Cab':
            P_Sacramento += 1
        else:
            Y_Sacramento += 1
    elif City[i] == 'SAN DIEGO CA':
        if Com[i] == 'Pink Cab':
            P_San_Diego += 1
        else:
            Y_San_Diego += 1
    elif City[i] == 'SAN FRANCISCO CA':
        if Com[i] == 'Pink Cab':
            P_San_Francisco += 1
        else:
            Y_San_Francisco += 1
    elif City[i] == 'SEATTLE WA':
        if Com[i] == 'Pink Cab':
            P_Seattle += 1
        else:
            Y_Seattle += 1
    elif City[i] == 'SILICON VALLEY':
        if Com[i] == 'Pink Cab':
            P_Silicon_Valley += 1
        else:
            Y_Silicon_Valley += 1
    elif City[i] == 'TUCSON AZ':
        if Com[i] == 'Pink Cab':
            P_Tucson += 1
        else:
            Y_Tucson += 1
    else:
        City[i] == 'WASHINGTON DC'
        if Com[i] == 'Pink Cab':
            P_Washington += 1
        else:
            Y_Washington += 1
    i +=1


