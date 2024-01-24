# Aleksejs Kaļinkins 10B
# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

x = 1 #Player one
y = 1 #Player two
rounds = 25 
throw = "1"
throw_2 = "2"
print("Welcome to the board game circus!")
print("Let's start to play.")


while rounds>0: #kamēr raundi nepabeidzas kods tiek aktivēts
 choise = input("Please role the dice") 
 if choise == throw : #ja met x spēlētjas tad izpildas nākama komanda
    import random
    throw_dice = random.randint(1, 6)
    print("Number on the dice is:" + str(throw_dice))
    x += throw_dice
    print("Your position is: " + str(x))
    print("Rounds left: " + str(rounds))
 elif choise == throw_2:#ja met y tad izpildas nākama komanda
    import random
    throw_2_dice = random.randint(1, 6) #randomu skaitļu ģeņerātors
    print("Number on the dice is:" + str(throw_2_dice))
    y += throw_2_dice
    print("Your position is: " + str(y))#rāda spēlētāja poziciju
    rounds-=1#atņem jau izpildītus raundus
    print("Rounds left: " + str(rounds))#rāda cik palika raundu
 #Visas nakamas rindas rada kāpņu funkciju, šeit ir 4 kāpnes kuri pazeminā spēlētāja poziciju un 4 kāpnes, kuras palielinā to
 if x==18:   #Šeit pozicija pazeminās atņemot no mainīgas noteiktus skaitļus
    x-=11
    print("You've been dropped to the: " + str(x))
 elif y==18:
    y-=11
    print("You've been dropped to the: " + str(y))
 if x==67:
    x-=21
    print("You've been dropped to the: " + str(x))
 elif y==67:
    y-=21
    print("You've been dropped to the: " + str(y))
 if x==80:
    x-=11
    print("You've been dropped to the: " + str(x))
 elif y==80:
    y-=11
    print("You've been dropped to the: " + str(y))
 if x==74:
    x-=11
    print("You've been dropped to the: " + str(x))
 elif y==74:
    y-=11
    print("You've been dropped to the: " + str(y))
 if x==15: #Šeit pozicija palielinās pieskaitot mainīgām noteiktus skaitļus
    x+=9
    print("You've been raised to the: " + str(x))
 elif y==15:
    y+=9
    print("You've been raised to the: " + str(y))
 if x==39:
    x+=9
    print("You've been raised to the: " + str(x))
 elif y==39:
    y+=9
    print("You've been raised to the: " + str(y))
 if x==33:
    x+=19
    print("You've been raised to the: " + str(x))
 elif y==33:
    y+=19
    print("You've been raised to the: " + str(y))
 if x==87:
    x+=9
    print("You've been raised to the: " + str(x))
 elif y==87:
    y+=9
    print("You've been raised to the: " + str(y))
 
if rounds == 0: #Ja raundi pabeizdas tad neviens neuzvarēja
   print("No winner")
elif x == 100: #Uzvarēja x spēlētajs, jo viņš sasniedza 100 laukumu
   print("Player one won!")
elif y == 100:# Uzvarēja y spēlētajs, jo viņš sasniedza 100 laukumu
   print("Player two won!")












