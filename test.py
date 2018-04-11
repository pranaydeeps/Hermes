from Hermes import Hermes

hermes = Hermes('pranaydeeps@gmail.com','pranaydeeps@gmail.com','testmodel')
list_1 = []
for i in range(0,100):
    list_1.append(i)
    hermes.track(list_1,'i')
    if i%10==0:
        hermes.mail()
