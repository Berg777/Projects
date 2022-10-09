#Labels
# 0 = Glicemia Normal
# 1 = Tolerância a glicose diminuida
# 2 = Diabetes Mellitus
#Features
# Primeiro - Jejum 
# Segundo - Pós-Sobrecarga 
# Terceiro - Glicemia Casual

from sklearn import tree
from random import randint
from pyfiglet import Figlet
import fade
from tqdm import tqdm
import time

#Glicemia Normal
#Tolerância a glicose Diminuida
#Diabetes

fonte = Figlet(font='standard')

text = (fade.fire(fonte.renderText('Doutor diabetes')))
print(text)
time.sleep(1)
print('\33[31;1mIsso é apenas um pré diagnostico\33[m')
time.sleep(1)

jejum = float(input("\33[1mQuantos mg/dL em Jejum: "))
sobrecarga = float(input("Quantos mg/dL após Sobrecarga: "))
diadia = float(input("Quantos mg/dL em qualquer hora do dia: "))

for x in range(0,1000):
    
    jejum1 = randint(50,95)
    sobrecarga1= randint(90,135)
    diatodo1 = randint(100,195)
    jejum2 = randint(100,120)
    sobrecarga2 = randint(140,200)
    diatodo2 = randint(100,195)
    jejum3 = randint(135,200)
    sobrecarga3 = randint(210,300)
    diatodo3 = randint(210,300)
    features = [[jejum1, sobrecarga1, diatodo1],[jejum2, sobrecarga2, diatodo2], [jejum3, sobrecarga3, diatodo3]]
    labels = [0, 1, 2] 
    classif = tree.DecisionTreeClassifier()
    classif.fit(features, labels)
    x = classif.predict([[jejum, sobrecarga, diadia]])

print('Carregando resultado...')

for i in tqdm(range(50), colour = "blue"):
    
    time.sleep(0.05)

if x == 0:
    
    print("\33[32;1mVocê tem Glicemia Normal\33[m")

elif x == 1:
    
    print("\33[33;1mVocê tem tolerância a glicose diminuida\33[m")

else:
    
    print("\33[31;1mVocê tem Diabetes Mellitus\33[m")
    print("\33[1mConsulte um médico especializado para mais informações\33[m")
    
    
