import string

mdp = input('rentrer votre mot de passe ')

mdp_trop_court = "votre mot de passe est trop court"

print (len(mdp))
print(mdp.isdigit())

if len(mdp) == 0:
     print(mdp_trop_court.upper())
     exit()
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
    exit()
elif mdp.isdigit() :
    print('votre mot de passe ne contient que des nombres')
    exit()

print("inscription terminée")