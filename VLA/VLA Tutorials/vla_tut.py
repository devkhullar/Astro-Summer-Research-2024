# VLA 5 GHz continuum survey of Seyfert galaxies 6.4.1
# We are using the sruvey AG733, which consists of observations of a handful of Seyfert galaxies (host to quasars)

# Our data for the old project has already been installed by Alex into this mac
# The whole project has been divided into steps

# 1. Importing from the VLA Archive and Preliminary Data Inspection
# We do not need to worry much about importing the data as it has already been installed. # Check Background information page to learn about some basic commands to work on the terinal

# Changing our directory to get the data
cd AG733

# To import the data in Casa, we use `importvla` command. Import VLA as in Very Large Array. So we use this command to import the vla data into a measurement set format that CASA can
# work with.
# In Casa, to get rid of any original version of the measurement set, we do
if os.path.exists('ag733.ms'): rmtables('ag733.ms')
# We do this to ensure that there is no conflict with any pre-existing data before importing the new data


importvla(archivefiles=['AG733_1_54078.16663_54078.27045.exp'],vis='ag733.ms')
# archivefiles: Name of input VLA archive file(s)
# 22-05-24: We tried using the import vla task but for some reason it does not work and gives the warning
#that all elements of the vector parameter must be a path that exists (at least one element of "['AG733_1_54078.16663_54078.27045.exp']" does not exist)
# We have sought alex's helpf
# 23-05-24: Okay, so it wasn't any problem. The thing was that we were working in the ag733.ms directory and we don't want to do that, ever, ever, ever.
# We always have to work with AG733 directory.

listobs('ag733.ms') 
# This will provide a list of scans, sources and their respective indices and antennas.

vishead('ag733.ms')
# This is very similar to what listobs does. But vishead will give a much concise view of the summary.


plotants(vis='ag733.ms', figfile='ag733_plotants.png')
# This will generate a plot of the antenna distribution,ie, the position of the antennae
# and will save it in a file named `ag733_plotants.png`.
# vis: use this to write the name of MS file, which will use the info on the antennas stored in the ms file
# figfile: Save the plotted figure to this file 

# ----------------------------------------------------------------------------------------

# 2. Viewing and Editing the Measurement Set

plotms()
# It brings up a graphical display that allows us to plot various displays of the graph
# In the tutorial, it is used to display the measurement set ag733.ms

# In our tutorial, we find that there is some bad data and we want to flag that. 
# we will use flagdata() to flag them and then we will plot our data again. 
# we note that the data from VA05, VA15 and VA22 are bad.

# flag the first 45 seconds as all antennas were not on the source
flagdata(vis='ag733.ms', timerange='2006/12/09/04:00:00~04:00:45')

# now we flag all the anamolies 
flagdata(vis='ag733.ms', antenna='VA15', timerange='2006/12/09/04:45:10.0~04:45:20.0')
flagdata(vis='ag733.ms', antenna='VA15', timerange='2006/12/09/06:12:30.0~06:14:10.0')
flagdata(vis='ag733.ms', antenna='VA05', timerange='2006/12/09/04:30:00.0~04:30:10.0')
flagdata(vis='ag733.ms', antenna='VA22', timerange='2006/12/09/06:28:10.0~06:28:20.0')
flagdata(vis='ag733.ms', timerange='2006/12/09/06:24:50.0~06:25:00.0')

# Now we plot the data again to see if it looks reasonable.
plotms()
# we made some amazing plots and also took some screenshots of them so that we can ask about them to Alex
# we also want to ask if we can save those plots, somehow.

# ----------------------------------------------------------------------------------------
# 3. Python interlude 

# First we define some variables which store calibrator and source information
FDS_callist = ['0137+331']
CG_callist = ['2250+143', '0119+321', '0237+288', '0239-025',
                '0323+055', '0339-017', '0423-013'] 
sourcelist = ['NGC7469', 'MRK0993', 'MRK1040', 'NGC1056', 'NGC1068',
              'NGC1194', 'NGC1241', 'NGC1320', 'F04385-0828',
              'NGC1667'] 
