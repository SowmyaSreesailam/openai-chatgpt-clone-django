from django.shortcuts import render
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(request):
    if request.method == "POST":
        user_msg = request.POST.get("message", "")
        if user_msg:
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": user_msg}]
            )
            reply = resp.choices[0].message.content
            return JsonResponse({"reply": reply})
    return render(request, "chatbot/chat.html")

