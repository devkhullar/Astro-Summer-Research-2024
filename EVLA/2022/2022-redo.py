# Date: 6 August 2024

'''In this document, I am working on the 2022 data sets. Here I am trying to
flag the data set'''

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
       xaxis='time', yaxis='amp', iteraxis='scan', coloraxis='spw',
       averagedata=True, avgchannel='64', correlation='RR, LL')

# it is mentioned in the observer's log that ea05 is corrupted

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	antenna='ea05')

# Quack Flagging
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	mode='quack', quackmode='beg', quackinterval=10.0)

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	xaxis='freq', yaxis='amp', iteraxis='antenna', coloraxis='channel',
	averagedata=True, avgtime='60s', scan='6', correlation='RR, LL')

# scan='6'
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', spw='30')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea03&ea23',spw='47:10~13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea03&ea12',spw='47:10~13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea06',spw='33:36~53')

flagmanager(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		mode='restore', versionname='flagdata_8')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea06',spw='33:36~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea06',spw='33:32~59')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea06',spw='34:21~34')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea10&ea23', spw='33:41~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea10&ea23', spw='35:5~20')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea10&ea23', spw='47:13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea10&ea23', spw='37:31')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea10&ea23', spw='35:21~23')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', antenna='ea10&ea23', spw='34:32')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea02&ea11', spw='33:19')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea11&ea21', spw='33:26')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea11&ea26', spw='33:19~22')

# Wrong command, did not specify spw
# restored it later
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea11&ea27', spw='18~29')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea11&ea26', spw='33:19~22')

# I just realised that I forgot to give the spw command in the code above the one above
# I need to restore that
flagmanager(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		mode='restore', versionname='flagdata_21')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea11&ea27', spw='33:18~29')


flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea12&ea14; ea12&ea20; ea12&ea22; ea12&ea23',
		 spw='33:26~55')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea12&ea23',
		 spw='35:20~22')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea12&ea23',
		 spw='47:0~27')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea19', spw='33:17~29')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea19', spw='35:17~27')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea20&ea22', spw='33:42~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea15&ea20', spw='34:21~32')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea20&ea23', spw='33:42')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea21', spw='33:19~30')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea12&ea22', spw='47:12~13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea12&ea22', spw='47:9~16')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea22&ea25', spw='33:41~51')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea15&ea22', spw='33:43~48')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea22&ea23', spw='47:9~14')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea23&ea28', spw='12~13')

# Scan 6 finally done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# let's take a look at scan='6' itself without any averaging

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='6', xaxis='time', yaxis='amp', coloraxis='antenna1',
		correlation='RR, LL')

# It does not look  very good. There are still a lot many squiggly points

# Let's look at the averaged data for some hint
plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', averagedata=True, avgtime='60s', coloraxis='channel',
		correlation='RR, LL')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea22&ea25', spw='33:52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='06', antenna='ea22', spw='33:40~53')

# OKAY WOW MY SCAN LOOKS BEAUTIFUL!!!!!!!!!!!

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', yaxis='amp', xaxis='freq', iteraxis='antenna',
		coloraxis='channel', correlation='RR, LL')

# SCAN='8'

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea02', spw='30:10~12')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea02', spw='30:21~49')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', spw='30')
# I forgot to put in the antenna command
#flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	#	scan='08', spw='47:13',)

flagmanager(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		mode='restore', versionname='flagdata_47')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', spw='47:13', antenna='ea03')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea04&ea17', spw='24:3~15')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06&ea12;ea06&ea20;ea06&ea22;ea06&ea23', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06&ea20', spw='34:22~32')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06&ea22', spw='34:24~32')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06&ea22', spw='33:15~63')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06&ea22', spw='33:3~14')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06', spw='33:39~55')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06', spw='33:21~34')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06&ea20', spw='32:33')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06&20', spw='34:21')

# Date: 7 August 2024
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea06', spw='34:21~33')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea10&ea23', spw='33:40~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea10&ea23', spw='34:22~24')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea10&ea23', spw='35:17~20')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12&ea14', spw='33:41~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12&ea14', spw='33:41~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12', spw='33:19~56')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12&ea23', spw='47:13~20')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12&ea22', spw='47:13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12&ea23', spw='33:6~62')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12&ea23', spw='34:23~32')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea12&ea23', spw='35:18~26')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea15&ea22', spw='33:42~45')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea15&ea20', spw='34:20~23')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea19&ea26', spw='33:20')

