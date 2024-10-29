import os
import time
import draw_hp as draw_hp


text = """
                                        *+=---::::-:.#                  %#*#####*#%                        
                                      +... ...........#                *+%#%%%%%##**+---==*#%              
                                    %- ... ............*+%           #-*%%%%%%%%%%%%%%%%%%%%%*++++*##%     
                                    =.  .. ... ..........-=#        ==%%%%%%%%%%%%%%%%%%%%%%%%%@@@@%%*+++*%
                                    +....++=:.............-:+%    %:#%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%% 
                                     +.-#%#=+-:............-.:+ @+=%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%   
                ##*%                 %-=#%%#----............:..-**%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%    
            %=::-*@                   %#%%%+-----...::...........-*%%%%%%%%+=-------*#%%%%%@@@@@@@@@@@     
          *.:-#*%                    %#%%%%--------..::............-*%%%#-------------=%%%@@@@@@@@@@@      
        %-:-#*#%                   @%#%%%%% #+*%%%%#+::::....:.......:+#---------------+%%@@@@@@@@@@%      
        -:-#**%            %#*------------+%          %=::....:::......:=+--%%#-------%%%@@@@@@@@@@%       
       =:-#**%         %*=------------------++%          *:....:::.......:-+#%%%%*----%%@@@@@@@@@@%        
      %-:+**#       #=:----------------------=++%       %:=#....---.......:----=#=----#@@@@@@@@@@%         
      +:-#**%    %=::--------------------------+++%    @==%%%*...---......::-=%%%=---=+%@@@@@@@@%          
      -:+**#    +---------------------------+=--+++#   +=%%%%%%..:--:......:-:*%%*--=++%@@@@@@@%           
     %-:#**#  %=--------------------------+-=+---+++% +=#%%%%%%%-.:--:..:...--:#%#-=+%#%@@@@@@%            
     *:=***%  =------------------=-----------*+--=++**=*%%%%%%#%%+.:#=:..: .:--:%-=++%@@@@@@@%             
     -:***#  +-------------====--------------=++--++*=*%%-%%%=%%%%*:-==..:...:--=#+++@@@@@@@%              
     ..***% #--------------------=++==------------++*+%-=-%%+*%%%%%#:+=-..:...---#++%@@@@@@%               
    %.:-**%#----==++==--------=+---------+*-+#----++*+=*+%%#-%%%%%%%=-=%%#.... .:--#@@@@@@%                
    %:+::+%=---------------------#*++*..#+:+=----=++=*+*%%%-%%%%%%%--+%%%*.....:--%@@@@@@%                 
    *:*=:+#++++=--------------***....:-=+--------*-*++*+==-#%%%%%%%--+%%%*.....:--%@@@@@%                  
    +.**=%@+--##*---+=----+-=-..:*----------=+-=--*++*+#---=%%-------=%%%=......:-+@@@@%                   
    =:+*#% #*..::.---#+-=*--+=+*%%%#%%#==-----=---++*+%*---%%##%%#-------%:.....:-=@@@%                    
    --#=# %+*=----=*=+---=*=+#********----+=--*---+++%%#---#%%%%%%---%%%%@*.....::-@@%                     
    -=***  #-******#+=--==--*+****+=--------------=+*%%#--%%%%%%%%--#%%%@@%..:..::-@%                      
    -=**#  #-=-+*****----+=--=+=----------------=-#:***=--%%%%%%%#--%%%@@@@..:..::-@                       
    -=**#  %=-----=+-=---=-==---------=-----+---=+#*%%=---**%%%%%---%%%@@@@:.:..::-                        
    -=**#    #*---=+--#-+=----=+------=.*--*=--*.-#%%%%*----%%%%=---#%@@@@@*.:..::=                        
    -=**#    *=---=----==-----+-*=--==..--==---+.:-+%%%%%----##*----=#@@@@@%.-:.::#                        
    --#*#    #.:-*-+:#:=--===:++:*#*:..:#----=...-***#%%%%---------=++%@@@@%:--.:-%                        
    --#*#     *+----------------------*++--==-..-#***#%%%%%%=-----=%%@@@@@@#:+-.:=                         
    =:**#     =-------=*==+=--===-------+-+:...++#***#%%%%%%+-=#%%%@@@@@@@@=-%..:%                         
    *:**#@    :==-----=-..-+-------------+...:**##++++*%%%%%%%%%%@@@@@@@@@@-*=..=                          
    %:**#%   %-==+--=--....-=-+==--=*==+...-*****#+--=+%%%%%%%%%@@@@@@@@@@#:#:.:%                          
    %-***%    :....=.. ......-...=.......:-*=#**##=--=++       %@@@@@@@@@%#%#.:+                           
     +#%%%%%% #%. . . ................-:***#*=-==----=+*         %@@@@@@%@* ::+                            
  %########%%   =+. . ...........::--*#***#+--------+*++          %@@@@%   *:-%                            
   %%%*==+#+%   %#*=.....:.-.-:=-*##+==*#=::--------=+#%            @@%   #:-%                             
     +++--+#=#%  #**#=%:+:+.+##*****---+-::----------++             %%   *.-%                              
     *-=-=+#+++++*+*+*###**##+**-:-----*------------=+%                 *:-                                
     %+*=--=*+++#+--::-------+---------------------=+%                 *:=                                 
     *-=----------------------------------------==+#                  +:*                                  
     %:==-------------------------------==--=++#++@                  --%                                   
      *==*#%%%  %%%**#*++==-==+=======+#++==++++%                  %:+%                                    
     %#*##%%*-:::::=*%%---------------++--+++++%                  %.#                                      
     #::+**%:::::::=+%%+-++=-+---=*++=--*=-=+*#%                %++                                        
      -::##%#:::::=*%%%###++++++++++---+-+*%##%+%               %                                          
     #*::=###::-+%%%%%%%%%#%##%#**++**###%#+-:::-*%                                                        
    %:-=::#*#%#%%%%%%%%%%%%##%%%##%%%%%#::::::::::=#                                                       
  #-:::==-##%#*%%%%%%%%%%%#%%%%#%%%%%%%%%-:::::::::=+#                                                     
#:::::-+%%#%%%#%%%%%%%%%%%#%%%%#%%%%%%%%%*::::::::::=+#                                                    
*:::::=+%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%#::::::::=-+*%                                                    
  *:::=+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+:::::+-:::=*                                                     
   %+:-+*%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%-::==:::::::++%                                                   
    %%%#+*%%%%%%%%%%%%%@@%%%%%%%%#%%%%%%%*@+:::::::::+#+#                                                  
    %%%%%%%%%%%%%%%%%%@@@  %%%%%%%#%%%%%%%%-::::::+%@@@%                                                   
      %%%%%%%%%%%%%%@%@     %%%%%%%%%%%%%%%::::+%@@@@@@@%                                                  
       %##%%%%%%%@@@%%       %%%%%%%%%%%%%+:=%%%%%%@@@@@%                                                  
         #--+#%%%%%            %%%%%%%%%%%%%%%%%%%%@@@@@                                                   
          %*-----+*              %%%%%%%%%%%%%%%%%%@@%%                                                    
             %+---+%               %%%%%%%%%%%%%%%%%%%                                                     
               %---*@                  %%%%%%%%##%#*++%                                                    
                #--+**                        %=----++*                                                    
               %=-=*=%                          *---=+*                                                    
               #=+**#                            #---=+%                                                   
              **+**#                              #---=*                                                   
              ####*%                               #---=*                                                  
                                                    +---=*                                                 
                                                    +----=%                                                
                                                   %=*++==*%                                               
                                                   +++*==*+#                                               
                                                  %----=*+%                                                
                                                    #=% %*%


































"""
player = """                                                                                                                                                                                                     
                                                             =:::=                                  
                                             +++-:::::::::::::::.::::-                              
                                           +:::.::::::::::::::::::::::::::==                        
                                        =-::::::::::::::::::::::::::::::::::.:++==                  
                                      =:::::::::::::::::::::::::::::::::::::::::::==                
                                    =:::::::::::::::::::::::::::::::::::::::::::::::==              
                             -==++=-::::::::::::::::::::::::::::::::::::::::::::::::::=-            
                        ++====:::::::::::::::::::::::::::::::::::::::::::::::::::::::::==           
                   ++==-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-=-         
               =+==-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::==        
            -+=-:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-==      
          ++=:-----------:::::::::::::::::::::::::::::::::::-::::-:--::::::::::::::::::::::--+      
       =*+=---------------:::::::::::::::::::::::::::---------------:::::::::::::::::::::::--+      
        =+*==-==-----------::::::::::::---::::::::------------------------------:::::-:------+-     
           -=**========---::::::::::::-------:::------================---------------------=--*+    
               =+**+===---::::::::::::------------===========================================+%*    
                    =*+--:::::::::::::::--==---==============================================*@%+   
                      =+-:::::::::::::::--=---=============================================+%%%%*   
                      =+::::::::::::::::----============================================+#%%%%%%#   
                      =+--::::::::::::::---========================================++#%%%%%%%%%%+   
                      -+-:::::::::::::----===================================++*#@%%%%%%%%%%%%%%+   
                       ==:::::::::::::----===*******===============+******%%%%%%%%%%%%%%%%%%%%%#    
                       ==-:::::::::::----==*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*    
                        +=-:::::::::----=+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#     
                         ==-::::::----=+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+      
                          =+-:::---=+#%@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#       
                            =+++**#########%%%%%@@@@@%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%@%#*##%        
                                 +#%###########%%%%%%%%%%%%%%%%@@@@@@@@@@@%%%%%%%%%%#+++###+        
                                     +%%%%%####################################%%#*+==+##%+         
                                          ###################################%##*++==+####          
                                           ################################%%#*+++==+####=          
                                               +#%###%###########%%%%%%%%##**++++==+####=           
                                                     =#%%%%%%%%%%#%#####*+*+++++===+##*             
                                                       +%%%%%%%##**++++++++++======##*              
                                                       =+#%#*++++*#*++++++++========*               
                                                      +@%%%%*#*#**#*++++============                
                                                     =%####%%%%%%%%#+=========+++=-                 
                                             ++*******--==+++++*###++++++++==-                      
                                       =*****+*+*******++=--=+++++++**=:                            
                                    -+**+++++++++++++**###=--=++++++#%%%#-                          
                                   +*+++++++++++++++*##****=--=++**#%%%%##*-                        
                                 =**+++++++==+=+++*##*++****--==+*####%%%%%%+                       
                                ===++++++++++++*##*++++++**#=--=+****###%%%#%#                      
                               ==:=++=-=--=+**##*+++++++****=--=+***####%%%%%%#                     
                              ++:::----------=#*++++++++****=--==+*#####%%%%%%#                     
                             =*=:::::---------=+++++++++***+=--==+*######%%%%%#                     
                            =#++-::::::::::---=+++++++++****=--==+*###%%%%%%%%*                     
                            +*++=::::::::::----=++++++++***=---=+*###%%%%%%%%#                      
                            #+++=-:::::::::----=++++++++***=---=++++===+++##%%                      
                            %**+---::::::::---=+*+++++++**+---=+===--------=+*                      
                            ###+---::::::::::-+*+++++++***=--=+++=----------==                      
                            #+++=----:-::.::::=+++++++***+---=*#+=----------*=                      
                            **+++=-------:::::::-++******=-==*##+=----------*                       
                            +#+++++=------=-:::::::-=+++--=+*###+=----------+                       
                            +**++++++**+**++++-::::------=+*####+=----------*                       
                            #*=+++++++#*+++++++++------==*######+=----------*                       
                           *+==+*+++++**++++++++***=--+*#########+----------*                       
                           *=-==++**+++*#*+++***+=-==+*##########+=---------+                       
                           *-:-====+++**##***====+**##############+=--------=*                      
                           +-:--=====-+##********#################+=--------=*                      
                            *-======-=##**********#################=---------+                      
                            *-======+#%%##************#############+=--------=*                     
                            =-======+%%%%%%###*********#############=--------=*                     
                            ========+%%%%%%%%%%%#####*##############+=-------=*                     
                            ========#%%%%%%%%%%%%%%%%%%%%############=--------=                     
                            ====  ==#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=--------=                     
                                  =#%%%%%%%%%%%##%%%%%%%%%%%%%%%%%%%#*=--------+                    
                                  *#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###=--------+                    
                                  *#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###=---------+                   
                                  #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*##=---------+                   
                                  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*##=---------+                   
                                 *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*##=--------+*                   
                                 #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*##==------+*                    
                                 #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%#======+**                     
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###**                         
                                #*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*                          
                               ##*****%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*                          
                               ##***********######%%%%%%%%%%%%%%%%%%%%%%%#                          
                               ###**********#####%%%%%%%%%%%%%%%%%%%%%%%%#                          
                                ##********#***###**#%%%%%%%%%%%%%%%%%%%%%*                          
                                **++***********#*********####%%%%%#######*                          
                                +==+++++++++++************###############*                          
                                +========++++++####******################*                          
                                +=========++++*+=+#****#################%*                          
                               *===========++*++ +*+++++***********##***                            
                               *=========+++*+* +**+=++++++++++++++#                                
                              *+=========++*++  ++*+====+++++++++=**                                
                              *==========+*++ * +**===============*                                 
                              *==========+=*******+==============**                                 
                             *+=========+*#*+*##**+=============+*                                  
                            #%%#*++###%%#=:-=+=*%#+=============*                                   
                           +-=+*#**+++==----++***+=============*#                                   
                          #++===-============+*%#+============+*#                                   
                          #++===++==========**%%#+==========+=+##                                   
                          #*+++++****+++++###%%%*+==========+++#######                              
                              #*##%%%        ####%##%%%%%%%%##*##**=---*                            
                                             *---++++===+++=::::=++++*#*                            
                                            #+==-=========------++++=#**                            
                                            #++++++==========--+****#*+*                            
                                            #*+++***+==========****####                             
                                              #####****++=====*#####%                               
                                                      %%%%%%%                                       
                                                                                                    
"""


