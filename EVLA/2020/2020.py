# Date: 19 August 2024
# Observation Date: 30 April 2020

# In this document, I am working on the data set of the year 2020. 

cd Desktop/Research/Ter1/EVLA_new/2020/extra/data/20A-440.sb38071857.eb38075778.58969.40988748842.1671971365

# To extract the data 
tar xzvf 20A-440.sb38071857.eb38075778.58969.40988748842.ms.tgz

listobs(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms', listfile='2020.listobs.txt')

plotants(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms', figfile='2020.plotants.png')

# Observer Log information
'''
1. ea26 data lost
2. ea12 data corrupted
'''

# Both ea09 and ea14 seem like good candidates to use as reference antennas
# I will use ea14 but I can also use ea09 later to see any differences

# 3C286: Bandpass, delay and flux
# J1744-3116: Amplitude, phase
# Ter1: Target


# FLAGGING

# since ea12 data is corrupted, let's flag it 
flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms', antenna='ea12')

# Quack Flagging
flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
	mode='quack', quackmode='beg', quackinterval=10.0)

# The first 3 scans are just for set up
# Additionally, it is contributing some really high points
# Let's flag that
flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
	scan='1')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
	scan='2')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
	scan='3')

# Let's take a look at my data now
plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
	selectdata=True, correlation='RR, LL', averagedata=True, avgchannel='64',
	coloraxis='field')

######################################
# Date: 20 August 2024

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        field='0', xaxis='time', yaxis='amp', iteraxis='scan', 
        coloraxis='baseline', correlation='RR, LL', avgchannel='64')

# Nothing looks way too out of the ordinary with the above plot
# But, let's investigate amp vs frequency

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        field='0', xaxis='freq', yaxis='amp', iteraxis='scan', 
        coloraxis='baseline', correlation='RR, LL', avgtime='60')

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        field='0', xaxis='freq', yaxis='amp', scan='4',iteraxis='baseline', 
        coloraxis='baseline', correlation='RR, LL', avgtime='60')

# Flagging

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        field='0', scan='4', antenna='ea02&ea20', correlation='RR, LL',
        xaxis='freq', yaxis='amp', coloraxis='spw')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea02&ea20', field='0', spw='45:24~35',
        timerange='2020/04/30/09:54:55.5~09:58:37.5')

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        field='0', scan='4', iteraxis='antenna', correlation='RR, LL',
        xaxis='freq', yaxis='amp', coloraxis='spw', avgtime='60')

# flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
#         scan='4', antenna='ea02&ea09; ea02&ea14; ea02&ea28; ea02&ea27', field='0', spw='45:23~38',
#         timerange='2020/04/30/09:54:55.5~09:58:37.5')

# flagmanager(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
#                 mode='restore', versionname='flagdata_7')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea02&ea09; ea02&ea14; ea02&ea28; ea02&ea17',
        field='0', spw='45:23~38',
        timerange='2020/04/30/09:54:55.5~09:58:37.5')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea02',
        field='0', spw='18:36~38',
        timerange='2020/04/30/09:54:55.5~09:58:37.5')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea02',
        field='0', spw='26:36~54',
        timerange='2020/04/30/09:54:55.5~09:58:37.5')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea02',
        field='0', spw='26:55~59',
        timerange='2020/04/30/09:54:55.5~09:58:37.5')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea01',
        field='0', spw='18:37',
        timerange='2020/04/30/09:54:55.5~09:58:37.5')

# Date: 21 August 2024

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', yaxis='amp', xaxis='time', correlation='RR, LL',
        avgtime='60', iteraxis='antenna', coloraxis='baseline')

# Date: 25 August 2024

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', xaxis='freq', yaxis='amp', correlation='RR, LL',
        iteraxis='antenna', coloraxis='spw', avgtime='60')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea06&ea22', spw='18:37')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea13&ea25; ea13&ea22; ea13&ea28', spw='18:37')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea09&ea17', spw='16:58~60')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea22&ea28', spw='18:37')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea24&ea25', spw='32:0')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea02&ea20; ea02&ea09', spw='45:23~53')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea02&ea20', spw='47:6')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', antenna='ea03&ea10; ea03&ea11', spw='13:55~59')

