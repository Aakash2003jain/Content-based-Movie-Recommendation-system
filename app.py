import streamlit as st 
import pickle
import pandas as pd 
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
simi=pickle.load(open('simi.pkl','rb'))

movies=pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')
movie_name=st.selectbox('Which movie?',movies['title'].values)

def recommend(movie):
    movie_idx=movies[movies['title']==movie].index[0]
    popular=movies['popularity'][movie_idx]
    distances=simi[movie_idx]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:]
    #print(movie_list)
    flag=0
    m=[]
    for i in movie_list:
        
        p=movies['popularity'][i[0]]
        if(p>=popular):
            print(movies['title'][i[0]])
            m.append(movies['title'][i[0]])
            flag+=1
        if(flag==6):
            break
    return m
        
    
    
if st.button('Recommend'):
   movie_recommendations= recommend(movie_name)
   for i in movie_recommendations:
        st.write(i)
    