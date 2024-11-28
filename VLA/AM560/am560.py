# Date: 12 July 2024

# AM560
# observation.50674.1328488
# Observation Date: 14 August 1997
# Expected Flux Density: < 0.29

# In this document, I am working on the source AM560. 
# Although, I already have the code that I sued for it, but I wrote those lines 
# of code in the very beginning. 
# I have learnt so much since then, so I would like to rewrite that code again

# The image does not have a point source, which I assume is consistent with the studies. 
# Alex will be the judge of that.  

# Importing data

cd Desktop/Research/Ter1/VLA_old/1995_97/AM560/new
importvla(archivefiles=['AM560_1_50674.13286_50674.21527.exp'], vis='am560.ms') 

listobs(vis='am560.ms', listfile='listobs.am560.txt') 

vishead('am560.ms')

plotants(vis='am560.ms', figfile='am560_plotants.png')

# Reference Antenna: VA13

# Data Flagging

# scan='1', field='0'
flagdata(vis='am560.ms', scan='1', field='0', spw='1', antenna='VA08&VA12', timerange='1997/08/14/03:21:00~03:25:00')

# scan='2', field='0'
flagdata(vis='am560.ms', scan='2', field='0', antenna='VA19')

# scan='3', field='1'
flagdata(vis='am560.ms', scan='3', field='1', timerange='1997/08/14/03:29:34~03:29:36')

# scan='5', field='1'
flagdata(vis='am560.ms', scan='5', field='1', timerange='1997/08/14/03:52:44~03:52:46')

# scan='9', field='1'
flagdata(vis='am560.ms', scan='9', field='1', timerange='1997/08/14/04:19:20~04:19:30')
flagdata(vis='am560.ms', scan='9', field='1', antenna='VA08&VA09', spw='1', timerange='1997/08/14/04:19:44~04:19:46')

# scan='11', field='1'
flagdata(vis='am560.ms', scan='11', field='1', timerange='1997/08/14/04:42:40~04:42:50')

# scan='14', field='1'
flagdata(vis='am560.ms', scan='14', field='1', timerange='1997/08/14/05:08:10~05:08:20')

# Data Flagging is complete

# Calibration

# Target: TERZAN1
# Gain Calibrator: 1751-253
# Flux Calibrator: 1331+305

default('setjy')
setjy(vis='am560.ms', field='1331+305', model='3C286_C.im', usescratch=True)

gencal(vis='am560.ms', caltype='gc', caltable='gc.cal')

gaincal(vis='am560.ms', caltable='cal.G', field='1331+305, 1751-253', solint='inf', refant='VA13', gaintable=['gc.cal'], append=False)
 
plotms(vis='cal.G', coloraxis='Antenna1', yaxis='amp', xaxis='time', plotfile='cal.G.png')

myFluxes = fluxscale(vis='am560.ms', caltable='cal.G', reference='1331+305', transfer='1751-253', fluxtable='cal.Gflx', append=False)

applycal(vis='am560.ms', field='TERZAN1', gaintable='cal.Gflx', gainfield='1751-253')

# In CASA
default('blcal')
vis = 'am560.ms'
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
blcal()

applycal(vis='am560.ms', field='TERZAN1', gaintable=['cal.Gflx', 'cal.BL'], gainfield='1751-253')

# Splitting
split(vis='am560.ms', outputvis='TERZAN1.ms', datacolumn='corrected', field='TERZAN1')

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
imagename           =      'TERZAN1_img'
rmtables(imagename + '*')
tclean()

# To fit a model and get flux 
imfit(imagename='TERZAN1_img.image', box='500, 509, 523, 533', logfile='TERZAN1.imfit.txt')

# To get the rms
imstat(vis='TERZAN1_img.image', box='', logfile='TERZAN1.imstat.txt')