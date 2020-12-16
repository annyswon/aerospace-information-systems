#используем необходимые библиотеки

import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import seaborn as sns
import os

os.listdir('../ИСАК/') #даем программе доступ к определенной папке для упрощения ввода
np.seterr(over="ignore")
np.seterr(invalid="ignore")

if __name__ == '__main__':
    img1 = rasterio.open('../ИСАК/LE07_L1TP_195030_20000321_20170212_01_T1_B3.tif')
    img2= rasterio.open('../ИСАК/LE07_L1TP_195030_20000321_20170212_01_T1_B4.tif')

    #переводим целочисленные данные в данные с плавающей точкой для точности подсчета
    red=img1.read(1).astype('float64')
    nir=img2.read(1).astype('float64')
    #print(type(red), type(nir))

    ndvi=np.where(nir+red==0., 0, (nir-red)/(nir+red)) #расчет индекса ndvi
    #print(ndvi[2000:2010, 2000:2010])

    fig = plt.figure(figsize=(8, 6)) #задаем размер изображения

    #задаем палитру цветов для геоснимка
    tk = sns.heatmap(ndvi, cmap="gist_earth", vmin=-1, vmax=1, xticklabels=False, yticklabels=False)

    #выводим окно с тепловой картой окна
    tk.set_title('heatmap')
    tk.set_axis_off()
    plt.tight_layout()
    plt.show()