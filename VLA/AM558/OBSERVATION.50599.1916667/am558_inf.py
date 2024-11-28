# Date: 30 June 2024
# In this document, I work with the source AM558 
# Observation Date: 31 May 1997
# with solint='inf'
# observation.50599.1916667
# However, the image seems to be really terrible so i did not run imfit and imstat yet. 


 # THIS DATA SET IS CORRUPTED
 
importvla(archivefiles = ['AM558_1_50599.19167_50599.52396.exp'], vis = 'am558.ms')

listobs(vis='am558.ms', listfile='am558.listobs.txt') 

vishead(vis='am558.ms') 

plotants(vis='am558.ms', figfile = 'am558_plotants.png')

# Reference Antenna: VA20

# Flagging

# field='0', scan='1'
flagdata(vis='am558.ms', antenna='VA12', spw='1', field='0', scan='1')

# field='3', scan='12'
flagdata(vis='am558.ms', antenna='VA03&VA11', field='3', scan='12', timerange='1997/05/31/06:31:20~06:31:30')

# field='1', scan='24'

flagdata(vis='am558.ms', antenna='VA27', field='1', scan='24')

# field='7', scan='27'
flagdata(vis='am558.ms', antenna='11&18', field='7', scan='27')

# Data flagging is now complete

# Calibrations

default setjy
inp
vis='am558.ms'
listmodels=True

# Model name for 1328+307 is 3C 286. 
# It is the same name as that of 1331+305.
# model='3C286_C.im'

setjy(vis='am558.ms', field='1328+307', model='3C286_C.im', usescratch=True)

gencal(vis='am558.ms', caltype='gc', caltable='gc.cal')

gaincal(vis='am558.ms', caltable='cal.G', field='1328+307, 1748-253', solint='inf', refant='VA20', gaintable='gc.cal', append=False)

plotms(vis='cal.G', coloraxis='Antenna1', yaxis='amp', xaxis='time')

fluxscale(vis='am558.ms', caltable='cal.G', reference='1328+307', transfer='1748-253', fluxtable='cal.Gflx', append=False)

applycal(vis='am558.ms', field='1328+307', gaintable='cal.Gflx', gainfield='1748-253')

default('blcal')
blcal(vis='am558.ms',
	caltable='cal.BL',
	solint='inf',
	gaintable='cal.Gflx',
	gainfield='1328+307',
	interp='nearest')

applycal(vis='am558.ms', field='1328+307', gaintable=['cal.Gflx', 'cal.BL'], gainfield='1328+307')

split(vis='am558.ms', outputvis='TERZAN1.split.ms', field='TERZAN1', datacolumn='corrected')

# Imaging

default('tclean')
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
vis                 =      'TERZAN1.split.ms'
imagename           =      'TERZAN1.AM558_img.image'
rmtables(imagename + '*')
tclean()
# This is the warning that I got: 
2024-06-30 07:36:49	WARN	SIImageStore::restore (file src/code/synthesis/ImagerObjects/SIImageStore.cc, line 2247)	Restoring with an empty model image. Only residuals will be processed to form the output restored image.

# The image seems to be really terrible. 
# It is indistinguishable so I do not even know if I should run imfit and imstat on it. 
# I will try it now with solint='1min' and solint='2min'

imfit(imagename='TERZAN1.AM558_img.image', box='507, 504, 520, 518', logfile='TERZAN1.imfit.txt')
# logfile created

imstat(imagename='TERZAN1.AM558_img.image', box='507, 504, 520, 518', logfile='TERZAN1.imstat.txt')
# logfile created

# since the flux density is so weak, I will try once creating a ms of 
# just TERZAN1 with the spw 0 and 1 and then see what happens 