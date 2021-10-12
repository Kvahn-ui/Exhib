# ©Kvahn version 1.19
pate = 1.19
d = input("type how many [full] days left 'till exam due ")
h = int(d)*24
sl = int(d)*9
usl = int(h) - int(sl)
proc = 1.59*int(d)
poo = int(d)*6
proh = int(usl) - int(proc) - int(poo)
to = proh/2
tot = to/24
print("incuding procrastination and sleep the best case scenario is:")
print(tot)
print("days")
print(" ")
t = input("type c for details or type b for misc info ")
if t == "c":
    print("days:")
    print(d)
    print("hours:")
    print(h)
    print("time spend sleeping (best case scenario) :")
    print(sl)
    print("time spent awake (hours):")
    print(usl)
    print("time spent procrastinating(best case scenario)")
    print(proc)
    print("time spent eating(bestCaseScenario)")
    print(poo)
    print('time spent not procrastinating/asleep/eating in hours')
    print(proh)
    print('adjusted for activities/sleepins')
    print(to)
    print("time spent not procrastinating/asleep in day form")
    print(tot)
    print(" ")
    t = input("type c for details or type b for misc info ")

if t == "b":
    print("version:")
    print(pate)
    print("copyright:")
    print("©Kvahn 2021")
    print(" ")
t = input("type c for details, type b for misc info ")

if t =="r":
    print(" ")
    d = input("type how many [full] days left 'till exhibition research due ")

if t =="sas":
    while True:
        print("sas")

    

    
    
    

