# Date: 11 July 2024

# source: AM481
# observation.49965.9681829
# Observation Date: 5 September 1995
# Expected Flux Density: < 0.28 mJy

# Importing data

importvla(archivefiles = ['AM481_1_49965.96818_49966.09179.exp'], vis = 'am481.ms')

listobs(vis='am481.ms', listfile='am481.listobs.txt') 

vishead(vis='am481.ms')

plotants(vis='am481.ms', figfile = 'am481_plotants.png')

# Reference antenna: VA27

# Data Flagging

# scan='1', field='0'
flagdata(vis='am481.ms', scan='1', field='0', timerange='1995/09/05/23:14:45~23:18:30')

# scan='7', field='4'
flagdata(vis='am481.ms', scan='7', field='4', timerange='1995/09/05/23:58:10~23:58:20')

# scan='14', field='1'
flagdata(vis='am481.ms', scan='14', field='1', timerange='1995/09/06/00:48:24.5~00:48:25.5')
flagdata(vis='am481.ms', scan='14', field='1', antenna='VA18&VA20')

# scan='18', field='1'
flagdata(vis='am481.ms', scan='18', field='1', timerange='1995/09/06/01:14:20~01:14:30')

# scan='20', field='1'
flagdata(vis='am481.ms', scan='20', field='1', antenna='VA18&VA20')
flagdata(vis='am481.ms', scan='20', field='1', timerange='1995/09/06/01:27:44~01:27:46')

# scan='22', field='1'
flagdata(vis='am481.ms', scan='22', field='1', timerange='1995/09/06/01:41:00~01:41:10')

# Data flagging is complete

# Calibrations 

# target: TERZAN1
# gain calibrator: 1748-253 [1]
# flux calibrator: 1328+307 [0]

default('setjy')
setjy(vis='am481.ms', field='1328+307', model='3C286_C.im', usescratch=True)

gencal(vis='am481.ms', caltype='gc', caltable='gc.cal')

gaincal(vis='am481.ms',caltable='cal.G', field='1328+307, 1748-253', solint='inf', refant='VA27', gaintable='gc.cal', append=False)

plotms(vis='cal.G', coloraxis='Antenna1', yaxis='amp', xaxis='time', plotfile='cal.G.png')

myFluxes = fluxscale(vis='am481.ms', caltable='cal.G', reference='1328+307', transfer='1748-253', fluxtable='cal.Gflx', append=False)

applycal(vis='am481.ms', field='TERZAN1', gaintable='cal.Gflx', gainfield='1748-253')

default('blcal')
vis = 'am481.ms'
# output baseline-based calibration solutions
caltable = 'cal.BL' 
# use the strong flux density scale calibrator to determine baseline-based solutions
field = '1328+307' 
# generate a solution for each calibrator scan
solint = 'inf' 
gaintable = 'cal.Gflx'
# calibration table with the best antenna-based solutions, so far
gainfield = '1328+307' 
# calibrator for the BL calibrator; in this example, gain cal and bl cal are the same
interp = 'nearest'
blcal()

applycal(vis='am481.ms', field='TERZAN1', gaintable=['cal.Gflx', 'cal.BL'], gainfield='1748-253')

split(vis='am481.ms', outputvis='TERZAN1.ms', field='TERZAN1', datacolumn='corrected')

# Imaging
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
imagename           =      'TERZAN1_img'
rmtables(imagename + '*')
tclean()

# To fit a model and to get 
imfit(imagename='TERZAN1_img.image', box='510,510,513,513')
# When I run imfit, I get the following error: 
2024-07-11 17:36:19	SEVERE	imfit::ComponentShape::fromPixel(...)	DirectionCoordinate conversion to pixel failed because wcslib wcsp2s error: One or more of the pixel coordinates were invalid
2024-07-11 17:36:19	WARN	imfit::ImageFitter::_fitLoop	Fit failed to converge because of exception: Fit converged but transforming fit in pixel to world coordinates failed. Fit may be nonsensical, especially if any of the following fitted values are extremely large: [1.87991e+36, -8.53807e+37, -2.48284e+38, 2.25134e+75, 4.93225e+36, 0]. The lower level exception message is 2024-07-11 17:36:19	SEVERE	imfit::ComponentShape::fromPixel(...)	DirectionCoordinate conversion to pixel failed because wcslib wcsp2s error: One or more of the pixel coordinates were invalid at File: src/code/imageanalysis/ImageAnalysis/ImageFitter.tcc, line: 1538
Out[33]: 
{'converged': array([False]),
 'pixelsperarcsec': array([1.33333333, 1.33333333]),
 'results': {'nelements': 0}}

# To get the rms
imstat(imagename='TERZAN1_img.image', box='500, 504, 519, 520', logfile='TERZAN1.1min.imstat.txt')
# Since I could not run imfit, i did not run imstat either

# Export image as .fits
exportfits(imagename='TERZAN1_img.image', fitsimage='TERZAN1.AM553.1min.fits')
