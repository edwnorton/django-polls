#!/home/tq/py_env/django/bin/python3
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import re, os, time
import sys
import django
sys.path.insert(0, '/home/tq/py_env/django/mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django.setup()
from polls.models import BookList

booklog = "/home/tq/py_env/django/mysite/polls/book.log"
def book_save():
    with open (booklog, 'r') as f:
        lines = f.readlines()
        for i in lines:
            bookname = os.path.basename(i).strip("\n")
            bookpath = os.path.dirname(i)
            format = os.path.splitext(i)[1].strip("\n")
            location = "2"
            print("bookname:{0}\nbookpath:{1}\nformat:{2}".format(bookname\
            ,bookpath, format))
            b = BookList(bookname=bookname, format=format, path=bookpath, location="2")
            b.save()
book_save()

