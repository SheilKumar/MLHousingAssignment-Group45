from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

class LassoClass:
    """
    Generates Lasso regression model with desired "C" from the sklearn.linear_model module.
    """

    def __init__(self,C) -> None:
        self.alpha_chosen = 1/(2*C)
        self.model = Lasso(alpha=self.alpha_chosen)



class RidgeClass:
    """
    Generates Ridge regression model with desired "C" from the sklearn.linear_model module.
    """

    def __init__(self,C) -> None:
        self.alpha_chosen = 1/(2*C)
        self.model = Ridge(alpha=self.alpha_chosen)