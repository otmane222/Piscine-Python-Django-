# ex02/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import Text
from datetime import datetime
import logging
import os



def contact_view(request):
    if request.method == 'POST':
        form = Text(request.POST)
        if form.is_valid():
            text_input = form.cleaned_data['text_input']
            
            # Save to logs file
            log_file_path = os.path.join(settings.EX02_LOGS_DIR, 'input_history.log')
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"{datetime.now()} - {text_input}\n")
            
            # Append to input history
            if 'input_history' not in request.session:
                request.session['input_history'] = []
            # request.session['input_history'].append((datetime.now(), text_input))
            request.session['input_history'].append((f"{datetime.now()}", text_input))
            request.session.modified = True  # Ensure session is saved
            
            return redirect('ex02')  # Redirect to the 'ex02' URL name
    else:
        form = Text()
    
    # Retrieve input history from session
    input_history = request.session.get('input_history', [])
    formatted_input_history = [
        (entry[0].strftime('%Y-%m-%d %H:%M:%S'), entry[1]) if isinstance(entry[0], datetime) else entry
        for entry in input_history
    ]
    
    return render(request, 'ex02/index.html', {'form': form, 'input_history': formatted_input_history})