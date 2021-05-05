from .models import Throwing, Lifting
import json

def getChartDataAvgLift(user):
    data = []
    queryset = Throwing.objects.filter(ath_user_id=user.id)

    for throw in queryset:
        j = throw.throw_data
        keys = list(j.keys())
        for key in keys:
            data.append(0)
            repList = j.get(key)
            reps=0
            weight=0
            for rep in repList:
                if rep!=0:
                    reps+=1
                    weight+=rep
            data.append(weight/reps)
    return data, keys

def getChartDataAvgThrow(user):
    data = []
    queryset = Throwing.objects.filter(ath_user_id=user.id)

    for throw in queryset:
        j = throw.throw_data
        keys = list(j.keys())
        for i, key in enumerate(keys):
            data.append(0)
            repList = j.get(key)
            reps=0
            velo=0
            for rep in repList:
                if rep!=0:
                    reps+=1
                    velo+=rep
            if reps!=0:
                data[i] = (velo/reps)
    return data, keys