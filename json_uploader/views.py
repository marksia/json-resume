import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import JSONUploaderForm

# class JsonUploaderView(TemplateView):
# 	template_name = "index.html"


class JsonUploaderView(FormView):
    template_name = 'index.html'
    form_class = JSONUploaderForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print (type(form.cleaned_data["file"]))

        file = form.cleaned_data["file"]
        json_data = json.loads(file.read().decode("utf-8"))

        print (json_data)
        print (type(json_data))

        self.request.session["json_data"] = json_data
        return super(JsonUploaderView, self).form_valid(form)

    def get_success_url(self):
        return reverse('json_uploader:profile')


class JSONProfileView(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.session.get("json_data") is not None:
            return super(JSONProfileView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("json_uploader:index"))

    def get_context_data(self, **kwargs):
        context = super(JSONProfileView, self).get_context_data(**kwargs)
        context["json_data"] = self.request.session["json_data"]
        del self.request.session["json_data"]
        return context