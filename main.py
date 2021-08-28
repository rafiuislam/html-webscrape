from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    get_content = html_file.read()

    soup = BeautifulSoup(get_content, 'lxml')
    tags = soup.find_all('div', class_='card')
    for course in tags:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs: {course_price}')
       