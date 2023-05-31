import numpy as np
from sklearn.metrics import pairwise_distances


def cosine_distances(embs1, embs2):
    return pairwise_distances(np.stack(embs1), np.stack(embs2), metric='cosine')


def cosine_distance(emb1, emb2):
    return pairwise_distances(emb1.reshape(1, -1), emb2.reshape(1, -1), metric='cosine')[0][0]


def jaccard(vs1, vs2, how='inner'):
    if how == 'inner':
        if len(set(vs1) | set(vs2)) == 0:
            return 1
        return len(set(vs1) & set(vs2)) / len(set(vs1) | set(vs2))
    elif how == 'left':
        if len(vs1) == 0:
            return 1
        return len(set(vs1) & set(vs2)) / len(set(vs1))
    elif how == 'right':
        if len(vs2) == 0:
            return 1
        return len(set(vs1) & set(vs2)) / len(set(vs2))
    raise ValueError(how)