# I made the mistake of writing ea20&22 instead of 'ea20&ea22'
# flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
# 		scan='08', antenna='ea20&22', spw='33:40~53')

# I need to correct that 
flagmanager(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		mode='restore', versionname='flagdata_71')

# Now the correct command
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea20&ea22', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea22&ea23', spw='47:13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea22', spw='33:42~53')

# for some reason, the command below did not do anything when I ran it earlier.
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		scan='08', antenna='ea22&ea23', spw='47:13')

# Okay scan='8' also looks very good!!!!!!!!!

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	yaxis='amp', xaxis='time', correlation='RR, LL',
	scan='8', coloraxis='baseline')

# I just checked the plot of scan='8' and it looks nice. No flagging required

# Moving on to scan='10'

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	yaxis='amp', xaxis='freq', scan='10', coloraxis='channel',
	iteraxis='antenna', correlation='RR, LL', averagedata=True, avgtime='60')

# spw='30' as expected is bad
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', spw='30')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea03&ea28',spw='47:13~14')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea04&ea19', spw='33:22~28')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea06&ea12; ea06&ea22; ea06&ea23', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea06&ea20', spw='34:20~34')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea06&ea12;ea06&ea22;ea06&ea20', spw='33')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea06&ea15', spw='33:42~49')

# flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
# 	scan='10', antenna='ea06&ea23', spw='39~61')

# I did not specify the spw in the above code, need to undo that
flagmanager(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
		mode='restore', versionname='flagdata_84')

# OH my god, why arent you getting flagged????
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='5&21', spw='33:39~61')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='8&21', spw='33:41~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='8&21', spw='35:6~13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12&ea20; ea12&23;ea12&ea22', spw='33:18~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12&ea23', spw='47:6~20')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12&ea22', spw='47:13~14')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12', spw='33:18~58')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12', spw='34,35:20~33')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12&ea22', spw='47:10~10',)

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12&ea23', spw='47:2~21')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12&ea23', spw='33:11~62',)

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12', spw='35:5~8',)

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea12&ea22', spw='47:12~20')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea15&ea22; ea15&ea23', spw='33:43~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea15&ea20', spw='34:19~36')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea20&ea22; ea20&ea23', spw='33:41~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea22', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea22', spw='34:20~33')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea21&ea22; ea22&ea23', spw='47:8~15')

# flagging of scan='10' is done 
# i am just going to take a look at the entire scan without any averaging of the amp vs time

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
       xaxis='time', yaxis='amp', scan='10', coloraxis='baseline',
       correlation='RR, LL')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='10', antenna='ea23&ea28', spw='47:13~14', timerange='2022/04/27/10:02:18.5~10:02:55.5')

# the scan='10' looks beautiful

# Let's look at scan='12' now
plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	yaxis='amp', xaxis='freq', scan='12', coloraxis='channel',
	iteraxis='antenna', correlation='RR, LL', averagedata=True, avgtime='60')

# I am going to flag spw='30' from the entire data set now
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms', spw='30')

# I realised the pattern with the baselines, there are a few antennas contributing to the bad data, namely ea23, ea20, ea22
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea23', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea22', spw='33:23~63')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea06&ea20;ea12&ea20', spw='33:41~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea06&ea20;ea15&ea20', spw='34:21~33')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea06&ea22', spw='33:13~21')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea10&ea23', spw='35:17~27')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea12&ea23', spw='47:13~20')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea12&ea23', spw='33:20~24')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea28', spw='47:13~14')

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	coloraxis='spw', correlation='RR, LL', yaxis='amp', xaxis='time', scan='12')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea06&ea12', spw='33:54')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='12', antenna='ea19&ea21', spw='33:22')

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	coloraxis='spw', correlation='RR, LL', yaxis='amp', xaxis='time', scan='12')



