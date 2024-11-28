# Date: 31 July 2024

# In this document, I am writing the code for the calibrations
# to be applied on the datasets of the year 2022

# Calibrating the Data
gencal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	   caltable='SI1065.antpos',caltype='antpos')

# Initial Flux Density scaling

setjy(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	  field='0',standard='Perley-Butler 2017',
      model='3C286_C.im',usescratch=True)

## Phase Calibration
gaincal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
 caltable='SI1065.phase.cal', 
        field='0,1', refant='ea28',
        gaintype='G',calmode='p', solint='int', 
        gaintable=['SI1065.antpos'])

plotms(vis='SI1065.phase.cal',
		xaxis='time', yaxis='phase', coloraxis='corr', iteraxis='antenna') # plotrange=[-1, -1, -180, 180]

# should see a smooth variation with time. 
# if any antenna looks bad, flag it

# everything looks beautiful except antenna ea26, just going to flag that
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	antenna='ea26')

# for our data, we only need to use the bandpass calibrator
gaincal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
 caltable='SI1065.phase.cal.required', 
        field='0', refant='ea28',
        calmode='p', solint='int', 
        gaintable=['SI1065.antpos'])

plotms(vis='SI1065.phase.cal.required',
		xaxis='time', yaxis='phase', coloraxis='corr', iteraxis='antenna',plotrange=[-1, -1, -180, 180]) # plotrange=[-1, -1, -180, 180]

#### Something looks sketchy in ea10. I am not going to flag it to see what happens

## Delay Calibration
gaincal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	caltable='SI1065.delay.cal',
		field='3C286', refant='ea28', gaintype='K',
		solint='inf', combine='scan',
		gaintable=['SI1065.antpos',
		           'SI1065.phase.cal.required'])

# Plot to inspect solutions as a function of time. 
# They should be within 4 nanoseconds
plotms(vis='SI1065.delay.cal',
	   xaxis='antenna1', yaxis='delay', coloraxis='baseline')

## Bandpass Calibration
bandpass(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	     caltable='SI1065.bandpass.cal',
	     field='3C286',spw='',refant='ea28', combine='scan',
	     solint='inf', bandtype='B',
	     gaintable=['SI1065.antpos',
			  'SI1065.phase.cal.required',
			  'SI1065.delay.cal'])

# To inspect the solutions
plotms(vis='SI1065.bandpass.cal', field='0',
	xaxis='chan', yaxis='amp', coloraxis='corr',
	iteraxis='antenna', gridrows=2, gridcols=2)

plotms(vis='SI1065.bandpass.cal', field='0',
	xaxis='chan', yaxis='phase', coloraxis='corr',
	iteraxis='antenna', gridrows=2, gridcols=2,plotrange=[-1,-1,-180,180])
# everything looks amazing

# Gain Calibration

# to derive solutions for the complex antenna gains

# first for the flux calibrator
gaincal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	   caltable='SI1065.cal.G',
	   field='0', solint='inf', refant='ea28', gaintype='G',
	   calmode='ap', solnorm=False,
	   gaintable=['SI1065.antpos',
			'SI1065.delay.cal',
			'SI1065.bandpass.cal'],
		interp=['','','nearest'])

# now on the phase calibrator
gaincal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	   caltable='SI1065.cal.G',
	   field='1', solint='inf', refant='ea28', 
	   gaintype='G',calmode='ap',
	   gaintable=['SI1065.sb41775211.antpos',
				   'SI1065.delay.cal',
				   'SI1065.bandpass.cal'],
		append=True)

# to check the solutions
plotms(vis='SI1065.cal.G',
	   xaxis='time', yaxis='phase', gridrows=1, gridcols=2, iteraxis='corr',
	   coloraxis='baseline', plotfile='plotms_gain_phase.png',
	   plotrange=[-1, -1, -180, 180])  

plotms(vis='SI1065.cal.G',
	   xaxis='time', yaxis='amp', gridrows=1, gridcols=2, iteraxis='corr',
	   coloraxis='baseline', plotfile='plotms_gain_amp.png')

# to check if reference antenna has good phase stability
plotms(vis='SI1065.cal.G',
	xaxis='time', yaxis='phase', correlation='/',
	coloraxis='baseline',plotrange=[-1, -1, -180, 180])


# if there are no phase jumps, then everything is good

## Scaling Amplitude gains
myscale = fluxscale(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
                    caltable='SI1065.cal.G',
                    fluxtable='SI1065.fluxscale',
                    reference='3C286', transfer='J1744-3116 ',
                    incremental=False)

# plotting the rescaled amplitudes
plotms(vis='SI1065.fluxscale',
	   xaxis='time', yaxis='amp', correlation='R', coloraxis='baseline')

plotms(vis='SI1065.fluxscale',
	   xaxis='time', yaxis='amp', correlation='L', coloraxis='baseline')

# They should be similar across sources

# Applying the Calibrations to the calibrators first

