# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from django.template import loader
# from django.http import Http404
# from .models import Album, Song


# def index(request):
    #1.
    # just gives us a link through which we can access the id through the album_title links.
    # html = ''
    # for album in all_albums:
    #     path = '/music/' +str(album.id) + '/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    # return HttpResponse(html)


    #2.
    # working with templates...........................
    # template = loader.get_template('music/index.html')
    # context = {
    #     'all_albums' : all_albums,
    #     }
    # return HttpResponse(template.render(context, request))


    #3.
    # creating a shortcut for templates
    # from django.shortcuts import render
    # all_albums = Album.objects.all()
    #  context = { all_albums' : all_albums}
    #  return render(request, 'music/index.html', context)


    #all_albums = Album.objects.all()
    #return render(request, 'music/index.html', {'all_albums': all_albums})

#def detail(request, id):

   # raising the http error
   #try:
   #   album = Album.objects.get(pk=id)
   #except Album.DoesNotExist:
   #    raise Http404("Album does not exist")

   # the below code is basically the simple code for try and except case.
   #album = get_object_or_404(Album, pk=id)
   #return render(request,'music/Detail.html', {'album': album})

#def favourite(request, id):
    # access the class and assign the object.
    #album = get_object_or_404(Album, pk=id)
    # now we put the error message from the detail.html.
    #try:
       #selected_song = album.song_set.get(pk=request.POST['song'])
    #except (KeyError, Song.DoesNotExist):
        #return render(request,'music/Detail.html', {
            #'album': album,
            #'error_message': "You did not select a valid song",
        #})

    # if selected then perform the proper operations.
    #else:
        # 1. if selected then cant be changed
        #selected_song.is_favourite = True
        #selected_song.save()
        #return render(request, 'music/Detail.html', {'album': album})


        # 2. if selected then can be changed but in complex method of code.
        #if selected_song.is_favourite:
        #    selected_song.is_favourite = False
        #else:
        #    selected_song.is_favourite = True
        # selected_song.save()
        # return render(request, 'music/Detail.html', {'album': album})

        # 3. if selected then can be changed and in simple version of code.
        # selected_song.is_favourite = not selected_song.is_favourite
        # selected_song.save()
        # return render(request, 'music/Detail.html', {'album': album})

from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'my_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/Detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
    fields = ['artist', 'album_title', 'genre', 'album_logo']