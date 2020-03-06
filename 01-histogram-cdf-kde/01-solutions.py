# задача 1
def ecdf(x, data) -> float:
    return (data < x).sum() / data.shape[0]

# задача 2
def discrete_hist(data):
    result = dict()
    for loc in data:
        if not loc in result:
            result[loc] = 1
        else:
            result[loc] += 1
    return list(result.values()), list(result.keys())

# задача 3
def continuous_hist(data, bins=4):
    data_min = np.min(data)
    data_max = np.max(data)
    
    bin_edges = np.linspace(data_min, data_max, bins + 1)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2
    hist = np.zeros(bins)
    
    for x in data:
        loc = 0
        while (loc < bins - 1) and not (x >= bin_edges[loc] and x <= bin_edges[loc+1]):
            loc += 1
        hist[loc] += 1
        
    step = bin_edges[1] - bin_edges[0]
    return hist / (len(data) * step), bin_centers

# задача 4
def kde(x, data, h):
    x = (x - data) / h
    x = np.exp(- x ** 2 / 2) / np.sqrt(2 * np.pi)
    return x.sum() / (data.shape[0] * h)