# Let's move on to scan='14'

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	coloraxis='baseline', correlation='RR, LL', yaxis='amp', xaxis='time', scan='14')

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', yaxis='amp', xaxis='freq', iteraxis='antenna',
	coloraxis='channel', averagedata=True, avgtime='60',
	correlation='RR, LL')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea06&ea22', spw='33:42~49')

# Okay, scan='14' looks pretty good now
# the points are very high 
# I am just going to investigate everything 

# There are some bad points 
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea06&ea12', spw='33:54')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea12&ea23', spw='47:7~16')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea15&ea17', spw='24:7~11')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea15&ea28', spw='33:20~58')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea15&ea28', spw='35:18~24')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea04&ea20', spw='34:22~29')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea06', spw='33:39~54')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea06&ea20', spw='34:21~25')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea10&ea23', spw='34:21~30')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='14', antenna='ea10&ea23', spw='35:7~27')

# Let's look at scan='14' now 
plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	coloraxis='baseline', correlation='RR, LL', yaxis='amp', xaxis='time', scan='14')

# It looks nice

# Let's move on to scan='16'

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	coloraxis='baseline', correlation='RR, LL', yaxis='amp', xaxis='time', 
	scan='16')

# I accidentally forgot to put in a in ea10
# flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
# 	scan='16', antenna='ea06&ea22; ea10&ea23', spw='33:41~53')

# flagmanager(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
# 		mode='restore', versionname='flagdata_131')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea22; ea10&ea23', spw='33:41~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea12&ea23', spw='47:14')

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', yaxis='amp', xaxis='freq', iteraxis='antenna',
	coloraxis='baseline', averagedata=True, avgtime='60',
	correlation='RR, LL')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea20&ea28', spw='33:19~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea28', spw='33:42~51')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea28', spw='47:14')

# I made a mistake in the antenna paramater so need to undo the flagging below
# flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
# 	scan='16', antenna='ea06&ea23;ea10&ea23;ea12&ea23;20&ea23', spw='33:41~53')

# flagmanager(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
# 		mode='restore', versionname='flagdata_138')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea23;ea10&ea23;ea12&ea23;ea20&ea23', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea10&ea23', spw='34:22~33')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea10&ea23', spw='35:19~28')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea10&ea23', spw='47:9~20')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea12&ea23', spw='47:13')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea23;ea10&ea23;ea12&ea23;ea20&ea23', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea22', spw='33:40')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea22&ea23', spw='47:14')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea19&ea21', spw='33:20~29')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea20', spw='33:44~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea15&ea17', spw='47:5~41')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea15&ea16', spw='47:2~51')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea15', spw='47:5~51')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea12', spw='33:41~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea12&ea23', spw='47:20')

# scan='16' is also done. Let's take a look at the scan without any averaging 
flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea06&ea12;ea06&ea20;ea06&ea28;ea20&ea22', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='16', antenna='ea03&ea23;ea12&ea22', spw='47:14')

# things should be fine now

# let's take a look at the scan='18'

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', yaxis='amp', xaxis='time',
	coloraxis='baseline',
	correlation='RR, LL')

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', yaxis='amp', xaxis='freq', iteraxis='antenna',
	coloraxis='baseline', averagedata=True, avgtime='60',
	correlation='RR, LL')
# I will start with this tomorrow

# Date: 8 August 2024

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea10&ea23; ea06&ea22', spw='33:43~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea06&ea28', spw='33:19~54')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea06&ea28', spw='47:14~21')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea23&ea28', spw='18:12~55')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea28', spw='47:14')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea06&ea25', spw='33:41~48')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea06&ea23; ea10&ea23; ea12&ea23', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea10&ea23', spw='34:23~32')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea10&ea23', spw='35:21~24')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea06&ea22', spw='33:40~53')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea06&ea20', spw='33:43~52')

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea06&ea12', spw='33:47~53')

# flagging for scan='18' is also complete. Let's take a complete look at the scan

flagdata(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	scan='18', antenna='ea12&ea23', spw='47:14')

# Let's take a look at the flux calibrator now

plotms(vis='SI1065.sb41775211.eb41785647.59696.39802591436.ms',
	field='0', scan='5', yaxis='amp', xaxis='time',
	correlation='RR, LL', coloraxis='baseline')