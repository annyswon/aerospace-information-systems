# Информационные системы аэрокосмических комплексов
### Лабораторные работы
MAI/ 5 semester<br>
Выполнили студенты группы ***М3О-312Б-18***<br>

Быков Н.М.<br>
Суркова А.А.<br>

Города: <br>
Быков Н.М. - **Майами, США** -> branch: **lab1**<br>
Суркова А.А. - **Марсель, Франция** -> branch: **lab2**<br>

## Лабораторная работа 1
[Задание на работу](https://gist.github.com/ilyashatalov/08f28665645a8e8709f1ed51fdc00791)

##### Ход работы
1) Скачиваем снимок
2) Находим файл *_MTL.txt
3) Парсим значения координат углов
4) "Ориентируемся" на снимке с помощью подсчета дельты по горизонтали и вертикали 
5) Определем на снимке свой город. 
Координаты города были взяты из Википедии.


## Лабораторная работа 2
[Задание на работу](https://gist.github.com/ilyashatalov/5c6d8d24222c8fb07a7921dda109c8ea)

##### Цель работы 
1. Считать NDVI для вырезанного города;
2. "Разукрасить" город в соответствии со шкалой NVDI. 

##### Ход работы 
**NDVI (Normalized Difference Vegetation Index)**, или вегетационный индекс – это показатель фотосинтетической активности растительной биомассы.

При расчёте NDVI учитывается красный (RED) и инфракрасный (NIR) свет, отражаемый растениями. Индекс вычисляется по следующей формуле:

**NDVI = (NIR - RED) / (NIR + RED)**

Полученный показатель варьируется в значениях от -1 до 1. Чем выше положительное значение NDVI, тем активнее происходит фотосинтез растений и, следовательно, зеленая фитомасса на карте с визуализацией индекса вегетации будет отображаться контрастнее.

Расчет был выполнен с помощью библиотеки rasterio на языке Python3. 
