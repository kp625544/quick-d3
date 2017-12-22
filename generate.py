import argparse


def genhead():
    return '<!DOCTYPE html>\n<meta charset="utf-8">\n<head>\n<script src="d3.v3.min.js"></script>\n</head>'

if __name__ == "__main__":
        skeleton = ''

        parser = argparse.ArgumentParser()

        parser.add_argument('-width', action='store', dest='width',
                            required=True,
                            type=int,
                            help='Specify the width of canvas in pixels')

        parser.add_argument('-height', action='store', dest='height',
                            required=True,
                            type=int,
                            help='Specify the height of canvas in pixels')

        parser.add_argument('-file_name', action="store", dest='file_name',
                            required=True,
                            help='Specify the file_name aka csv file',
                            )

        parser.add_argument('-title', action="store", dest='title',
                            default="Test project",
                            help='Specify the title for the project',
                            )

        parser.add_argument('--version', action='version', version='%(prog)s 1.0')


        results = parser.parse_args()
        print 'Title     =', results.title
        skeleton += genhead()
        print skeleton

#vdvd
