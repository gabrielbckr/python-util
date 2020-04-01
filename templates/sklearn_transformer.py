from sklearn.base import BaseEstimator, TransformerMixin

class Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _validate_input(X):
	raise NotImplementedError

    def fit(self, X, y=None, **fit_params):  # NOSONAR(python:S117)
        return self

    def transform(self, X):
	raise NotImplementedError
