from Linux import debian
import random

try:
    from Win import windows
except:
    pass

styleOne = """
 .d88888b.  .d8888b.  .d8888b.        d88888888888b.  .d88888b.  
d88P" "Y88bd88P  Y88bd88P  Y88b      d88888888   Y88bd88P" "Y88b 
888     888Y88b.     888    888     d88P888888    888888     888 
888     888 "Y888b.  888           d88P 888888   d88P888     888 
888     888    "Y88b.888          d88P  8888888888P" 888     888 
888     888      "888888    888  d88P   888888 T88b  888 Y8b 888 
Y88b. .d88PY88b  d88PY88b  d88P d8888888888888  T88b Y88b.Y8b88P 
 "Y88888P"  "Y8888P"  "Y8888P" d88P     888888   T88b "Y888888"  
                                                            Y8b  
"""

styleTwo = """
      * ***          *******          * ***            **             ***** ***        * ***    
    *  ****        *       ***      *  ****  *      *****          ******  * **      *  ****    
   *  *  ***      *         **     *  *  ****      *  ***         **   *  *  **     *  *  ***   
  *  **   ***     **        *     *  **   **          ***        *    *  *   **    *  **   ***  
 *  ***    ***     ***           *  ***              *  **           *  *    *    *  ***    *** 
**   **     **    ** ***        **   **              *  **          ** **   *    **   **     ** 
**   **     **     *** ***      **   **             *    **         ** **  *     **   **     ** 
**   **     **       *** ***    **   **             *    **         ** ****      **   **     ** 
**   **     **         *** ***  **   **            *      **        ** **  ***   **   **     ** 
**   **     **           ** *** **   **            *********        ** **    **  **   **     ** 
 **  **     **            ** **  **  **           *        **       *  **    **   **  ** *** ** 
  ** *      *              * *    ** *      *     *        **          *     **    ** *   ****  
   ***     *     ***        *      ***     *     *****      **     ****      ***    ***     *** 
    *******     *  *********        *******     *   ****    ** *  *  ****    **      ******* ** 
      ***      *     *****            ***      *     **      **  *    **     *         ***   ** 
               *                               *                 *                           ** 
                **                              **                **                         *  
                                                                                            *   
                                                                                           *    
"""

styleThree = r"""
(  ___  )(  ____ \(  ____ \(  ___  )(  ____ )(  ___  )
| (   ) || (    \/| (    \/| (   ) || (    )|| (   ) |
| |   | || (_____ | |      | (___) || (____)|| |   | |
| |   | |(_____  )| |      |  ___  ||     __)| |   | |
| |   | |      ) || |      | (   ) || (\ (   | | /\| |
| (___) |/\____) || (____/\| )   ( || ) \ \__| (_\ \ |
(_______)\_______)(_______/|/     \||/   \__/(____\/_)
"""

a = random.randint(0, 2)
if a == 0:
    print(styleOne)
elif a == 1:
    print(styleTwo)
else:
    print(styleThree)

opt = 1
# emailID = input("Enter Email ID: ")
emailID = "kaustubhkishorem@gmail.com"
# opt = input("Select Operating System:\n1.Debian\n2.Windows\n")
if opt == 1:
    obj = debian.Debian()
    obj.emailID = emailID
    obj.runner()
    print("Score: " + str(obj.score_getter()))
    print("Non Compliant Score loss: " + str(obj.ncScore_getter()))
elif opt == 2:
    obj = windows.Windows()
    obj.userEmailID = emailID
