import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

##PARAMETROS
K=100
R=0.85
t_times=[10**t for t in range(1,7)]
centerX, centerY = 0.0, 0.0
seed  = 42

##
print(t_times)
data_simulation={
      "x":[],
      "y":[],
      "distance":[]
  }

def runSimluation_caso_01(radius,points):
  theta = 2 * np.pi * np.random.rand(points)
  rho = radius * np.sqrt(np.random.rand(points))
  x = rho * np.cos(theta)
  y = rho * np.sin(theta)
  # Calcular la distancia del centro al punto
  distances = np.sqrt(x**2 + y**2)
  # Calcular la media y desviación estandar de la distancia
  data_simulation["x"].extend(x)
  data_simulation["y"].extend(y)
  data_simulation["distance"].extend(distances)
       
def runSimluation_caso_02(radius,points):
  theta = 2 * np.pi * np.random.rand(points)
  rho = radius * np.random.rand(points)
  x = rho * np.cos(theta)
  y = rho * np.sin(theta)

  # Calcular la distancia del centro al punto
  distances = np.sqrt(x**2 + y**2)
  # Calcular la media y desviación estandar de la distancia
  data_simulation["x"].extend(x)
  data_simulation["y"].extend(y)
  data_simulation["distance"].extend(distances) 

if __name__=="__main__":

  for time in t_times:
    for iteration in range(time):
      runner_simulation=runSimluation_caso_02(radius=R, points=K)

    df=pd.DataFrame(data_simulation)
    df.to_csv(f"ejemplo_simulation_caso02_{time}.csv", index=False)
    data_simulation={
      "x":[],
      "y":[],
      "distance":[]
    }