import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        enrollment_number = request.POST.get('enrollment_number')
        df = pd.read_excel('Cyber student data.xlsx')
        entry = df[df['enrollment_number'] == int(enrollment_number)]
        
        if not entry.empty:
            entry_details = entry.iloc[0].to_dict()
            request.session['entry_details'] = entry_details  # Store in session
            return render(request, 'index.html', {'entry_details': entry_details})
        else:
            return render(request, 'index.html', {'not_found': True})
    return render(request, 'index.html')


def save_entry(request):
    if request.method == 'GET':
        df = pd.read_excel('Cyber student data.xlsx')
        df2=pd.read_excel('newdata.xlsx')
        
        entry_details = request.session.get('entry_details')
        
        if entry_details is None:
            return JsonResponse({'error': 'Entry details not found'})
        
        if int(entry_details['enrollment_number']) in df2['enrollment_number'].values:
            return JsonResponse({'error': 'Entry already exists'})
        
        # Create a new DataFrame with the new entry
        new_entry = {
            'Sr. No': int(entry_details['Sr. No']),
            'enrollment_number': int(entry_details['enrollment_number']),
            'Roll No': int(entry_details['Roll No']),
            'First Name': (entry_details['First Name']),
            'Last Name': (entry_details['Last Name']),
            'Student Unique Id': (entry_details['Student Unique Id']),
            # Add other fields here
        }
        new_df = pd.DataFrame([new_entry])
        
        df_combined = pd.concat([df2, new_df], ignore_index=True)
        df_combined.to_excel('newdata.xlsx', index=False)
        
        # Remove the stored entry_details from the session
        del request.session['entry_details']
        
        return JsonResponse({'message': 'Entry saved successfully'})

    return JsonResponse({'error': 'Invalid request'})
