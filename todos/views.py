from django.shortcuts import render, HttpResponseRedirect
from todos.forms import TodoForm
from todos.models import Todo
from datetime import datetime
from dateutil import parser
import spacy

def new_todo(request):

    nlp = spacy.load('en_core_web_sm')

    extracted_date = None
    extracted_time = None

    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)

        # check if the form is valid
        if form.is_valid():
            description = form.cleaned_data.get('description') 
            doc = nlp(description)

            for ent in doc.ents:
                if ent.label_ == 'TIME':
                    extracted_time = ent.text
                    try:
                        extracted_time = parser.parse(extracted_time).time()
                    except (ValueError, TypeError):
                        extracted_time = None
                elif ent.label_ == 'DATE':
                    extracted_date = ent.text
                    break
            
            if extracted_time and not extracted_date:
                extracted_date = datetime.now().strftime('%Y-%m-%d')
            
            todo_instance = form.save(commit=False)  # Do not commit the save yet
            todo_instance.extracted_date = extracted_date  # Save the extracted date
            todo_instance.extracted_time = extracted_time  # Save the extracted time
            todo_instance.save()

            # redirect to other pages
            return HttpResponseRedirect('/')
        
    return render(request, 'todos/new.html', {'form': form, 'extracted_date': extracted_date, 'extracted_time': extracted_time}) 


def list_todo(request):
    all_todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': all_todos})


def todo_details(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        return render(request, 'todos/detail.html', {'todo': todo})
    except Todo.DoesNotExist:
        return HttpResponseRedirect('/')
    

def edit(request, pk):
    try: 
        todo = Todo.objects.get(id=pk)
        return render(request, 'todos/edit.html', {'todo': todo})
    except Todo.DoesNotExist:
        # "show errors to your customers"
        return HttpResponseRedirect('/')










