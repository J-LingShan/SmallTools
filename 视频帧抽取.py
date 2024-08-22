import os.path

import cv2


def extractPic(vidoPath, targetPath, img_size=(), interval=4, pic=16, imgType='.jpg'): # img_size提取视频帧储存,元组：(height,width)
    video = cv2.VideoCapture(vidoPath)
    if not video.isOpened():
        print("视频加载失败")
        return False
    else:
        print("视频加载成功")

    video_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while video_count // interval <= pic:
        interval -= 1

        if interval <= 0:
            print(f"视频帧数不满足，您所设置的pic:{pic}")
            return False

    temp = 0  # 记录提取的帧，当已提取interval张，则归0
    now_pic_count = 0
    isRead = True
    while isRead and now_pic_count <= pic:
        isRead, img = video.read()

        if img is None:
            continue

        if temp == interval:
            temp = 0

        if img_size[0] != video_height and img_size[1] != video_width:
            img = cv2.resize(img, img_size)
            cv2.imwrite(filename=os.path.join(targetPath,f"{now_pic_count}{imgType}"), img=img)
            temp += 1
            now_pic_count += 1
            print(f"提取第{now_pic_count}张")

    video.release()


if __name__ == "__main__":

    extractPic("1.avi", "./", img_size=(128, 172), interval=4, pic=16)












