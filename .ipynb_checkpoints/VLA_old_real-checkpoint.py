# Importing from the VLA Archive and Data Inspection


# So, we know that AM481 -> observation.49887.1873958 does not have the source
importvla(archivefiles = ['AM481_1_49887.18740_49887.39064.exp'], vis = 'am481.ms')
listobs('am481.ms', listfile='observ_log_am481_2')

vishead('am481.ms') # this will give a pared down version of the listobs output

plotants(vis='am481.ms', figfile = 'am481_plotants.png') # will create an antenna distributon of the antennas.

# Now, we try, observation. 49965.9681829
# So, we know that AM481 -> observation.49887.1873958 does not have the source
importvla(archivefiles = ['AM481_1_49965.96818_49966.09179.exp'], vis = 'am481.ms')
listobs('am481.ms',listfile='observ_log_am481_2')
# This is also not the source

# Now, we try the observation.49967.1316088
importvla(archivefiles = ['AM481_1_49967.13161_49967.19295.exp'], vis = 'am481_obs3.ms')
listobs('am481_obs3.ms', listfile='observ_log_am481_3')
# So, this is also not the source

# Now we will try AM553, observation.50708.0822801
importvla(archivefiles = [''], vis = 'am553_obs1.ms')
listobs('am553_obs1.ms', listfile='observ_log_am553_1')
# This is one of the sources YAAY!

# Now we will try AM553, observation.50714.9612153
importvla(archivefiles = [''], vis = 'am553_obs2.ms')
listobs('am553_obs2.ms ', listfile='observ_log_am553_2')
# This is also not the data

# Now, let's try AM558, observation.50599.1916667
importvla(archivefiles = [''], vis = 'am558_obs.ms')
listobs('am558_obs.ms', listfile='observ_log_am558_1')
# This is not the source either

# Now, let's try AM558, observation.50624.1409722
importvla(archivefiles = [''], vis = 'am558_obs2.ms')
listobs('am558_obs2.ms', listfile='observ_log_am558_2')
# This is one of the sources, Yaaay!

# Now, let's try AM560, observation.50674.1328588
importvla(archivefiles = [''], vis = 'am560_obs.ms')
listobs('am560_obs.ms', listfile='observ_log_am560')
# This may be the source. The date says 14 August but in the pdf, there is nothing on August 14 but on August 11
# Update: This is one of the sources

# So, the data that I need to work with are:

# 1. AM553, observation.50708.0822801
# 2. AM558, observation.50624.1409722
# 3. AM580, observation.50674.1328588

# Let's work with AM553 observation.50708.0822801 first 

# Questions:  
# 1. How do I figure out which sources to flag?
# 2. How do I choose my flux density scale calibrator field? 


Usually 1331+305 is used as the common flux density scale calibrator for VLA


# Date: 27 June 2024
# I have worked with all the sources above except one, i.e., AM558/observation.50599.1916667

# AM553
 - solint='1min'

 - solint='2min'

 - solint='inf'

 # AM 558/ observation.50624.1409722
 - solint='1min'

 - solint='2min'

 - solint='inf'

 # AM553.observation.50599.1916667
 - solint='1min'

 - solint='2min'

 - solint='inf'

