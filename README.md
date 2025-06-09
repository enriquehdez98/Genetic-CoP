# New Genetic Center of Pressure Indices

The present repository describes the details of the new genetic Center of Pressure indices using Adaptive Genetic Programming to improve the effectiveness of fall risk classification

The individual capacity of CoP indices reported in the state-of-the-art was optimized by Adaptive Genetic Programming across mathematical domains, such as entropy, time-based (distance, area, hybrid measures), and frequency-based:

## Genetic-distance:

```math
genetic-distance = \sum_{n=1}^{N}\left\{\left\{\left[\left(\left(\left(\left(\left(\left(\left(\left({cumsum\left(CoP_y\left[n\right] \bmod12.27\right)}^2 \bmod 86.10\right) \bmod -91.84\right) \bmod 12.27\right)+89.13\right) \bmod 12.27\right) \bmod 4.62\right) \bmod -91.84\right) \bmod 89.13-12.27\right) \bmod 4.62\right]^2\right\}^2\right\}
```

## Genetic-area:

```math
genetic-area=\sum_{n=1}^{N}\left(47.39\ast\left(18.84\ast\left(-45.68\bmod\left(18.84\ast\left(18.84\bmod\left(18.84\ast\left(CoP_{rd}\left[n\right]-\sum_{n=1}^{N}\frac{CoP_y\left[n\right]}{N}\right)\right)\right)\right)\right)\right)\right)
```


## Genetic-hybrid

```math
genetic-hydrid =\\
\frac{ \sum_{n=1}^{N}\left|(CoP_{y}[n+1]-hybrid_{item2})- hybrid_{item3}\right|}{4*\left(2*\left(\frac{max(\left|CoP_{y}-max(psMl)\right|)}{N}\right)\right)^{\sqrt{\sqrt{2}}}}
```

Where $$hybrid_{item1}$$ , $$hybrid_{item2}$$ , $$hybrid_{item3}$$ are:


```math
hybrid_{item1} = \\
\left|\left((CoP_{y}[n+1]-\sum_{n=1}^{N}\frac{CoP_{y}[n+1]}{N})-(CoP_{y}[n-1]-\sum_{n=1}^{N}\frac{CoP_{y}[n+1]}{N})\right)\right|
```

```math
hybrid_{item2} = \\
\sum_{n=1}^{N}\left|\left(CoP_{y}[n+1]-(\sum_{n=1}^{N}CoP_{x}[n]-\sum_{n=1}^{N}hybrid_{item1})\right)-\left(CoP_{y}[n-1]-\sum_{n=1}^{N}\frac{CoP_{x}[n-1]}{N}\right)\right|
```

```math
hybrid_{item3}=\\
\frac{cumsum\left(\left(((CoP_{y}[n+1]-range(CoP_{y}[n-1]))-(CoP_{y}[n-1]-range(CoP_{x}[n-1])))^2\right)^2\right)}
{\left| CoP_{y}[n+1]-\sum_{i=1}^{len(m)}\frac{psML[i]}{len(m)}\right|^{\sqrt{2}}}
```

## Genetic-frequency

```math
genetic-frequency = \\
\frac{ \sum_{i=1}^{len(m)}(m*\beta)^8*psRD[i] }{
\gamma -  \sum_{i=1}^{len(m)} \left( \frac{\left( \sum_{i=1}^{len(m)} \frac{frequency_{item10}} {frequency_{item9} } * psRD[i] \right) - 2}{ frequency_{item4} } * psML[i] \right)
}
```

 Where, $\beta$ is $-72.99423513659278$, $\gamma$ is $0.01666$, and $m$ is a vector containing the indices of $freq$, and frequency items 1 to 10 are:

```math
frequency_{item1}= \sum_{i=1}^{len(m}((((m*\gamma)^4)*psRD[i])^4)*psRD[i]
```

```math
frequency_{item2}= \left(\sum_{i=1}^{len(m)}((m*\beta)*psML[i])\right) \bmod{2}
```

