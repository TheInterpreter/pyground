"""
    _____                 __                                                                                    
  / ____|               /_ |  _                                                                                
 | |     __ _ ___  ___   | | (_)                                                                               
 | |    / _` / __|/ _ \  | |                                                                                   
 | |___| (_| \__ \  __/  | |  _                                                                                
 _\_____\__,_|___/\___|_ |_| (_)      _____            _   _                         ____                 _    
 \ \        / / |   (_) |            / ____|          | | (_)                       |  _ \               | |   
  \ \  /\  / /| |__  _| | ___ ______| |     ___  _ __ | |_ _ _ __  _   _  ___ ______| |_) |_ __ ___  __ _| | __
   \ \/  \/ / | '_ \| | |/ _ \______| |    / _ \| '_ \| __| | '_ \| | | |/ _ \______|  _ <| '__/ _ \/ _` | |/ /
    \  /\  /  | | | | | |  __/      | |___| (_) | | | | |_| | | | | |_| |  __/      | |_) | | |  __/ (_| |   < 
     \/  \/   |_| |_|_|_|\___|       \_____\___/|_| |_|\__|_|_| |_|\__,_|\___|      |____/|_|  \___|\__,_|_|\_\
                                                                                                               
                                                                                                               """

demogorgon = 50
powers = 18
fireworks = 4
pipe = 1
bullet = 2
doubleshot=bullet*2

print("The demogorgon got into the scene! it is attacking El, Hal and the Kids")
while demogorgon >0:
    demogorgon= demogorgon-pipe
    print ("Billy is attacking The Demogorgon with a pipe, inflicting "+str(pipe)+" points of damage!")
    if demogorgon == 40:
        demogorgon = demogorgon-doubleshot
        print (("Hal shot the Demogorgon twice with his revolver, inflicting ")+str(doubleshot)+(" points of damage!"))
        continue
    elif demogorgon == 30:
        demogorgon = demogorgon-powers
        print (("El came to scene by graving the Demogorgon with her mighty superpowers! OMG the Demogorgon lost ")+str(powers)+(" points of damage!"))
        continue    
    elif demogorgon == 10:
        demogorgon = demogorgon-fireworks
        print(("The Demogorgon is about to die, AND THE KIDS STROKE WITH FIREWORKS! they inflicted ")+str(fireworks)+(" points of damage"))
        continue
    if demogorgon <= 5:
        print ("Billy gave the final strike with that pipe...")
        print ("The demogorgon perishes in terrible pain!!!")
        break
print ("it's over... BUT IS IT??")
