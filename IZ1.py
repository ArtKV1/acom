import cv2
import time

# # использование встроенного метода KCF
#
# video_path = 'C:/Users/Ростислав/Downloads/Cereal.mp4'
# cap = cv2.VideoCapture(video_path)
# start_time = time.time()
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output_video = cv2.VideoWriter('D:/4_курс/АЦОМ/IZ/input_video/output2.mp4', fourcc, fps, (width, height))
#
# # Чтение первого кадра
# ret, frame = cap.read()
# if not ret:
#     print("Не удалось прочитать первый кадр")
#     exit()
#
# bbox = cv2.selectROI("Frame", frame, False)
# cv2.destroyWindow("Frame")
#
# tracker = cv2.TrackerKCF_create()
# tracker.init(frame, bbox)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     _, bbox = tracker.update(frame)
#
#     (x, y, w, h) = [int(v) for v in bbox]
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
#
#     cv2.imshow("video", frame)
#     output_video.write(frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# end_time = time.time()
# time = end_time - start_time
# print(f"Время выполнения: {time} секунд")
# cap.release()
# cv2.destroyAllWindows()



# использование встроенного метода CSRT


# video_path = 'C:/Users/Ростислав/Downloads/Cereal.mp4'
# cap = cv2.VideoCapture(video_path)
#
# start_time = time.time()
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output_video = cv2.VideoWriter('D:/4_курс/АЦОМ/IZ/input_video/output2.mp4', fourcc, fps, (width, height))
#
# ret, frame = cap.read()
# if not ret:
#     print("Не удалось прочитать первый кадр")
#     exit()
#
# bbox = cv2.selectROI("Frame", frame, False)
# cv2.destroyWindow("Frame")
#
# tracker = cv2.TrackerCSRT_create()
# tracker.init(frame, bbox)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     _, bbox = tracker.update(frame)
#
#     (x, y, w, h) = [int(v) for v in bbox]
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
#
#     cv2.imshow("video", frame)
#     output_video.write(frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# end_time = time.time()
# time = end_time - start_time
# print(f"Время выполнения: {time} секунд")
#
# cap.release()
# cv2.destroyAllWindows()
#
# использование встроенного метода MOSSE
#
# video_path = 'C:/Users/Ростислав/Downloads/Cereal.mp4'
# cap = cv2.VideoCapture(video_path)
#
# start_time = time.time()
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output_video = cv2.VideoWriter('C:\\Users\\Ростислав\\Downloads\\result\\result\\dialog.mp4', fourcc, fps, (width, height))
#
# ret, frame = cap.read()
# if not ret:
#     print("Не удалось прочитать первый кадр")
#     exit()
#
# bbox = cv2.selectROI("Frame", frame, False)
# cv2.destroyWindow("Frame")
#
# tracker = cv2.legacy.TrackerMOSSE_create()
# tracker.init(frame, bbox)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     _, bbox = tracker.update(frame)
#
#     (x, y, w, h) = [int(v) for v in bbox]
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
#
#     cv2.imshow("video", frame)
#     output_video.write(frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# end_time = time.time()
# time = end_time - start_time
# print(f"Время выполнения: {time} секунд")
# cap.release()
# cv2.destroyAllWindows()
#

import cv2
import numpy as np

#from search_borders import borders

# Открываем видеофайл для чтения
input_video = cv2.VideoCapture(r'C:\\Users\\Ростислав\\Downloads\\result\\result\\dialog.mp4')
start_time = time.time()

# Чтение характеристик видео (размеры кадра, FPS и т.д.)
width = 1000  # int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = 600  # int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = input_video.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('D:/4_курс/АЦОМ/IZ/input_video/output_student.mp4', fourcc, fps, (width, height))

# Чтение первого кадра
ret, frame = input_video.read()
prev_frame = cv2.resize(frame, (1000, 600))

if not ret:
    print("Не удалось прочитать первый кадр.")
else:
    # Применение гауссового размытия к первому кадру
    prev_gauss_frame = cv2.GaussianBlur(prev_frame, (15, 15), 1)
    prev_gray_gauss_frame = cv2.cvtColor(prev_gauss_frame, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frame = input_video.read()
        curr_frame = cv2.resize(frame, (1000, 600))
        if not ret:
            break

        # Применение гауссового размытия к текущему кадру
        curr_gauss_frame = cv2.GaussianBlur(curr_frame, (15, 15), 1)
        curr_gray_gauss_frame = cv2.cvtColor(curr_gauss_frame, cv2.COLOR_BGR2GRAY)

        # Сравнение гауссовских кадров
        frame_diff = cv2.absdiff(curr_gray_gauss_frame, prev_gray_gauss_frame)
        _, binary_frame = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

        # Находим контуры объектов на бинарном изображении
        contours, _ = cv2.findContours(binary_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # contours = cv2.Canny(curr_frame, threshold1=100, threshold2=200)
        # cv2.imshow('123', contours)
        # double_filtration = borders(curr_frame, 15, 1.0)
        # cv2.imshow("frame123", double_filtration)

        # Задаем минимальную площадь контура
        min_contour_area = 2000
        for contour in contours:
            area = cv2.contourArea(contour)

            img_with_rectangle = curr_frame.copy()

            if area > min_contour_area:
                print(area, "\n")
                all_points = np.vstack(contours)  # Объединяем все контуры в один массив
                x, y, w, h = cv2.boundingRect(all_points)  # Находим ограничивающий прямоугольник для всех контуров

                # Рисуем ограничивающий прямоугольник на оригинальном изображении
                cv2.rectangle(img_with_rectangle, (x, y), (x + w, y + h), (0, 0, 0),2)
                cv2.imshow('Original with Bounding Rectangle', cv2.resize(img_with_rectangle, (500, 333)))
                output_video.write(img_with_rectangle)

                break  # Выход из цикла, если обнаружен хотя бы один контур

        # cv2.imshow('Binary', binary_frame)
        # cv2.imshow('Detected Objects', curr_frame)

        # Обновление предыдущего гауссовского кадра
        prev_gauss_frame = curr_gauss_frame

        # Задержка
        if fps > 0:
            delay = int(1000 / fps)
        else:
            delay = 1
        if cv2.waitKey(delay) & 0xFF == 27:
            break

end_time = time.time()
time = end_time - start_time
print(f"Время выполнения: {time} секунд")
# Освобождаем ресурсы
input_video.release()
output_video.release()
cv2.destroyAllWindows()


