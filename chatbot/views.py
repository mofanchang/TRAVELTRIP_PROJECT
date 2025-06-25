from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .llm import query_llm_local
from .services.service import recommend_trips
from django.db.models import Q


@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        body = json.loads(request.body)
        user_input = body.get("message", "")

        llm_reply = query_llm_local(user_input)
        trips = recommend_trips(llm_reply)

        trip_list = []
        for trip in trips:
            trip_list.append({
                "name": trip.name,
                "description": trip.description,
                "link": f"/trips/{trip.id}/"  # 產品連結
            })

        return JsonResponse({
            "recommended_trips": trip_list
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