applycal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	     field='3C286',
	     gaintable=['SI1065.antpos',
	     		  'SI1065.fluxscale',
			   'SI1065.delay.cal',
			   'SI1065.bandpass.cal'],
	    gainfield=['','3C286','',''],
	    interp=['','nearest','',''], calwt=False)

applycal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	     field='J1744-3116',
	     gaintable=['SI1065.antpos',
	                'SI1065.fluxscale',
		         'SI1065.delay.cal',
			   'SI1065.bandpass.cal'],
	    gainfield=['','J1744-3116','',''],
	    interp=['','nearest','',''], calwt=False)

applycal(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	  field='Ter1', gaintable=['SI1065.antpos',
	                           'SI1065.fluxscale',
				      'SI1065.delay.cal',
				      'SI1065.bandpass.cal'],
	  gainfield=['','J1744-3116','',''], interp=['','linear','',''], calwt=False)

# To inspect our results
plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	field='0', correlation='RR, LL', antenna='', avgtime='60', xaxis='channel',
	yaxis='amp', ydatacolumn='corrected', coloraxis='corr', 
	plotfile='plotms_SI1065-fld0-corrected-amp.png')

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	field='0', correlation='RR, LL', antenna='', avgtime='60', xaxis='channel',
	yaxis='phase', ydatacolumn='corrected', coloraxis='corr', 
	plotfile='plotms_SI1065-fld0-corrected-phase.png', plotrange=[-1, -1, -180, 180])
# plotrange=[-1, -1, -180, 180]

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms', 
	field='1', correlation='RR, LL', antenna='', avgtime='60', xaxis='channel',
	yaxis='amp', ydatacolumn='corrected', coloraxis='corr',
	plotfile='plotms_SI1065-fld1-corrected-amp.png')

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms', 
	field='1', correlation='RR, LL', antenna='', avgtime='60', xaxis='channel',
	yaxis='phase', ydatacolumn='corrected', coloraxis='corr',
	plotfile='plotms_SI1065-fld1-corrected-phase.png',
	 plotrange=[-1, -1, -180, 180])
# the last photo does not look so good 

# the plots should look relatively smooth

split(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	outputvis='SI1065_split.ms', datacolumn='corrected', field='Ter1',
	correlation='RR, LL')

# to correct data weights
statwt(vis='SI1065_split.ms',datacolumn='data')

# Imaging
plotms(vis='SI1065_split.ms', xaxis='uvwave', yaxis='amp', ydatacolumn='data',
	field='0', avgtime='30', correlation='RR',
	plotfile='plotms_SI1065-uvwave.png', overwrite=True)

tclean(vis='SI1065_split.ms',
       imagename='SI1065_ter1-2022.img',
	field            =    'Ter1',
	specmode         =     'mfs', 
	niter            =     5000,
	threshold        =     '0.01mJy',
	deconvolver      =      'hogbom',
	interactive      =      True,
	imsize           =      [4096, 4096],
	cell             =      ['0.1arcsec'],
	stokes           =      'I',
	weighting        =      'natural',
	pbcor            =       False,
	pblimit          =       0.1,
	savemodel        =      'modelcolumn')

# to calculate the cell size, check the configuration of the array


arcminutes is θPB = 42/νGHz, ie, 42 / frequency in Ghz (https://science.nrao.edu/facilities/vla/docs/manuals/oss/performance/fov)
i work with 6Ghz frequency so 42/6 = 7

there are 60 arcseconds in one arcminute
so 7*60 = 420 arcseconds

7*60/0.1 = 4200
We divide with 0.1 because that was the rough approximation we got

but we cannot use 4200 as our image size. 
we will have to use a power of 2: 2^12 works best there
2 ^ 12 = 4096

our image size is going to be 4096 then

cell size = 0.1arcsec


find the cofiguration on the website below
https://science.nrao.edu/facilities/vla/docs/manuals/oss/performance/resolution
for this project, the configuration was A and band was C so our resolution was 0.33

we divide 0.33 with 4 or 5, we just need a rough approximation 0.33/4=0.085
so we get 0.1 


# imfit
imfit(imagename='SI1065_ter1-2022.img.image', box='2030, 2045, 2043, 2057',
	logfile='SI1065_ter1-2022.imfit.txt')

2024-08-10 23:40:03 INFO imfit	Flux ---
2024-08-10 23:40:03 INFO imfit	       --- Integrated:   36 +/- 13 uJy
2024-08-10 23:40:03 INFO imfit	       --- Peak:         11.0 +/- 3.2 uJy/beam
2024-08-10 23:40:03 INFO imfit	       --- Polarization: I

imstat(imagename='SI1065_ter1-2022.img.image', box='2030, 2045, 2043, 2057',
	logfile='SI1065_ter1-2022.imstat.txt')

exportfits(imagename='SI1065_ter1-2022.img.image', fitsimage='SI1065_ter1-2022.fits.image.png')
