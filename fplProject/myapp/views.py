from django.shortcuts import render
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import pandas as pd
import os


# Create your views here.

def show(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(BASE_DIR, 'data', 'fpl.csv')
    data = pd.read_csv(csv_file_path)
    few = data.head(10)
    tot_matches = data.shape[0]
    features = data.shape[1] - 1
    wins_at_home = len(data[data['FTR'] == 'H'])
    homewin_rate = (float(wins_at_home / tot_matches)) * 100
    referees = sorted(set(data['Referee']))
    refs = sorted(data['Referee'])
    maxs = 0
    maxrefs=""
    mins = 1000
    minrefs=""
    for ref in referees:
        x = refs.count(ref)
        if x > maxs:
            maxs = x
            maxrefs = ref
        if x == maxs:
            if maxrefs != ref:
                maxrefs +=", " + ref
        if x<mins:
            mins = x
            minrefs = ref
        if x == mins:
            if minrefs != ref:
                minrefs +=", " + ref


    return render(request, 'show.html',{'few':few, 'tot_matches':tot_matches, 'features':features, 'wins_at_home':wins_at_home,'homewin_rate':homewin_rate, 'referees':referees, 'maxs':maxs, 'maxrefs':maxrefs, 'mins':mins, 'minrefs':minrefs})
