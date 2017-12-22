import argparse
import graphmod
'''
Coded by Hydra

'''

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

        parser.add_argument('-chart_type', action="store", dest='chart_type',
                            default="bar",
                            help='Specify the chart_type for the project e.g bar',
                            )

        parser.add_argument('-o', action="store", dest='output_file',
                            default="test.html",
                            help='Specify the output_file for the project ',
                            )

        parser.add_argument('--version', action='version', version='%(prog)s 1.0')


        results = parser.parse_args()
        print 'Title     =', results.title
        if results.chart_type == "bar":
            op = open(results.output_file, "w")
            skeleton += graphmod.genhead(results.title)
            skeleton += graphmod.genbar(results.width, results.height, results.file_name)
            op.write(skeleton)
            op.close()