allcals = FDS_callist + CG_callist
print(allcals)

# It will also be helpful to have a way of referencing
# which complex gain calibrator should be assigned to which sourse.
# We do so by using a dictionary variable. 

calDict = {'NGC7469':'2250+143',
           'MRK0993':'0119+321', 
           'MRK1040':'0237+288', 
           'NGC1056':'0237+288',
           'NGC1068':'0239-025',
           'NGC1194':'0323+055',
           'NGC1241':'0323+055',
           'NGC1320':'0339-017',
           'F04385-0828':'0423-013',
           'NGC1667':'0423-013'} 

# ------------------------------------------------------------------------------------------
# 4. Calibration 

## We set the Flux Density Scale 
default setjy 
# this will fill the model column with the visibilities of a calibrator
inp 
# this will show the current and the possibile input parameters
vis = 'ag733.ms'
listmodel=True
go

# From the list of models, we will select 3C38_C.im and tell setjy to use this model and apply it to our observation if 0137+331.
# We will also tell setjy to set the usescratch parameter to True so that the value is written into the MODEL column 

setjy(vis='ag733.ms', field='0137+331', model='3C48_C.im', usescratch=True)
# vis: Name of the input visibility file
# field: we will give this parameter the name of the field
# model: model name
# usescratch: If True: the model visibility will be evaluated and saved on disk in the MODEL_DATA column.

#setjy will return a Python dictionary to the terminal and to the logger. 
# The amplitude value that setjy adjusted the flux density scale calibrator in the MODEL column is ~5.3 Jy for spw 0 and 1. 
# We then plot this by using plotms()''

# Now we determine the Calibration solutions
# At this stage, the data has an overall flux density scaling determined, but full gain solutions aren't there yet. 
# We use the gaincal task which will produce the table cal.G

# Delete any old versions of the calibration tables
# will give warning, but we can ignore it safely
rmtables('cal.G')
rmtables('gc.cal')

# We generate an antenna zenith-angle dependent gain curve calibration table 
gencal(vis='ag733.ms', caltype='gc', caltable='gc.cal')

# CAUTION 
# solint (solution interval) = 'inf', meaning average over entire scans of each calibrator in turn 
# This may not work. use '1min', or '2min'.
gaincal(vis='ag733.ms', caltable='cal.G', field=','.join(allcals), solint='inf',
		refant='VA05', gaintable=['gc.cal'], append=False)
plotms(vis='cal.G', coloraxis='Antenna1', yaxis='amp', xaxis='time',timerange='2006/12/09/04:0:0~06:30:0')

print allcals
print ','.join(allcals)

# Now we use the task fluxscale to boostrap the flux density scale calibrator onto the complex gain calibrations.
rmtables('cal.Gflx') # to remove any old versions of the calibration table 
myFluxes = fluxscale(vis='ag733.ms', caltable='cal.G', reference=','.join(FDS_callist),
					 transfer=','.join(CG_callist), fluxtable='cal.Gflx', append=False)
# Here the calibration table will be stored as 'cal.Gflx'.
# The python dictionary will also contain information about the flux density scaling and other info.
# We can check that by typing myFluxes in the prompt to see its contents. 


# Apply the Calibrations 
# we use the applycal. This will loop over sources and calibrators to properly match them. 
for source, calibrator in calDict.items():
	applycal(vis='ag733.ms', field=source,
			 gaintable='cal.Gflx', gainfield=calibrator)

# Baseline Based Corrections 

# this will not be of much help with what we are doing. However, when we will be playing with the real sources, it might come in handy. 
default('blcal')
# blcal : it will calculate the baseline-based calibration solution,ie, it will calculate the gain
vis='ag733.ms'
# output baseline-based calibration solutions
caltable = 'cal.BL'
# caltable: Name of the output gain calibration table (it is the name of the table)
# use the strong flux density scale calibratior to determine baseline bsed solutions
field = '0137+331'
# This will generate a solution for each calibrator scan
solint = 'inf'
gaintable = 'cal.Gflx'
gainfield = '0137+331'
# calibrator for the BL calibrator.
interp = 'nearest'
#enter the time range for the data
timerange = '2006/12/09/0:0:0~24:0:0'
blcal()
# blcal : it will calculate the baseline-based calibration solution,ie, it will calculate the gainpl

