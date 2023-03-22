import cv2
list_of_names = []


def cleanup_data():
    with open("name-list.txt") as file:
        for line in file:
            list_of_names.append(line.strip())
                    
                        
            

def generate_certificates():
    for name in list_of_names:
        template = cv2.imread("Codution Internship certificate.jpg")
        cv2.putText(template, name, (606,727), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (125, 158, 192), 3, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificated-data/{name}.jpg',template)
           



cleanup_data()
generate_certificates()

