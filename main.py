import numpy as np
import cv2

def flattener(image, pts, w, h):
    """Flattens an image of a card into a top-down 200x300 perspective."""
    temp_rect = np.zeros((4, 2), dtype="float32")

    s = np.sum(pts, axis=2)
    tl = pts[np.argmin(s)]
    br = pts[np.argmax(s)]

    diff = np.diff(pts, axis=-1)

    tr = pts[np.argmin(diff)]
    bl = pts[np.argmax(diff)]

    if w <= 0.8 * h:
        temp_rect[0] = tl
        temp_rect[1] = tr
        temp_rect[2] = br
        temp_rect[3] = bl

    if w >= 1.2 * h:
        temp_rect[0] = bl
        temp_rect[1] = tl
        temp_rect[2] = tr
        temp_rect[3] = br

    if 0.8 * h < w < 1.2 * h:
        if pts[1][0][1] <= pts[3][0][1]:
            temp_rect[0] = pts[1][0]
            temp_rect[1] = pts[0][0]
            temp_rect[2] = pts[3][0]
            temp_rect[3] = pts[2][0]
        if pts[1][0][1] > pts[3][0][1]:
            temp_rect[0] = pts[0][0]
            temp_rect[1] = pts[3][0]
            temp_rect[2] = pts[2][0]
            temp_rect[3] = pts[1][0]

    maxWidth = 150
    maxHeight = 200

    temp_rect += np.array([[-30, -30], [30, -30], [30, 30], [-30, 30]], dtype="float32")

    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], np.float32)
    M = cv2.getPerspectiveTransform(temp_rect, dst)
    warp = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warp

def getPhoto(image):
    img = cv2.imread(image)
    
    img_width, img_height = np.shape(img)[:2]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    background = img_gray[int(img_height / 100)][int(img_width / 2)]
    thresh_lvl = background + 80
    print(thresh_lvl)
    if (thresh_lvl > 200):
        thresh_lvl = 200
    
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    _, thresh = cv2.threshold(img_blur, thresh_lvl, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contourValues = [cv2.contourArea(i) for i in contours]
    contourValues.sort()
    
    biggestContour = max(contours, key=cv2.contourArea)

    if len(contourValues) != 0:
        peri = cv2.arcLength(biggestContour, True)
        # Increase the accuracy parameter for better corner approximation
        approx = cv2.approxPolyDP(biggestContour, 0.01 * peri, True)
        pts = np.float32(approx)
        x, y, w, h = cv2.boundingRect(biggestContour)
        CardWidth, CardHeight = w, h
        smallest = float("inf")
        for pt in pts:
            total = pt[0, 0] + pt[0, 1]
            if total < smallest:
                x = int(pt[0, 0])
                y = int(pt[0, 1])
                smallest = total
        average = np.sum(pts, axis=0) / len(pts)
        cent_x = int(average[0][0])
        cent_y = int(average[0][1])
        CardCenter = [cent_x, cent_y]
        cropped = img[x:x + w, y:y + h]
        img = flattener(img, pts, w, h)

    cv2.imwrite('pokemon.png', img)
    cv2.imshow('thresh', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

getPhoto("images/IMG_2370.png")
