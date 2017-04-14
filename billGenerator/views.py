from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Course

class IndexView(generic.ListView):
    template_name = 'billGenerator/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Course.objects.all().order_by('next_session')

class CourseDetailView(generic.ListView):
    template_name= 'billGenerator/course_detail.html'
    context_object_name = 'course_detail'