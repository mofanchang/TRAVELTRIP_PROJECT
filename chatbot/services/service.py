from django.db.models import Q
from itertools import combinations
from opencc import OpenCC
from trips.models import Trip
import json

cc = OpenCC('s2t')  # 簡轉繁

def recommend_trips(llm_output):
    try:
        parsed = json.loads(llm_output)
    except json.JSONDecodeError:
        return Trip.objects.none()

    days = int(parsed.get("天數", 0))
    city_name = cc.convert(parsed.get("城市") or "")
    country_name = cc.convert(parsed.get("國家") or "")
    keywords = cc.convert(
        parsed.get("特徵") or parsed.get("特性") or parsed.get("關鍵字") or parsed.get("keywords") or ""
    ).strip()

    conditions = []
    if city_name:
        conditions.append(Q(city__icontains=city_name))
    if country_name:
        conditions.append(Q(country__icontains=country_name))
    if days:
        conditions.append(Q(duration__gte=days - 1, duration__lte=days + 1))
    if keywords:
        first_kw = keywords.split(",")[0].split("、")[0].strip()
        if first_kw:
            conditions.append(Q(keywords__icontains=first_kw))

    qs = Trip.objects.all()

    if len(conditions) >= 2:
        q_obj = Q()
        for c1, c2 in combinations(conditions, 2):
            q_obj |= (c1 & c2)
        qs = qs.filter(q_obj)
    elif conditions:
        qs = qs.filter(conditions[0])

    return qs[:5]
