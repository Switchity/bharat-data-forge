import uuid
import subprocess
from django.http import JsonResponse
from django.shortcuts import render, redirect,reverse
from .forms import StudentRegistrationForm



def file_selection_page(request):
    if request.method == 'POST':
        unique_id = str(uuid.uuid4())
        fm = StudentRegistrationForm(request.POST)
        uploaded_pyspark_file = request.getlist('pysparkFile')
        print(uploaded_pyspark_file)
        if len(uploaded_pyspark_file) > 0:
            extension = uploaded_pyspark_file[0].split('.')[-1]
            print(extension)
            if extension not in ['.py']:
                error_message = "File extension must be .py"
                return render(request, "pyspark_app/index.html", {
                    "form": fm,
                    "error_message": error_message,
                })
            data_frame= {}
            context = {
                "unique_id": unique_id,
                "data_set" : data_frame
            }
            return render(request, "pyspark_app/sales_etl_dashboard", context)

        else:
            error_message = "uploaded file is empty"
            return render(
                request, "pyspark_app/index.html", {
                    "form": fm,
                "error_message": error_message,
                }
            )
    else:
        fm = StudentRegistrationForm()
        return render(
            request, "pyspark_app/index.html", {
                "form": fm
            }
        )