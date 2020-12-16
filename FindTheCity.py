import cv2

#Задаем координаты углов снимка
kor1 = 1793, 41
kor2 = 7993, 1497
kor3 = 6329, 7348
kor4 = 97, 5908

def coord(word): #находим значения углов
    inp = open('LE07_L1TP_195030_20000321_20170212_01_T1_MTL.txt').readlines()
    for i in iter(inp):
        if word in i:
            original = i[4:] #срез на 4 пикселя
            return float(original.replace(word + " = ", ""))

#Задаем координаты города, в нашем случае г. Марсель, Франция
t_coord = 43.44178, 5.222137

#Значения широты/latitude и долготы/longitude углов снимка из MTL файла
CORNER_UL_LAT_PRODUCT = coord('CORNER_UL_LAT_PRODUCT')
CORNER_UL_LON_PRODUCT = coord('CORNER_UL_LON_PRODUCT')
CORNER_UR_LAT_PRODUCT = coord('CORNER_UR_LAT_PRODUCT')
CORNER_UR_LON_PRODUCT = coord('CORNER_UR_LON_PRODUCT')
CORNER_LL_LAT_PRODUCT = coord('CORNER_LL_LAT_PRODUCT')
CORNER_LL_LON_PRODUCT = coord('CORNER_LL_LON_PRODUCT')
CORNER_LR_LAT_PRODUCT = coord('CORNER_LR_LAT_PRODUCT')
CORNER_LR_LON_PRODUCT = coord('CORNER_LR_LON_PRODUCT')

#Расчитаем разницу
delt_lat = ((CORNER_UL_LAT_PRODUCT + CORNER_UR_LAT_PRODUCT) / 2 - (CORNER_LL_LAT_PRODUCT + CORNER_LR_LAT_PRODUCT) / 2)
delt_lon = abs((CORNER_UL_LON_PRODUCT + CORNER_LL_LON_PRODUCT) / 2 - (CORNER_UR_LON_PRODUCT + CORNER_LR_LON_PRODUCT) / 2)


x = abs(abs((CORNER_UL_LON_PRODUCT + CORNER_LL_LON_PRODUCT) / 2) - abs(t_coord[1])) / delt_lon
y = (t_coord[0] - (CORNER_LL_LAT_PRODUCT + CORNER_LR_LAT_PRODUCT) / 2) / delt_lat
print('P: ', x, y)


def line_to_center(point1, point2, kof):
    l = kof / (1 - kof)
    if kof <= 0.5:
        xm = (point1[0] + l * point2[0]) / (1 + l)
        ym = (point1[1] + l * point2[1]) / (1 + l)
        M = xm, ym
        return M
    else:
        l = 1 / l
        xm = (point2[0] + l * point1[0]) / (1 + l)
        ym = (point2[1] + l * point1[1]) / (1 + l)
        M = xm, ym
        return M



line1 = line_to_center(kor1, kor2, x)
line2 = line_to_center(kor4, kor1, y)

def show_result(result): #Выводим изображение
    screen_res = 1280, 720
    scale_width = screen_res[0] / result.shape[1]
    scale_height = screen_res[1] / result.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(result.shape[1] * scale)
    window_height = int(result.shape[0] * scale)

    cv2.namedWindow('Marcel', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Marcel', window_width, window_height)

    cv2.imshow('Marcel', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


Epsln = -1120, 750 #Погрешность расчетов
if __name__ == '__main__':
    img = cv2.imread("LE07_L1TP_195030_20000321_20170212_01_T1_B2.tif")
    img = cv2.circle(img, (int(line1[0]+Epsln[0]), int(line2[1] + Epsln[1])), 400, (255, 52, 179), thickness=30)
    show_result(img)
