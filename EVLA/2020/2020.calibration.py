# Date: 20 August 2024
# Observation Date: 30 April 2020

# This document contains the script for calibrations for the above mentioned
# observation date

# CALIBRATIONS

# Antenna Position Corrections
gencal(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
	   caltable='2020.antpos',caltype='antpos')

# Intial Flux Density Scaling
setjy(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms', listmodels=True)

setjy(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',field='3C286',standard='Perley-Butler 2017',
      model='3C286_C.im',usescratch=True,scalebychan=True,spw='')

# Intial Phase Calibration
gaincal(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms', caltable='2020.intial.phase', 
        field='0,1', refant='ea14',
        gaintype='G',calmode='p', solint='int', 
        minsnr=5, gaintable=['2020.antpos'])

plotms(vis='2020.intial.phase',xaxis='time',yaxis='phase',
        coloraxis='corr',iteraxis='antenna',plotrange=[-1,-1,-180,180])
# If any antenna looks bad, then flag it.

# For the bandpass solution, we only need to solve for bandpass calibrator, ie. 3C286
gaincal(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms', caltable='2020.phase', 
        field='3C286', refant='ea14', calmode='p', solint='int', 
        minsnr=5, gaintable=['2020.antpos'])

plotms(vis='2020.phase',
        xaxis='time',yaxis='phase',coloraxis='corr',field='3C286',iteraxis='antenna',
        plotrange=[-1,-1,-180,180])

# Delay Calibration
gaincal(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',caltable='2020.delay', 
        field='3C286',refant='ea14', gaintype='K', 
        solint='inf',combine='scan',minsnr=5,
        gaintable=['2020.antpos',
                   '2020.phase'])

plotms(vis='2020.delay',xaxis='antenna1',yaxis='delay',coloraxis='baseline')
