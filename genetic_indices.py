import numpy as np

class genetic_indices:
    def __init__(self, CoPx, CoPy):
        """
        Initializes the `genetic_indices` class to compute features derived from 
        stabilogram signals in the mediolateral (CoPx) and anteroposterior (CoPy) directions.

        Parameters
        ----------
        CoPx : pandas.Series
            Stabilogram in the mediolateral (ML) direction, typically in millimeters.
        CoPy : pandas.Series
            Stabilogram in the anteroposterior (AP) direction, typically in millimeters.

        Computed Attributes
        -------------------
        CoPrd : numpy.ndarray
            Resultant displacement of the center of pressure, defined as the square root 
            of the sum of squared centered displacements in both ML and AP directions.
        psRD : numpy.ndarray
            Power spectral density (PSD) of the resultant displacement CoPrd.
        psAP : numpy.ndarray
            PSD of the centered CoPy (AP direction).
        psML : numpy.ndarray
            PSD of the centered CoPx (ML direction).
        freq : numpy.ndarray
            Frequency vector (in Hz) corresponding to the computed power spectra.
        m : numpy.ndarray
            Frequency bin indices shifted by 9, useful for downstream spectral analysis.
        N : int
            Length of the original CoPx/CoPy time series.

        """
                
        # Statokinesiogram and stabilograms:
        # Store the input stabilograms
        self.CoPx = CoPx
        self.CoPy = CoPy
        # Compute the centered resultant CoP displacement
        self.CoPrd = ((CoPy - CoPy.mean()) ** 2 + (CoPx - CoPx.mean()) ** 2) ** 0.5
       
        # Power spectrograms and frequency vector
        # Compute power spectral densities (keep bins 9 to 300), the first 9 frequency bins (up to ~0.8 Hz) are excluded to remove low-frequency noise.
        self.psRD = (((1 / (100 * 6000)) * np.abs(np.fft.fft(self.CoPrd)[:6000 // 2 + 1]) ** 2) * 2)[9:301]
        self.psAP = (((1 / (100 * 6000)) * np.abs(np.fft.fft(CoPy - CoPy.mean())[:6000 // 2 + 1]) ** 2) * 2)[9:301]
        self.psML = (((1 / (100 * 6000)) * np.abs(np.fft.fft(CoPx - CoPx.mean())[:6000 // 2 + 1]) ** 2) * 2)[9:301]
        self.freq = (np.arange(0, 100 / 2 + 100 / len(self.CoPrd), 100 / len(self.CoPrd)))[9:301] # Generate frequency vector

        # Constants
        self.m = np.arange(len(self.freq)) + 9
        self.N = len(CoPx)

    def distance(self):
        """
        Computes the genetic-distance index
        """
        return np.sum(((((((((((((((((np.cumsum(self.CoPy)%12.277863138799631)**2)%86.10804463529303)%-91.8466414859989)%12.277863138799631)%-91.8466414859989)+89.13298467050618)%12.277863138799631)%4.6201196285114605)%-91.8466414859989)%89.13298467050618)-12.277863138799631)%4.6201196285114605)**2)**2)))
    
    def area(self):
        """
        Computes the genetic-area index
        """
        return np.sum((47.39785342553628*(18.8496*(-45.68985547558218%(18.8496*(18.8496%(18.8496*(self.CoPrd-(self.CoPy.mean())))))))))
    
    def hybrid(self):
        """
        Computes the genetic-hybrid index
        """
        return ((((((self.CoPy[1:].values-(((((self.CoPy[1:].values-((self.CoPx-(((((self.CoPy[1:].values-(self.CoPy[1:].values.mean()))-(self.CoPy[:-1].values-(self.CoPy[1:].values.mean())))**2)**0.5).sum())).sum()))-(self.CoPy[:-1].values-(self.CoPx[:-1].values.mean())))**2)**0.5).sum()))-(np.cumsum(((((self.CoPy[1:].values-np.ptp(self.CoPy[:-1].values))-(self.CoPy[:-1].values-np.ptp(self.CoPx[:-1].values)))**2)**2))/((((self.CoPy[1:].values-(self.psML.mean()))**2)**0.5)**(2**0.5))))**2)**0.5).sum())/(((2*(((((self.CoPy[1:].values-np.max(self.psML))**2)**0.5).max())/self.N))**(0.5**0.5))*4))
    
    def frequency(self):
        """
        Computes the genetic-frequency index
        """
        return ((((((((self.m*-72.99423513659278)**2)**2)**2)*self.psRD).sum())/((((0.01666-(((((((1-((((((self.m*2)**2)*self.psML).sum())%2)/(((((((((self.m*0.01666)**2)**2)*self.psRD)**2)**2)*self.psRD).sum())*((((((((((((1-((((((((((((((1-((((((self.m*2)**1)*self.psML).sum())%2)/(((((((((self.m*0.01666)**2)**2)*self.psRD)**2)**2)*self.psRD).sum())*((((((self.m*-72.99423513659278)*self.psML).sum())%2)/((self.m**0.01666)/2)).sum()))))**1)/1)*self.psRD).sum())-2)/((self.psML.sum())*(((self.m*31.975821823865573)+2).sum())))*self.psML).sum())%2)/((self.m**0.01666)/2)).sum())%2)/(((((((((self.m*0.01666)**2)**2)*self.psRD)**2)**2)*self.psRD).sum())*((((((((0.01666-(((((((1-((1-((((((self.m*2)**1)*self.psML).sum())%2)/(((((((((self.m*0.01666)**2)**2)*self.psRD)**2)**2)*self.psRD).sum())*((((((self.m*-72.99423513659278)*self.psML).sum())%2)/((self.m**0.01666)/2)).sum()))))**1))**1)/1)*self.psRD).sum())-2)/((self.psML.sum())*(((self.m*2)+71.07565684634866).sum()))))**1)**1)*self.psML).sum())%2)/((self.m**0.01666)/2)).sum()))))**1)/1)*self.psRD).sum())-2)/((self.psML.sum())*(((self.m*31.975821823865573)+2).sum())))*self.psML).sum())%2)/((self.m**0.01666)/2)).sum()))))**1)/1)*self.psRD).sum())-2)/((self.psML.sum())*(((self.m*2)+71.07565684634866).sum()))))**1)*self.psML).sum()))**1)

    def entropy(self):
        """
        Computes the genetic-entropy index
        """
        return ((self.psRD%np.cos((self.psRD-np.log10((self.psRD%((self.psML-np.sin((self.psRD%((self.psML-np.sin((self.psRD%((self.psML-np.sin((self.psRD*((self.psML-np.mean(self.psRD)).mean())))).mean())))).mean())))).mean())))))).mean())

    def fall_risk(self):
        """
        Computes the genetic-fall risk index
        """
        return np.sum(self.freq[np.where((np.cos((((self.m*54.84222851382691)+67.49594105804479)*self.psRD))<=(np.cov(self.psML)*-77.82901199371551)))])


    