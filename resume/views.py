# Create your views here.
from django.shortcuts import *
from django.core import serializers
from resume.models import *

def resume_as_json(request, resume_id):
	json_serializer = serializers.get_serializer("json")()
	data = json_serializer.serialize(ResumeVersion.objects.all(), ensure_ascii=False)
	return HttpResponse(data, mimetype="application/json")