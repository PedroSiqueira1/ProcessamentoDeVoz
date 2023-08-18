import cv2

# ATENÇÃO - ESSA FUNÇÃO FOI MOVIDA PARA MAIN
def detect_edges(path):

        # Using cv2.imread() method
        img = cv2.imread(path)

        # Converting image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        #cv2.imwrite('gray.png', gray)
        #cv2.imshow('gray.png', gray)


        # Applying GaussianBlur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        #cv2.imwrite('blur.png', blur)
       # cv2.imshow('blur.png', blur)

        # Applying Canny Edge detection
        canny = cv2.Canny(blur, 200,300)
        cv2.imwrite('canny.png', canny)
        cv2.imshow('canny.png', canny)

        # Finding contours

        contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Finding the biggest contour
        biggest = None
        max_area = 0
        for i in contours:
                area = cv2.contourArea(i)
                if area > 100:
                        peri = cv2.arcLength(i,True)
                        approx = cv2.approxPolyDP(i,0.02*peri,True)
                        if area > max_area and len(approx)==4:
                                biggest = approx
                                max_area = area

        # Draw the biggest contour
        cv2.drawContours(img, [biggest], -1, (0,255,0), 3)

        # Displaying the image with contour
        cv2.imwrite('te.png', img)
        cv2.imshow('print.png', img)
        cv2.waitKey()
        return [biggest[0][0], biggest[2][0]]

detect_edges('print.png')