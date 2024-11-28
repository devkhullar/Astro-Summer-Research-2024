# Date: 11 July 2024 

# source: TERZAN 1
# observation.50714.9612153
# Observation Date: 23 September 1997
# Expected Flux Density: < 0.24


# Importing data
importvla(archivefiles=['AM553_1_50714.96122_50715.04084.exp'], vis='am553.ms')

listobs(vis='am553.ms', listfile='am553.listobs.txt')

vishead(vis='am553.ms')

plotants(vis='am553.ms', figfile='am553_plotants.png')
# I noticed that some of the antennas are missing 

# reference antenna: VA26
# Data flagging 

plotms(vis='am553.ms')

# scan='1', field='0'
flagdata(vis='am553.ms', scan='1', field='0', antenna='VA19&VA25')

# scan='2', field='0'
flagdata(vis='am553.ms', scan='2', field='0', antenna='VA08')
flagdata(vis='am553.ms', scan='2', field='0', antenna='VA19&VA25')
flagdata(vis='am553.ms', scan='2', field='0', timerange='1997/09/23/23:11:34~23:11:36')

# scan='3', field='1'
flagdata(vis='am553.ms', scan='3', field='1', timerange='1997/09/23/23:16:04.5~23:16:05.5')
flagdata(vis='am553.ms', scan='3', field='1', antenna='VA19')

# scan='9', field='1'
flagdata(vis='am553.ms', scan='9', field='1', antenna='VA19&VA25')

# scan='12', field='1'
flagdata(vis='am553.ms', scan='12', field='1', antenna='VA19&VA25')

# scan='13', field='7'

flagdata(vis='am553.ms', scan='13', field='7', antenna='VA08')
flagdata(vis='am553.ms', scan='13', field='7', timerange='1997/09/24/00:44:04~00:44:06')

# scan='14', field='8'
flagdata(vis='am553.ms', scan='14', field='8', antenna='VA26')
flagdata(vis='am553.ms', scan='14', field='8', antenna='VA10&VA13')

# scan='15', field='7'
flagdata(vis='am553.ms', scan='15', field='7', antenna='VA08')
flagdata(vis='am553.ms', scan='15', field='7', antenna='VA19&VA25')

# Calibrations

# Target: TERZAN1
# Gain Calibrator: 1751-253
# Flux Calibrator: 1331+305

default('setjy')
listmodels=True

setjy(vis='am553.ms', field='1331+305', model='3C286_C.im', usescratch=True)

gencal(vis='am553.ms', caltype='gc', caltable='gc.cal')

gaincal(vis='am553.ms', caltable='cal.G', field='1331+305, 1751-253', solint='inf', refant='VA26', gaintable=['gc.cal'], append=False)

plotms(vis='cal.G', coloraxis='Antenna1', yaxis='amp', xaxis='time', plotfile='cal.G.png')

myFluxes = fluxscale(vis='am553.ms', caltable='cal.G', reference='1331+305', transfer='1751-253', fluxtable='cal.Gflx', append=False)

applycal(vis='am553.ms', field='1331+305', gaintable='cal.Gflx', gainfield='1751-253')
      ...: 
The following MS spws have no corresponding cal spws in tab1885_984: 2 3 
2024-07-11 20:08:19	WARN	Calibrater::correct2 (VI2/VB2)	Spectral window(s) 2, 3, 
2024-07-11 20:08:19	WARN	Calibrater::correct2 (VI2/VB2)+	  could not be corrected due to missing (pre-)calibration
2024-07-11 20:08:19	WARN	Calibrater::correct2 (VI2/VB2)+	    in one or more of the specified tables.
2024-07-11 20:08:19	WARN	Calibrater::correct2 (VI2/VB2)+	    Please check your results carefully!


# In CASA
default('blcal')
vis = 'am553.ms'
# output baseline-based calibration solutions
caltable = 'cal.BL' 
# use the strong flux density scale calibrator to determine baseline-based solutions
field = '1331+305' 
# generate a solution for each calibrator scan
solint = 'inf' 
gaintable = 'cal.Gflx'
# calibration table with the best antenna-based solutions, so far
gainfield = '1331+305' 
# calibrator for the BL calibrator; in this example, gain cal and bl cal are the same
interp = 'nearest'
# enter the time range for the data
blcal()

applycal(vis='am553.ms', field='1331+305', gaintable=['cal.Gflx', 'cal.BL'], gainfield='1751-253')

split(vis='am553.ms', outputvis='TERZAN1.ms', field='TERZAN1', datacolumn='corrected')
The following MS spws have no corresponding cal spws in tab1885_1176: 2 3 
2024-07-11 20:08:56	WARN	Calibrater::correct2 (VI2/VB2)	Spectral window(s) 2, 3, 
2024-07-11 20:08:56	WARN	Calibrater::correct2 (VI2/VB2)+	  could not be corrected due to missing (pre-)calibration
2024-07-11 20:08:56	WARN	Calibrater::correct2 (VI2/VB2)+	    in one or more of the specified tables.
2024-07-11 20:08:56	WARN	Calibrater::correct2 (VI2/VB2)+	    Please check your results carefully!

# Imaging
# In CASA
default(tclean)
savemodel           =      'modelcolumn'
specmode            =      'mfs'        
niter               =      1000      
gain                =      0.1       
threshold           =      '4.5e-5Jy'      
deconvolver         =      'hogbom'            
cyclefactor         =      3              
interactive         =      False      
mask                =      []       
imsize              =      [1024, 1024]      
cell                =      ['0.75arcsec', '0.75arcsec']
stokes              =      'I'        
weighting           =      'natural'        
uvtaper             =      []      
pbcor               =      False      
pblimit             =      0.1 
selectdata          =      False                  
vis                 =      'TERZAN1.ms'
imagename           =      'TERZAN1.img'
rmtables(imagename + '*')
tclean()






# use a different reference antenna
# use a different solution interval




