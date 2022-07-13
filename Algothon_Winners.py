import numpy as np

def getMyPosition (prcSoFar):
    if prcSoFar.shape[1] <= 1: 
        return np.zeros(prcSoFar.shape[0])
    indxs = [2, 6, 60, 76, 91, 92, 95]
    p = prcSoFar[indxs, :]
    p_log = np.log(p)
    p_log_diff = np.diff(p_log, axis=1)

    p_log_diff_last = p_log_diff[-1]
    m = np.mean(p_log_diff_last)

    buys = np.zeros(prcSoFar.shape[0], dtype=bool)
    np.put(buys, indxs, p_log_diff_last < m - 0.0005)

    sells = np.zeros(prcSoFar.shape[0], dtype=bool)
    np.put(sells, indxs, p_log_diff_last > m + 0.0005)

    pos_limits = np.ceil(10000 / prcSoFar[:,-1])
    return pos_limits * buys - pos_limits * sells
