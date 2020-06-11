import cv2

IMAGE_HEIGHT = 60
IMAGE_WIDTH  = 160

def get_grayscale_image(image_path):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMAGE_WIDTH, IMAGE_HEIGHT), )
    img = img / 255

    return img

if __name__ == '__main__':

    image_path = './000a.png'
    image = get_grayscale_image(image_path)

    print(image)
    cv2.imshow("gray_img", image)  # 可视化
    cv2.waitKey(0)