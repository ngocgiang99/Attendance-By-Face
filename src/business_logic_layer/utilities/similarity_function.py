from scipy import spatial


# threshold = 0.3779
# threshold = 0.2487
# threshold = 0.3968
COSINE_THRESHOLD = 0.3779
def cosine_similarity(emb1, emb2):
    return spatial.distance.cosine(emb1, emb2)