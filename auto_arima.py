from statsmodels.tsa.arima_model import ARIMA

def get_aic(ts, pdq, *args):
    """
    Fits and returns ARIMA model aic for a give time series

    Arguments
    --------
    ts -- time series; pandas.Series
    pdq -- ARIMA order

    """
    model = ARIMA(ts, pdq, *args).fit()
    return model.aic


def auto_arima(ts, order):
    """
    Auto_arima function like R's

    Arguments
    ---------
    ts -- time series being fit
    order -- max pdq for ARIMA model

    Returns
    -------
    order_min -- order of minimim aic
    aic_min -- minimum aic
    """
    p = list(range(order[0] + 1))
    d = list(range(order[1] + 1))
    q = list(range(order[2] + 1))

    combinations = []
    for i in p:
        for j in d:
            for k in q:
                combinations.append((i,j,k))

    aic_min = None
    order_min = None
    aic = None
    for c in combinations:
        try:
            aic = get_aic(ts, c)
            if aic_min == None or aic_min > aic:
                aic_min = aic
                order_min = c
        except:
            pass
    
    return order_min, aic


def map_arima(x):
    return auto_arima(x, (3,3,3))
