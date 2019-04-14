import graphlab
import graphlab as gl


sf2 = graphlab.SFrame({'user_id': ['0', '0', '0', '1', '1', '2', '2', '2'],
                     'item_id': ['a', 'b', 'c', 'a', 'b', 'b', 'c', 'd'],
                     'rating': [1, 3, 2, 5, 4, 1, 4, 3]})
m2 = graphlab.item_similarity_recommender.create(sf2, target="rating")

recs = m2.recommend()
print recs