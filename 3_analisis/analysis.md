# Sensitividad y especificidad
## Valores obtenidos:

Sensitivity: 0.9744025597440256

Specificity: 0.991091140311804

## Observaciones

  Luego de observar los resultados obtenidos, se puede concluir que el algoritmo de detección tiene un alto grado de acierto, teniendo valores bastante cercanos al máximo: 1.
  Esto quiere decir que el algoritmo se encuentra bien entrenado y resulta fiable a la hora de detectar url DGA de aquellas que son normales, pudiendo ser utilizado como filtro
  prefectamente. Los valores se pueden observar en el archivo "argencon_sample_domains_predictions.csv"
  
## Histogramas:
 
 ![image](https://github.com/Juanma1223/labsin-pasantias-2021/blob/master/3_analisis/dga_domains_histogram.png)
 
 ![image](https://github.com/Juanma1223/labsin-pasantias-2021/blob/master/3_analisis/normal_domains_histogram.png)
  
# Análisis de los histogramas

  Con respecto a los histogramas de longitud de los URLs, podemos observar una serie de patrones, siendo el primero la concenctración que tenemos hacia el centro
  en el gráfico de los detectados como DGA, dándonos a entender que hay una gran mayoría que tiene longitudes parecidas, es decir, que es muy posible que estén generados
  de manera algorítmica siguiendo algún tipo de procedimiento repetitivo, es por eso que no encontramos grán variación
  
  Por otro lado, en el histograma de URLs detectados como normales nos encontramos una mayor diversidad en el conteo de caracteres, dándonos a entender que dificilmente se podría
  generar una distribución tan poco uniforme, en contraste con con el histograma de DGA que se asemeja incluso a una distribución normal (salvando las distancias).
  
  También, si unimos este histograma con los histogramas de la actividad 2, encontraremos que los URLs DGA resultan una combinación de caracteres sin ningún tipo de sentido,
  con longitudes similares, mientras que los normales resultan siempre nombres coherentes, esto tiene que ver con que los URLs normales tienen el fin de ser mas sencillos de
  recordar, cuando claramente los DGA son todo lo contrario. 
  
  Gracias a estos 2 histogramas podemos comenzar por entender que los DGA suelen tener una cantidad similar de caracteres
  y suelen ser una combinación sin ningún sentido aparente
  
