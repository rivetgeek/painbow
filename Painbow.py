import os
import stopwatch
import datetime
import CardTools
import Config

chains_total=Config.chains_total
chain_length=Config.chain_length
prefix = Config.prefix   
t = stopwatch.Timer()


for x in range(chains_total):
        #set the output table
    if x < chains_total / 4:
        table = open(str(prefix)+'-1-'+str(chain_length)+'-'+str(chains_total)+'.txt','a')
        table_num=1
    if x == chains_total / 4:
        table = open(str(prefix)+'-2-'+str(chain_length)+'-'+str(chains_total)+'.txt','a')
        table_num=2
    if x == chains_total / 2:
        table = open(str(prefix)+'-3-'+str(chain_length)+'-'+str(chains_total)+'.txt','a')
        table_num=3
    if x == chains_total / 2 + chains_total / 4:
        table = open(str(prefix)+'-4-'+str(chain_length)+'-'+str(chains_total)+'.txt','a')
        table_num=4        
    
    chain_start,chain_end=CardTools.create_chain()
 

    table.write(chain_start + ' ' + chain_end+'\n')






#below here is just pretty stuff
    def cls():
        os.system(['clear','cls'][os.name == 'nt'])        
    

    if x > 0:
        percent_done = float(x) / float(chains_total) *100
        cls()
        

            #how many chains per second
        chains_per_second = x / t.elapsed
        seconds_total = chains_total / chains_per_second
        time_left=datetime.timedelta(seconds=seconds_total)
        
        print ("\r"+str("%.2f" % percent_done)+"% done")
        print "Working on chain number " + str(x) + " out of "+str(chains_total) 
        print "Writing to table"+str(table_num)+" ("+ str(chains_total / 4)+" chains per table)"
        print "Elapsed time:"+ str(t)
        print "Time remaining: "+ str(time_left)
t.stop
cls ()
print "Elapsed time:"+  str(t)        
    

        