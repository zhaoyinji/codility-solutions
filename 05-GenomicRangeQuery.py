# To avoid O(N*M), we will keep a cumulative counters of occurences for each nucleotides.
# Therefore, for a given range with P and Q, if cum[Q] > cum[P], it indicates the fact that 
# the nucleotides was present. 

def solution(S, P, Q):
    N = len(S)
    M = len(P)
    impact = {'A':1, 'C':2, 'G':3, 'T': 4}
    n_counters = {'A':0, 'C':0, 'G':0, 'T': 0}
    # we add the starting counters state of 0s
    counters = [{'A':0, 'C':0, 'G':0, 'T': 0}]

    min_impact = []

    # we'll have one more item than the list of letter to account for the start of 0s
    for i in range(N):
        n_counters[S[i]] += 1
        counters.append({'A':n_counters['A'], 'C':n_counters['C'], 'G':n_counters['G'], 'T': n_counters['G']})

    for i in range(M):
        P_idx = P[i]
        Q_idx = Q[i]+1 # since our count is shifted

        if counters[Q_idx]['A'] > counters[P_idx]['A']:
            min_impact.append(impact['A'])
        elif counters[Q_idx]['C'] > counters[P_idx]['C']:
            min_impact.append(impact['C'])
        elif counters[Q_idx]['G'] > counters[P_idx]['G']:
            min_impact.append(impact['G'])
        else:
            min_impact.append(impact['T'])

    return min_impact