def clear_terminal():
    # Pour Windows, utilise la commande 'cls'
    # Pour Linux et macOS, utilise la commande 'clear'
    if os.name == 'nt':  # Si le système est Windows
        os.system('cls')



def ennemy_attack_animation():

  i = 1

  while i < 5 :
    # Nombre d'espaces pour décaler le dessin
    indent = " " * (50* (5-i))

    # Ajouter des espaces avant chaque ligne de l'orc
    orc_centered = "\n".join([line1 + indent + line2 for line1, line2 in zip(player.splitlines(), text.splitlines())])
    print(orc_centered)
    time.sleep(0.1)
    clear_terminal()
    i += 1
  i = 1
  while i < 5 :
    # Nombre d'espaces pour décaler le dessin
    indent = " " * (50*i)

    # Ajouter des espaces avant chaque ligne de l'orc
    orc_centered = "\n".join([line1 + indent + line2 for line1, line2 in zip(player.splitlines(), text.splitlines())])
    print(orc_centered)
    time.sleep(0.1)
    clear_terminal()
    i += 1
      
  indent = " " * 250

  # Ajouter des espaces avant chaque ligne de l'orc
  orc_centered = "\n".join([line1 + indent + line2 for line1, line2 in zip(player.splitlines(), text.splitlines())])
  print(orc_centered)

  draw_hp.draw_hp_ennemy(40, "red", 100, 100)
  player_attack_animation()


