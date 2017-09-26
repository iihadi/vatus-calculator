#Abdul Hadi - 20/09/17

a = int(input("What is the value of a?\n"))
v = int(input("What is the value of v?\n"))
u = int(input("What is the value of u?\n"))
t = int(input("What is the value of t?\n"))

equations_for_s = { 1 : ((v ** 2) - (u ** 2) / (2 * a)) #if you have v,u,a
                    2 : ((u*t)+(0.5*(a*t)**2)) #If you have u,a,t
                    3:  ((0.5 * (u + v)) * t)  # If you have u,v,t
                    4 : ((v*t)-(0.5*((a*t)**2)) #If you have v,a,t
                    }


print(equations_for_s[1])

