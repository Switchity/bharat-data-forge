import subprocess
from django.http import JsonResponse


def run_pipeline(request):

    subprocess.run(["python", "spark_jobs/sales_etl.py"])

    return JsonResponse({"status": "Spark pipeline executed"})