def player_attack_animation():

  i = 1

  clear_terminal()
  while i < 5 :
    # Nombre d'espaces pour décaler le dessin

    indent = " " * (50*i)
    indent2 = " " * (250 - (50*i))



    # Ajouter des espaces avant chaque ligne de l'orc
    orc_centered = "\n".join([indent + line1  + indent2 + line2 for line1, line2 in zip(player.splitlines(), text.splitlines())])
    print(orc_centered)
    time.sleep(0.1)
    clear_terminal()
    i += 1

  while i < 5 :
    # Nombre d'espaces pour décaler le dessin
    indent = " " * (50* (5-i))
    indent2 = " " * (250 - (50* (5-i)))


    # Ajouter des espaces avant chaque ligne de l'orc
    orc_centered = "\n".join([ indent + line1  + line2 for line1, line2 in zip(player.splitlines(), text.splitlines())])
    print(orc_centered)
    time.sleep(0.1)
    clear_terminal()
    i += 1
  i = 1
 
      
  indent = " " * 250

  # Ajouter des espaces avant chaque ligne de l'orc
  orc_centered = "\n".join([line1 + indent + line2 for line1, line2 in zip(player.splitlines(), text.splitlines())])
  print(orc_centered)

  draw_hp.draw_hp_ennemy(40, "red", 100, 100)







ennemy_attack_animation()