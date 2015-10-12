import Levenshtein

class obejct(object):
    def __getattr__(self,attr):
        scores = sorted([ (Levenshtein.ratio(attr,a),a) for a in self.__dict__.keys() ],reverse=True)
        return object.__getattribute__(self,scores[0][1])
