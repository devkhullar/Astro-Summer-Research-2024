# Date: 27 June 2024

# In this document, I work with the project AM553. I use the solution
# intervals, solint='inf' while calibrating the data

# Observation Date: 17-Sep-1997

importvla(archivefiles = ['AM553_1_50708.08228_50708.18483.exp'], vis = 'am553.ms')

listobs(vis='am553.ms', listfile='observation.log_am553') 

vishead(vis='am553.ms')

plotants(vis='am553.ms', figfile = 'am553_plotants.png')

# Reference antenna: VA24

# Data flagging: I am doing data flagging again and not using the previous code.

# field='0', scan='2'
flagdata(vis='am553.ms', field='0', scan='2', antenna='VA08')

flagdata(vis='am553.ms', field='0', scan='2', antenna='VA03', timerange='1997/09/17/02:10:10~02:10:20')

flagdata(vis='am553.ms', field='0', scan='2', timerange='1997/09/17/02:09:04~02:09:06')

# field='1', scan='5'
flagdata(vis='am553.ms', field='1', scan='5', timerange='1997/09/17/02:31:24~02:31:26')

# field='2', scan='6'
flagdata(vis='am553.ms', field='2', scan='6', antenna='VA05&VA13')

# field='6', scan='16'
flagdata(vis='am553.ms', field='6', scan='16', antenna='6')

flagdata(vis='am553.ms', field='6', scan='16', antenna='8&11')

flagdata(vis='am553.ms', field='6', scan='16', antenna='1&3', timerange='1997/09/17/04:11:04~04:11:06')

# field=;7, scan='17'                              
flagdata(vis='am553.ms', field='7', scan='17', antenna='3&8')

flagdata(vis='am553.ms', field='7', scan='17', antenna='16&17')

flagdata(vis='am553.ms', field='7', scan='17', antenna='VA18&VA21')

# field='6', scan='18'
flagdata(vis='am553.ms', field='6', scan='18', antenna='VA09', timerange='1997/09/17/04:25:10~04:25:20')
flagdata(vis='am553.ms', field='6', scan='18', antenna='VA16,VA22', timerange='1997/09/17/04:25:10~04:25:20')
flagdata(vis='am553.ms', field='6', scan='18', timerange='1997/09/17/04:23:50~04:24:00')
flagdata(vis='am553.ms', field='6', scan='18', antenna='VA08')
flagdata(vis='am553.ms', field='6', scan='18', antenna='VA10&VA13')
flagdata(vis='am553.ms', field='6', scan='18', antenna='VA05&VA21', timerange='1997/09/17/04:25:10~04:25:20')
flagdata(vis='am553.ms', field='6', scan='18', antenna='VA06&VA14', timerange='1997/09/17/04:25:10~04:25:20')

# Data flagging is complete

# Calibrations 

default setjy
setjy(vis='am553.ms', field='1331+305', model='3C286_C.im', usescratch=True)
# I used the same model for AM560. These two projects have the same FDSC and CG

gencal(vis='am553.ms', caltype='gc', caltable='am553.gc.cal')

gaincal(vis='am553.ms',caltable='am553.cal.G', field='1331+305, 1751-253', solint='inf', refant='VA24', gaintable='am553.gc.cal', append=False)

plotms(vis='am553.cal.G', coloraxis='Antenna1', yaxis='amp', xaxis='time')

fluxscale(vis='am553.ms', caltable='am553.cal.G', reference='1331+305', transfer='1751-253', fluxtable='am553.cal.Gflx', append=False)

applycal(vis='am553.ms', field='TERZAN1', gaintable='am553.cal.Gflx', gainfield='1751-253')
# The following MS spws have no corresponding cal spws in tab778_2002: 2 3 

default('blcal')
vis = 'am553.ms'
# output baseline-based calibration solutions
caltable = 'am553.cal.BL' 
# use the strong flux density scale calibrator to determine baseline-based solutions
field = '1331+305' 
# generate a solution for each calibrator scan
solint = 'inf' 
gaintable = 'am553.cal.Gflx'
# calibration table with the best antenna-based solutions, so far
gainfield = '1331+305' 
# calibrator for the BL calibrator; in this example, gain cal and bl cal are the same
interp = 'nearest'
blcal()

# Below is what CASA output
Found no unflagged data at:   (time=1997/09/17/02:08:50.0 field=0 spw=2 chan=0)
Found no unflagged data at:   (time=1997/09/17/02:08:50.0 field=0 spw=3 chan=0)

applycal(vis='am553.ms', field='TERZAN1', gaintable=['am553.cal.Gflx', 'am553.cal.BL'], gainfield='1751-253')
# Below is the CASA output
The following MS spws have no corresponding cal spws in tab778_2259: 2 3 

split(vis='am553.ms', outputvis='TERZAN1.553.ms', field='TERZAN1', datacolumn='corrected')

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
vis                 =      'TERZAN1.553.ms'
imagename           =      'TERZAN1.553_img'
rmtables(imagename + '*')
tclean()

imfit(imagename='TERZAN1.553_img.image', box='500, 502, 523, 527', logfile='TERZAN1.imfit.txt')

imfit(imagename='TERZAN1.553_img.image', box='500, 504, 519, 520', logfile='TERZAN1.imfit.txt')

imstat(imagename='TERZAN1.553_img.image', box='500, 504, 519, 520', logfile='TERZAN1.imstat.txt')

exportfits(imagename='TERZAN1.553_img.image', fitsimage='TERZAN1.inf.fits')