# Flagged scan='4'. Let's look at the scan without averaging it. 

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', correlation='RR, LL', coloraxis='baseline')

# there is a lot of bad data that we could not clean off. 

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', xaxis='freq', yaxis='amp', correlation='RR, LL',
        iteraxis='antenna', coloraxis='baseline')

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', xaxis='freq', yaxis='amp', correlation='RR, LL',
        iteraxis='antenna', coloraxis='baseline', avgchannel='64')


spw='18, 26, 45'

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', xaxis='freq', yaxis='amp', correlation='RR, LL',
         coloraxis='baseline', avgtime='60')

# 26 August 2024

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', xaxis='freq', yaxis='amp', correlation='RR, LL',
        coloraxis='baseline')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='18:37')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='18:36~41')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='26:36~41')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='26:54~59')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='26:51~53')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='18:33~44')]

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='44:45~47', antenna='ea08&ea22; ea01&ea08; ea22&ea28')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='45:2', antenna='ea08&ea22; ea01&ea08; ea08&ea22')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='45:22~25')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='45:32:36')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='45:52~53')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='4', spw='45:2')

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', xaxis='time', yaxis='amp', correlation='RR, LL',
        coloraxis='baseline')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='18:36~38')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='18:35~42')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='26:35~38')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='44:45', antenna='ea22, ea28, ea08')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:2', antenna='ea22, ea28, ea08')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='44:46', antenna='ea08&ea22;ea22&ea28')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:18', antenna='ea08&ea22;ea22&ea28')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:25')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:18')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:24~26')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:33~35', antenna='ea20, ea28, ea02, ea09')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:31~36', antenna='ea02,ea20, ea28, ea14')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:53', antenna='ea02,ea20, ea28, ea14')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='45:50~54', antenna='ea01, ea08, ea22, ea01')

# the bad data from the flux calibrator have been successfully cleaned now

# Let's look at the field now: 
plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        xaxis='time', yaxis='amp', correlation='RR, LL', coloraxis='spw', scan='5')

ea22&ea28; ea03&ea13; ea08&ea13; ea22&ea28; ea08&ea22; ea19&ea27
flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='18:33~44', antenna='ea22&ea28; ea03&ea13; ea08&ea13; ea22&ea28; ea08&ea22')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', spw='18:33~44', antenna='ea08&ea22;ea19&ea27')

# 27 August 2024

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='5', correlation='RR, LL', coloraxis='baseline')

# Data Flagging in scan='5' is complete. 

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='18:36~38')

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', correlation='RR, LL', coloraxis='baseline',
        spw='18')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', antenna='ea13', spw='18:29~46')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', antenna='ea08&ea13', spw='18')

# flagmanager(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
#          mode='restore', versionname='flagdata_54')


flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='18:28~47')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='18:3~63', antenna='ea03, ea02, ea01')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:29~39', antenna='ea03, ea02, ea01, ea07')

# flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
#         scan='6', spw='45' ,timerange='2020/04/30/10:05:40.00~10:05:41')

# flagmanager(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
#         mode='restore', versionname='flagdata_60')

# flagmanager(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
#         mode='restore', versionname='flagdata_61')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:33~34', timerange='2020/04/30/10:05:43~10:05:44')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:33~34')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:53')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='44:45~46')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:23~46')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:8~22', antenna='ea01, ea02, ea08, ea09')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:2', antenna='ea01&ea08; ea08&ea22; ea22&ea28')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:2', antenna='ea01&ea22; ea08&ea28')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45:47~59')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='45')

# 30 August 2024

plotms(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', xaxis='time', yaxis='amp', correlation='RR, LL',
        coloraxis='baseline')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='26:52~59')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='26:36~40')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', antenna='ea23', spw='26:49~62')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', antenna='ea09&ea17; ea06&ea17', spw='26')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', antenna='ea06, ea17', spw='46:4~31')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='46, 47')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='43:48~56', antenna='ea17, ea06')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='44:23~27', antenna='ea06&ea17; ea06&ea25')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='44:37~44', antenna='ea06&ea17; ea06&ea25')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='44:41~44')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='44:35~38', antenna='ea06; ea17' )

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='44:47~52', antenna='13&16')

flagdata(vis='20A-440.sb38071857.eb38075778.58969.40988748842.ms',
        scan='6', spw='44:47~50')
