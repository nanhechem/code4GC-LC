def column():
        a = float(input('What is the retention time? '))
        b = float(input('Peak width at half maximum? '))
        c = float(input('Column length? '))
                
        eff = int((5.54*(a/b)**2)/c)
        if a/c < 0.4:
                print ("Retention time is too short. The column might be leaked")
        else:
                if eff > 2000:
                        print ("Good Job, this is a good column")
                        print (eff)
                        
                elif eff <2000 and eff > 1000:
                        print ("So close. Try harder!")
                        print (eff)
                else:
                        print ("Please keep woring! never give up")
                        print (eff)

			
	
column()

#Thanks to Marcelino!
