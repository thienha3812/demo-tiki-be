from review.models import ImageReview


def save_img(request,review_id):
    for i in range(0,len(request.FILES)):
        img = request.FILES['img[' + str(i) + ']']
        ImageReview.create(review_id=review_id,img=img)
