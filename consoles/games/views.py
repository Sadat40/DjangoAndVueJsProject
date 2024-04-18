from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Character, Game
from .forms import GameForm
from django.forms.models import model_to_dict
from django.views import View
from django.views.generic.base import TemplateView
from django.http import JsonResponse


# Create your views here.


###################### ACTORS ##########################

class CharacterListView(ListView):
    model = Character

class CharacterCreateView(CreateView):
    model = Character
    fields = ['name']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Character "{character_name}" has been created'.format(
                character_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("games:character_detail", args=[self.object.id])

class CharacterDetailView(DetailView):
    model = Character

class CharacterUpdateView(UpdateView):
    model = Character
    fields = ['name']
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Character "{character_name}" has been updated'.format(
                character_name=self.object.name))
        return response
    
    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("games:character_detail", args=[self.object.id])
        # you can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        #return reverse_lazy("movies:actor_detail",
        #                    kwargs={'pk':self.object.id})


class CharacterDeleteView(DeleteView):
    model = Character
    success_url = reverse_lazy("games:character_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Character "{character_name}" has been deleted'.format(
                character_name=self.object.name))
        return response


###################### MOVIES ##########################


class GameListView(LoginRequiredMixin, ListView):
    model = Game


class GameDetailView(DetailView):
    model = Game


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Game "{game_name}" has been created'.format(
                game_name=self.object.name))
        return response

    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("games:game_detail", args=[self.object.id])
        # you can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        #return reverse_lazy("movies:actor_detail",
        #                    kwargs={'pk':self.object.id})



class GameUpdateView(UpdateView):
   model = Game
   form_class = GameForm

   def form_valid(self, form):
       response = super().form_valid(form)
       messages.add_message(
           self.request,
           messages.SUCCESS,
           'Game "{game_name}" has been updated'.format(
               game_name=self.object.name
           ),
       )
       return response

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       game_dico = model_to_dict(self.object)
       game_dico["release_date"] = game_dico["release_date"].strftime(
           "%Y-%m-%d"
       )
    #    number of characters
       characters = game_dico["characters"]
       game_character_list = []
       for character in characters:
           game_character_list.append({"id": character.id, "name": character.name})
       game_dico["characters"] = game_character_list
       character_list = list(Character.objects.all().values())
       context["game_dict"] = game_dico
       context["character_list"] = character_list
       print("context", context)
       return context

   # comment the following line to show the error about not having an
   # success_url
   def get_success_url(self):
       return reverse_lazy("games:game_detail", args=[self.object.id])
       # you can also use it this way with kwargs, just to let you know
       # but here we have only one argument, so no mistake can be done
       # return reverse_lazy("movies:actor_detail",
       #                    kwargs={'pk':self.object.id})

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy("games:game_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Game "{game_name}" has been deleted'.format(
                game_name=self.object.name))
        return response

class GameUpdatebisView(View):
   def post(self, request, *args, **kwargs):
       game = get_object_or_404(Game, pk=self.kwargs["pk"])
       # Create a form instance with POST data
       form = GameForm(request.POST, instance=game)
       if form.is_valid():
           form.save()
           return JsonResponse({"success": True})
       else:
           return JsonResponse({"success": False, "errors": form.errors})
       
class GameDetailbisView(TemplateView):
    template_name = "games/game_detailbis.html"
    def get(self, request, *args, **kwargs):
        game = get_object_or_404(Game, pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_id'] = self.kwargs["pk"]
        return context

class GameDetailJsView(View):
    def get(self, request, *args, **kwargs):
        game = get_object_or_404(Game, pk=self.kwargs["pk"])
        game_js = model_to_dict(game)
        game_js["characters"] = []
        for character in game.characters.values():
            game_js["characters"].append(character)
        return JsonResponse({"game": game_js})
    