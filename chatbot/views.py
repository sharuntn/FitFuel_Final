from django.shortcuts import render
from translate import translate
# Create your views here.
L = []
def chatbotfunc(request):
   
    if request.method == 'POST':
        prompt_value = request.POST.get('prompt', '')
        ans = translate(prompt_value)
        L.append({'prompt': prompt_value, 'translation': ans})
        return render(request, 'chatbot.html', {'data': L})
    else:
        return render(request, 'chatbot.html')