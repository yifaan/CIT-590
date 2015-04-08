import string


def GetName(text):
    '''get name from resume'''
    f = open(text)
    name = f.readline().lstrip().rstrip()
    if name[0] in string.ascii_uppercase:
        return name
    else:
        raise NameError(
            'First line should be name with first letter uppercase')


def GetEmail(text):
    '''get email from resume'''
    f = open(text)
    for line in f:
        if '@' in line:
            email = line.lstrip().rstrip()
    lastfour = email.split('.')[-1]
    string = email.split('@')[-1].split(lastfour)[0]

    if lastfour != 'edu' and lastfour != 'com':
        raise NameError('last four characters should be edu or com')
    elif string == '.':
        raise NameError('Should have a string between @ and last four digit')
    else:
        return email


def GetCourse(text):
    '''get courses from resume'''
    f = open(text)
    for line in f:
        if 'Courses' in line:
            courseline = line
    coursesplited = courseline.split('Courses')[-1].splitlines()[0].split(',')
    courses = []
    for coursepunc in coursesplited:
        course = ''
        for ch in coursepunc:
            if ch not in string.punctuation:
                course = course + ch

        courses.append(course.lstrip().rstrip())
    return courses


def GetProjects(text):
    '''get projects from resume'''
    f = open(text)
    for line in f:
        if 'Projects' in line:
            break

    projects = []
    for line in f:
        if '------' not in line:
            if line.splitlines()[0].lstrip().rstrip() != '':
                projects.append(line.splitlines()[0].lstrip().rstrip())
        else:
            break
    return projects


def GetEducation(text):
    '''get education from resume'''
    f = open(text)
    Edu = []
    for line in f:
        if 'university' in line or 'University' in line:
            Edu.append(line.splitlines()[0].lstrip().rstrip())
    return Edu


def WriteHTML(html, tag, text, flag):
    '''write in html'''
    f = open(html, 'r+')
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    del lines[-1]
    del lines[-1]
    if flag is True:
        del lines[-1]
    lines += surround_block(tag, text)
    f.writelines(lines)
    if flag is True:
        f.writelines('\n</div>\n</body>\n</html>')
    else:
        f.writelines('\n</body>\n</html>')


def intro(name, email):
    '''get the html for intro'''
    text = '<h1 >\n' + name + '\n</h1>\n<p>\n' + email + '\n</p>'
    return text


def Eduhtml(education):
    '''generate education html'''
    text = '<h2>Education</h2>\n<ul>\n'
    for i in range(0, len(education)):
        text += '<li>\n' + education[i] + '\n</li>\n'
    text += '</ul>'
    return text


def Projecthtml(projects):
    '''generate education html'''
    text = '<h2>\nProjects\n</h2>\n<ul>\n'
    for i in range(0, len(projects)):
        text += '<li>\n<p>\n' + projects[i] + '\n</p>\n</li>\n'
    text += '</ul>'
    return text


def Courseshtml(courses):
    '''generate course html'''
    text = '<h3>\nCourses\n</h3>\n'
    courselist = ', '.join(courses)
    text += '<span>\n' + courselist + '\n</span>'
    return text


def surround_block(tag, text):
    '''generate the <tag>'''
    text = '<div ', tag, '>\n', text, '\n</div>'
    return text


def main():
    resumehtml = 'resume.html'
    resume = 'resume.txt'
    WriteHTML(resumehtml, 'id="page-wrap"', '', False)
    name = GetName(resume)
    email = GetEmail(resume)
    WriteHTML(resumehtml, '', intro(name, email), True)
    education = GetEducation(resume)
    WriteHTML(resumehtml, '', Eduhtml(education), True)
    project = GetProjects(resume)
    WriteHTML(resumehtml, '', Projecthtml(project), True)
    courses = GetCourse(resume)
    WriteHTML(resumehtml, '', Courseshtml(courses), True)


if __name__ == '__main__':
    main()
