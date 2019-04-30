# coding=utf-8

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import scipy
from nltk.corpus import stopwords


def recommend(pois, pois_user):
    """

    :type pois_user: pandas.core.frame.DataFrame
    :type pois: pandas.core.frame.DataFrame
    """
    #pois = pd.read_json('data/poi.json') # pois from DB
    #pois_user = pd.read_json('data/poi2.json') #pois que usuário mais gostou
    pois_appended = pois.append(pois_user)

    size_pois_user = len(pois_user) * -1


    tfidf = TfidfVectorizer(stop_words=stopwords.words('portuguese'))
    tfidf_matrix = tfidf.fit_transform(pois_appended['text'])

    pois_user_sum = tfidf_matrix[size_pois_user:].sum(axis=0) #soma as linhas referentes ao usuario

    tfidf_matrix_initial = tfidf_matrix[:tfidf_matrix.shape[0] + size_pois_user] #pega as linhas sem as do usuario
    tfidf_matrix = scipy.sparse.vstack((pois_user_sum, tfidf_matrix_initial)).tocsr() #adiciona uma linha com a soma do usuarios


    #tfidf_matrix = tfidf.fit_transform(metadata['overview'])
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix)
    #indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:]

    list_return = []
    for s in sim_scores:
        poi_id = pois.iloc[s[0] - 1]['item_id'] #subtrai o indice por 1 ja que adicionou a linha do usuario
        list_return.append((poi_id, s[1]))
    return sim_scores


if __name__ == '__main__':
    pois = pd.read_json('data/poi.json')  # pois from DB
    pois_user = pd.read_json('data/poi2.json')
    recommend(pois,pois_user)

'''
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return metadata['title'].iloc[movie_indices]

'''

