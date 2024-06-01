import face_recognition

def detect_face(image1,image2):
    img1 = 'media/'+str(image1)
    img2 = 'media/'+str(image2)
    known_image = face_recognition.load_image_file(img1)
    unknown_image = face_recognition.load_image_file(img2)

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    return results

# image1 = "nani.jpg"
# image2 = "nani_match2.jpg"
# print(detect_face(image1,image2))