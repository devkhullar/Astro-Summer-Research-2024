# Date: 14 July 2024 

# I am working on the project AM481
# observation.49887.1873958
# Observation Date: 19 June 1995

# Importing data
importvla(archivefiles=['AM481_1_49887.18740_49887.39064.exp'], vis='am481.ms')

listobs(vis='am481.ms', listfile='am481.listobs.txt')

vishead(vis='am481.ms')

plotants(vis='am481.ms', figfile='am481_plotants.png')

# Reference Antenna: VA03 

# Data Flagging

plotms(vis='am481.ms')

# scan='1', field='0'
flagdata(vis='am481.ms', scan='1', field='0', antenna='VA02', timerange='1995/06/19/04:34:50~04:37:30')
flagdata(vis='am481.ms', scan='1', field='0', timerange='1995/06/19/04:30:34~04:30:46')

# scan='4', field='1'
flagdata(vis='am481.ms', scan='4', field='1', timerange='1995/06/19/04:58:44~04:58:46')

# scan='9', field='5'
flagdata(vis='am481.ms', scan='9', field='5', timerange='1995/06/19/05:39:20~05:39:40')

# scan='11', field='6'
flagdata(vis='am481.ms', scan='11', field='6', timerange='1995/06/19/05:53:24.95~05:53:25.05')

# scan='16', field='1'
flagdata(vis='am481.ms', scan='16', field='1', timerange='1995/06/19/06:43:24~06:43:26')

# scan='26', field='1'
flagdata(vis='am481.ms', scan='26', field='1', antenna='VA17', timerange='1995/06/19/08:12:24~08:12:26')

# scan='31', field='8'
flagdata(vis='am481.ms', scan='31', field='8', antenna='VA14', timerange='1995/06/19/08:45:44.95~08:51:25.05')
flagdata(vis='am481.ms', scan='31', field='8', antenna='VA14', timerange='1995/06/19/08:51:44.95~08:52:45.05')

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

fluxscale(vis='am481.ms', caltable='cal.G', reference='1328+307', transfer='1748-253', fluxtable='cal.Gflx', append=False)

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
# I did not run this because the image does not have a point source
imfit(imagename='TERZAN1_img.image', box='510,510,513,513')

# To get the rms
imstat(imagename='TERZAN1_img.image', box='500, 504, 519, 520', logfile='TERZAN1.1min.imstat.txt')
# Since I could not run imfit, i did not run imstat either

# Export image as .fits
exportfits(imagename='TERZAN1_img.image', fitsimage='TERZAN1.AM481.fits')














