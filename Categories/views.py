from django.views.generic import  DeleteView, UpdateView
from django.shortcuts import render
from Categories.models import Gaming, Crypto, Coding, Anime
from Categories.forms import Games, Cryptos, Code, Animes


def AddGPost(request):
    if request.method == 'GET':
        context = {
            'form': Games()
        }

        return render(request, 'Gaming/addGPost.html', context=context)

    elif request.method == 'POST':
        form = Games(request.POST)
        if form.is_valid():
            Gaming.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user = form.cleaned_data['user']
            )
            context = {
                'message': 'added successfully'
            }
            return render(request, 'Gaming/addGPost.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Games()
            }
            return render(request, 'Gaming/addGPost.html', context=context)

def AddCPost(request):
    if request.method == 'GET':
        context = {
            'form': Cryptos()
        }

        return render(request, 'Crypto/addCPost.html', context=context)

    elif request.method == 'POST':
        form = Cryptos(request.POST)
        if form.is_valid():
            Crypto.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user = form.cleaned_data['user']
            )
            context = {
                'message': 'added successfully'
            }
            return render(request, 'Crypto/addCPost.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Cryptos()
            }
            return render(request, 'Crypto/addCPost.html', context=context)

def AddCodingPost(request):
    if request.method == 'GET':
        context = {
            'form': Code()
        }

        return render(request, 'Code/addCPost.html', context=context)

    elif request.method == 'POST':
        form = Code(request.POST)
        if form.is_valid():
            Coding.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user = form.cleaned_data['user']
            )
            context = {
                'message': 'added successfully'
            }
            return render(request, 'Code/addCPost.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Code()
            }
            return render(request, 'Code/addCPost.html', context=context)
        
def AddAPost(request):
    if request.method == 'GET':
        context = {
            'form': Animes()
        }

        return render(request, 'Anime/addAPost.html', context=context)

    elif request.method == 'POST':
        form = Animes(request.POST)
        if form.is_valid():
            Anime.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user = form.cleaned_data['user']
            )
            context = {
                'message': 'added successfully'
            }
            return render(request, 'Anime/addAPost.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Animes()
            }
            return render(request, 'Anime/addAPost.html', context=context)

def GamesList(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_Games = Gaming.objects.filter(name__icontains=search) 
    else:
        all_Games = Gaming.objects.all()   
    context = {
        'Gaming':all_Games,
    }
    return render(request, 'Gaming/gaming.html', context=context)

def CryptoList(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_crypto = Crypto.objects.filter(name__icontains=search) 
    else:   
        all_crypto = Crypto.objects.all()
    context = {
        'Crypto':all_crypto,
    }
    return render(request, 'Crypto/crypto.html', context=context)

def C_List(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_Code = Coding.objects.filter(name__icontains = search) 
    else:   
        all_Code = Coding.objects.all()  
    context = {
        'Coding':all_Code,
    }
    return render(request, 'Code/code.html', context=context)

def AnimeList(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_Anime = Anime.objects.filter(name__icontains = search) 
    else:   
        all_Anime = Anime.objects.all()  
    context = {
        'Anime':all_Anime,
    }
    return render(request, 'Anime/anime.html', context=context)

def GameUpdate(request, pk):
    game = Gaming.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Games(
                initial={
                    'name':game.name,
                    'description':game.description,}
            )
        }

        return render(request, 'Gaming/update.html', context=context)

    elif request.method == 'POST':
        form = Games(request.POST)
        if form.is_valid():
            game.name = form.cleaned_data['name'],
            game.description = form.cleaned_data['description'],
            
            game.save()
            
            context = {
                'message': 'Updated'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Games()
            }
        return render(request, 'Gaming/update.html', context=context)

def CryptoUpdate(request, pk):
    crypto = Crypto.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Cryptos(
                initial={
                    'name':crypto.name,
                    'description':crypto.description,}
            )
        }

        return render(request, 'Crypto/update.html', context=context)

    elif request.method == 'POST':
        form = Cryptos(request.POST)
        if form.is_valid():
            crypto.name = form.cleaned_data['name'],
            crypto.description = form.cleaned_data['description'],
            
            crypto.save()
            
            context = {
                'message': 'Updated'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Games()
            }
        return render(request, 'Crypto/update.html', context=context)

def CodeUpdate(request, pk):
    code = Coding.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Code(
                initial={
                    'name':code.name,
                    'description':code.description,}
            )
        }

        return render(request, 'Code/update.html', context=context)

    elif request.method == 'POST':
        form = Cryptos(request.POST)
        if form.is_valid():
            code.name = form.cleaned_data['name'],
            code.description = form.cleaned_data['description'],
            
            code.save()
            
            context = {
                'message': 'Updated'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Games()
            }
        return render(request, 'Code/update.html', context=context)
    
def AnimeUpdate(request, pk):
    anime = Anime.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Animes(
                initial={
                    'name':anime.name,
                    'description':anime.description,}
            )
        }

        return render(request, 'Anime/update.html', context=context)

    elif request.method == 'POST':
        form = Cryptos(request.POST)
        if form.is_valid():
            anime.name = form.cleaned_data['name'],
            anime.description = form.cleaned_data['description'],
            
            anime.save()
            
            context = {
                'message': 'Updated'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Games()
            }
        return render(request, 'Anime/update.html', context=context)
    
class GameDeleteView(DeleteView):
    model = Gaming
    template_name = 'Gaming/delete.html'
    success_url = '/gaming'
    
class CryptoDeleteView(DeleteView):
    model = Crypto
    template_name = 'Crypto/delete.html'
    success_url = '/crypto'
    
class CodingDeleteView(DeleteView):
    model = Coding
    template_name = 'Code/delete.html'
    success_url = '/coding'
    
class AnimeDeleteView(DeleteView):
    model = Anime
    template_name = 'Anime/delete.html'
    success_url = '/anime'