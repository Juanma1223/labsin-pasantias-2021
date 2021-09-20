# Métricas del modelo entrenado por mi

Sensitivity: 0.8997100289971003

Specificity: 0.9514048595140486

# Tabla comparativa

| | Implementación propia (Histograma de caracteres) | Algoritmo en server | Implementación propia (Vocales, consonantes y entropía)
| ---- | ---- | ---- |
| Sensitivity | 0.8997100289971003 | 0.9744025597440256 | 0.3133686631336866 |
| Specificity | 0.9514048595140486 | 0.991091140311804 | 0.8743125687431257 |

# Conclusiones de los gráficos de caja
    ![image](https://github.com/Juanma1223/labsin-pasantias-2021/blob/master/4_implementacion/Graficos/dga_probability_boxplot.png)
    ![image](https://github.com/Juanma1223/labsin-pasantias-2021/blob/master/4_implementacion/Graficos/normals_probability_boxplot.png)
    
    En los gráficos se observan probabilidades bastante altas de que las predicciones son correctas, lo único que creo que se podría destacar
    es el hecho de que encontramos unos cuantos datos anómalos en el gráfico de las probabilidades de acertar en dominios normales.

# Conclusión

    Luego de observar los resultados encontramos una mas que clara diferencia entre los planteos en las entradas al algoritmo de regresión
    logística, donde en la implementación con el conteo de caracteres tuvo una efectividad (sensitivity) de casi el 90% a la hora de detectar
    DGA, mientras que la implementación que hace uso de la cantidad de vocales, consonantes y la entropía, llega a un pobre 31% de efectividad.

    Además, encontramos una diferencia entre la versión que se encuentra almacenada en el servidor con la implementación, entiendo que esto
    se debe al tamaño de la entrada qu recibió cada uno, ya que para entrenar el algoritmo de implementación propia con histograma de caracteres solo utilicé una muestra de 50000 dominios (Mitad DGA y mitad normales), dando como resultado un modelo menos entrenado
    y por tanto menos preciso.

    Con respecto a la implementación alternativa, luego de observar la entrada con la que se entrenó al algoritmo, se puede ver como realmente
    las métricas no diferencian claramente entre dominios DGA y normales, ya que el grado de entropía de los dominios DGA resultó casi idéntico a aquel de los normales, también, como hipótesis planteé que si un dominio tenía un desbalance entre vocales y consonantes,
    era posiblemente un conjunto de letras sin sentido, ya que normalemente, las palabras están compuestas por números similares de consonantes y vocales. Aún así, esto demostró no ser eficaz como modelo de aprendizaje para el algoritmo de regresión logística
