from django.shortcuts import render
import json
from .models import Event

# 공휴일 데이터 (2025년 기준)
HOLIDAYS = [
    {"name": "추석", "start": "2025-10-06", "end": "2025-10-08"},
    {"name": "설날", "start": "2025-01-28", "end": "2025-01-30"},
]

def calendar_view(request):
    # 데이터베이스에서 이벤트 가져오기
    events = Event.objects.all()
    event_data = {event.date.strftime("%Y-%m-%d"): [event.description] for event in events}

    # 샘플 이벤트 데이터 (2025년 기준)
    sample_events = {
        "2025-01-28": ["설날 시작"],
        "2025-10-06": ["추석 시작"],
    }

    # 기존 이벤트와 샘플 이벤트 병합
    for date, descriptions in sample_events.items():
        if date in event_data:
            event_data[date].extend(descriptions)
        else:
            event_data[date] = descriptions

    return render(request, 'calendar_app/calendar.html', {
        "events": json.dumps(event_data),  # JSON 형식으로 변환
        "holidays": json.dumps(HOLIDAYS),  # JSON 형식으로 변환
    })