# this will generate the calibration table cal.BL. We can inspect the solutions using plotms(). 
# Now we have to use applycal again to apply both the antenna based and baseline based calibration solutions to the data. 
for source, calibrator in calDict.items():
    applycal(vis='ag733.ms', field = source,
            gaintable =['cal.Gflx', 'cal.BL'], gainfield=calibrator)
## Splitting the calibrated source data from the multisource measurement set

# to split the calibrated source data out of the measurement set, we use Casa task split()
# So what we are doing here is that we are splitting the calibrated source data from our multisource measurement set 
****** Question from Alex**********
splitfile = 'NGC1667.split.ms'
rmtables(splitfile) # to get rid of any old versions before splitting 
split(vis='ag733.ms', outputvis=splitfile, datacolumn='corrected', field='NGC1667')

&&&&&&&&&&&& How do we know that NGC1667 is the calibrated sourcelist


# instead of manually repeating the split task for each source, we will loop over the sources:
for source in sourcelist:
    splitfile = source + '.split.ms'
    rmtables(splitfile)
    split(vis='ag733.ms', outputvis=splitfile,
          datacolumn='corrected', field=source)


# IMAGING 
default(tclean)
# Reset task parameter values to the task’s default parameter values.

rmtables(imagename + '*')

tclean()
# tclean() is used for radio inferometric imaging

default(tclean)
for source in sourcelist:
    splitfile = source + '.split.ms'
    vis = splitfile
    imagename = source + '_img'
    rmtables(iamgenae + '*')
    tclean()


# SELF CALIBRATION 

# Now, we cannot do much with the faint sources, but we can show some residual calibration artifacts. We do so using the task `gaincal`,
# only this time, we will use the bright source itself as a calibrator.

# step i

source = 'NGC1068'
tget(tclean)
# tget : Recover saved values of the inputs to a task.
# tclean : Radio inferometric imaging 
vis = source + '.split.ms' 
imagename = source + '_img0'
interactive = True # this will trigger an interactive GUI at every major cycle boundary
niter = 500 # niter: maximum number of iterations 
cycleniter = 100 # Maximum number of minor-cycle iterations
go 

# step i + 1

# We should have a clean model for NGC 1068 stored in the visibility database. We can set up gaincal
# gaincal(): determines the gain from calibrator observations 

default('gaincal')
vis = source + '.split.ms'
caltable = source + '.gcal0'
gaintype = 'G'
calmode = 'p'
solint = '10 min'
minsnr = 3.0
gaintable = ''
field = source 
gainfield = source 
gaincal()


# Troubleshooting 
plotms(caltable, iteraxis='antenna', xaxis='time', yaxis='phase', plotrange=[-1,-1,-180,180])
# If I want a more detailed view of the phases:
plotms(caltable, iteraxis='antenna', xaxis='time', yaxis='phase', plotrange=[-1,-1,-20,20])

# Step i + 2

default('applycal')
vis = source + '.split.ms'
gaintable = source + '.gcal0'
gainfield = source 
go 

# applycal : apply calibration solutions to data 

# Now, we generate a new tclean model 
# tclean: Radio Inferometric Image Reconstruction 

tget(tclean)
imagename = source + '_img1'
go

# FURHTER STEPS 

tget(gaincal)
caltable = source + '.gcal1'
solint = '5 min'
go

plotms()

tget(applycal) # tget: Recover saved files of the input to the task
gaintable = source + '.gcal1'
go 

tget(tclean)
imagename = source + '_img2'
go 

# ONE LAST ITERATION: AMPLITUDE AND PHASE SELF CALIBRATION 
default('gaincal')
vis = source + '.split.ms'
caltable = source + '.gcalap'
gaintype = 'G'
calmode = 'ap'
solint = 'inf'
combine = ''
minsnr = 3.0
gaintable = source + '.gcal1'
gaincal()




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
vis = source + '.split.ms'
imagename = source + '_img2'
tclean()


 





