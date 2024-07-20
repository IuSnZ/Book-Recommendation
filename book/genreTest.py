
import pickle 

data = pickle.load(open('book/content_cv copy.pkl','rb'))

genrelist = data['list_genre'].unique()
print(genrelist)

all_genre = set()
for genres in data['list_genre']:
    all_genre.update(genres.split(','))
all_genre = sorted(all_genre)
print(all_genre)
