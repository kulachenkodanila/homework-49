from django.shortcuts import redirect, get_object_or_404, render
from django.views import View


class UpdateView(View):
   form_class = None
   template_name = None
   redirect_url = ''
   model = None
   key_kwarg = 'pk'
   context_key = 'object'

   def get(self, request, *args, **kwargs):
       self.object = self.get_object()
       form = self.form_class(instance=self.object)
       context = self.get_context_data(form=form)
       return render(request, self.template_name, context=context)



   def post(self, request, *args, **kwargs):
       self.object = self.get_object()
       form = self.form_class(instance=self.object, data=request.POST)
       if form.is_valid():
           return self.form_valid(form)
       else:
           return self.form_invalid(form)


   def form_valid(self, form):
       self.object = form.save()
       return redirect(self.get_redirect_url())

   def form_invalid(self, form):
       context = self.get_context_data(form=form)
       return render(self.request, self.template_name, context=context)

   def get_object(self):
       pk = self.kwargs.get(self.key_kwarg)
       return get_object_or_404(self.model, pk=pk)

   def get_context_data(self, **kwargs):
       context = self.kwargs.copy()
       context[self.context_key] = self.object
       context.update(kwargs)
       return context

   def get_redirect_url(self):
       return self.redirect_url
