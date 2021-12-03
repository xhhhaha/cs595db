import random
fieldSize=10**7
ita=11
alpha=13
g=5
# subgroup=[1,3,4,5,9], mod 11
def Groupmulti(m):
    '''cyclic group'''
    ita_prime=11*alpha
    return pow(g, m)%ita_prime


def getAdditiveShares(secret, N):
    '''Generate N additive shares from 'secret' in finite field of size 'fieldSize'.'''
 
    # Generate n-1 shares randomly
    shares = [random.randrange(fieldSize) for i in range(N-1)]
 
    # Append final share by subtracting all shares from secret
    # Modulo is done with fieldSize to ensure share is within finite field
    shares.append((secret - sum(shares)) % fieldSize )
    return shares
 
def reconstructSecret(shares):
    '''Regenerate secret from additive shares'''
    return sum(shares) % fieldSize
 
if __name__ == "__main__":
    # Generating the shares
    shares = getAdditiveShares(1234, 5)
    print('Shares are:', shares)
     
    # Reconstructing the secret from shares
    print('Reconstructed secret:', reconstructSecret(shares))


def proactivizeShares(shares):
    '''Refreshed shares by proactivization'''
    
    n = len(shares)
    refreshedShares = [0]*n

    for s in shares:

        # Divide each share into sub-fragments using additive sharing
        subShares = getAdditiveShares(s, n)

        # Add subfragments of corresponding parties
        for p, sub in enumerate(subShares):
            refreshedShares[p] += sub
            
    return refreshedShares