```math
frequency_{item3} =  \left(\sum_{i=1}^{len(m)} (2*m)*psML[i] \right) \bmod 2
```

```math
frequency_{item4}= \left( \sum_{i=1}^{len(m)} psML[i]\right)*\left( 
 \sum_{i=1}^{len(m)} ((m*2)+71.07565684634866) \right)
```

```math
frequency_{item5}= \left( \sum_{i=1}^{len(m)} psML[i]\right)*\left( 
 \sum_{i=1}^{len(m)} ((m*31.975821823865573)+2) \right)
```

```math
frequency_{item6} = 1 - \frac{frequency_{item3}}{frequency_{item1} * \sum_{i=1}^{len(m)} \frac{frequency_{item2}}{  \frac{m^\gamma}{2}    }}
```

```math
frequency_{item7} = \\ 
\sum_{i=1}^{len(m)}\frac{\left( \sum_{i=1}^{len(m)}\left(\frac{\left(\sum_{i=1}^{len(m)}frequency_{item6}*psRD[i]\right)-2}{frequency_{item5}}\right)*psML[i]\right) \bmod 2}{   \frac{m^\gamma}{2}    } \bmod 2
```

```math
frequency_{item8} = 
\\
1 - \frac{frequency_{item7}}{frequency_{item1} * \sum_{i=1}^{len(m)} {\left(
 \frac{ \gamma - \left( \sum_{i=1}^{len(n)} \frac{(\sum_{i=1}^{len(m)} (1- frequency_{item6}) * psRD) -2}{ frequency_{item4}} * psML \right) \bmod 2}{  \frac{m^\gamma}{2}    } \right)  }}
```

```math
    frequency_{item9} = 
    \\
    frequency_{item1} * \sum_{i=1}^{len(m)} \frac{ \sum_{i=1}^{len{m}}\left(\frac{\left(\sum_{i=1}^{len(m)}frequency_{item8}*psRD[i]\right)-2}{frequency_{item5} }  * psML[i] \right) \bmod 2}{ \frac{m^\gamma}{2}   } 
```

```math
    frequency_{item10} = \sum_{i=1}^{len(m)} \left( \left( 1 - 
 \frac{(\sum_{i=1}^{len(m)}(4*m^2) * psML[i]) \bmod 2}{ frequency_{item9} } \right) * psRD[i] \right) -2
```


## Genetic-entropy:
```math
    genetic-entropy =
    \\
    \frac{\sum_{i=1}^{len(psRD)} psRD[i] \bmod \cos (psRD[i] -\log_{10}(entropy_{item2}))}{len(psRD)}
```

Where $entropy-items$ are:

```math
entropy_{item1} = 
psRD[i] \bmod \frac{\sum_{i=1}^{len(psML)} \left( psML[i]- \sin \left(\frac{\sum_{i=1}^{len(psML)} psML[i] - \frac {\sum_{i=1}^{len(psRD)} psRD[i]}{len(psRD)}}{len(psML)} * psRD[i]\right) \right)}{len(psML)}
```

```math
entropy_{item2} = \\
   psRD[i]\bmod  
   \\
   \frac{\sum_{i=1}^{len(psML)} \left( psML[i] - \sin \left( psRD[i]\bmod \frac{\sum_{i=1}^{len(psML)} psML[i] - \sin(entropy_{item1})} {len(psML)} \right) \right)}{len(psML)}
```

## Genetic-fall risk

```math
\text{genetic-fall risk} = 
\\
\sum_{i=0.15}^{5}\{ freq[i] : \cos((54.84 * m + 67.49) * psRD[i]) \leq -77.82 * Cov(psML[i]), i \in \mathbb{N} \}
```

Where $Cov$ refers to the covariance matrix, $freq$ is the vector of frequencies contained from 0.15 to 5 Hz of the $psRD$ spectrum, and $m$ is a vector containing the indices of $freq$.
