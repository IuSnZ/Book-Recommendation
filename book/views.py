from django.shortcuts import render
from django.http import HttpRequest
# from . import Bookdata
import numpy as np
from django.contrib.auth.decorators import login_required

# from .models import Books

# from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

import pickle
# for home page
popular_df = pickle.load(open('book/final_df.pkl','rb'))

#for receommendation
content_cv = pickle.load(open('book/content_cv copy.pkl','rb'))
empty_cosine1 = pickle.load(open('book/empty_cosine1 copy.pkl','rb'))

# Create your views here.

#to handle the traffic of the homepage
def home(request):
    data = {
         "BookName" :list(
         zip(
             list(popular_df['title'].values),
             list(popular_df['rating'].values),
             list(popular_df['cover_url'].values)
         ))
    }
    # content = {
    #     'Bdetail' : data
    # }
    # return render(request,'bookhtml/home.html', {'title':'Home'})
    return render(request,'bookhtml/home.html', data)

def about(request):
    return render(request, 'bookhtml/about.html', {'title':'About Us'})

def login(request):
    return render(request, 'bookhtml/login.html', {'title':'Login'})

def register(request):
    return render(request, 'bookhtml/register.html', {'title':'Sign-up'})

def footer(request):
    return render(request, 'bookhtml/footer.html', {'title':'Footer'}),

@login_required
def browse(request):
    data = {
         "BookName" :list(
         zip(
             list(content_cv['title'].values),
             list(content_cv['author_x'].values),
             list(content_cv['cover_url'].values)
         ))
    }
    return render(request,'bookhtml/browse.html', {'title':'Browse','BookName':data})


#for genre
def genre(request):
    all_genre = set()
    for genres in content_cv['list_genre']:
        all_genre.update(genres.split(','))
    all_genre = sorted(all_genre)
    print(all_genre)
    # if request.method == 'POST':
    selected_genre = request.POST.get('genre')
    if selected_genre:
        recommend_books = content_cv[content_cv['list_genre'].str.contains(selected_genre)]
    genrelist = {
        'genres':all_genre,
        'selected_genre':selected_genre,
        'recommend_books':recommend_books

    }
    return render(request,'bookhtml/browse.html', genrelist)
    

def recommend_Cntcv1(book1):
    if book1 not in content_cv['title'].values:
        raise ValueError(f"Book '{book1}' not found in the dataset.")
    
    index = np.where(content_cv['title'] == book1)[0][0]
    similar_books = sorted(enumerate(empty_cosine1[index]), key=lambda x: x[1], reverse=True)[1:6]

    ContentReccomend = []
    for i in similar_books:
        item = []
        tempdf = content_cv[content_cv['title'] == content_cv['title'][i[0]]]
        item.extend(list(tempdf.drop_duplicates('title')['title'].values))
        item.extend(list(tempdf.drop_duplicates('title')['author_x'].values))
        item.extend(list(tempdf.drop_duplicates('title')['cover_url'].values))

        ContentReccomend.append(item)
    return ContentReccomend

def recommend_books(request: HttpRequest):
    data = []
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            data = recommend_Cntcv1(user_input)
        except ValueError as e:
            return render(request, 'bookhtml/browse.html', {'error': str(e)})

    return render(request, 'bookhtml/browse.html', {'data': data})





