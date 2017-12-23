import argparse
import os
import json
import graphmod
'''
Coded by Hydra

'''

if __name__ == "__main__":
        skeleton = ''
        """
        Parsing various input arguments
        """
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
                            help='Specify the chart_type for the project (supported: bar, forced)',
                            )

        parser.add_argument('-o', action="store", dest='output_file',
                            default="test.html",
                            help='Specify the output_file for the project ',
                            )

        parser.add_argument('-of', action="store", dest='output_folder',
                            help='Specify the output_folder for the project ',
                            )

        parser.add_argument('-stroke_width', action='store', dest='stroke_width',
                            default=1.5,
                            type=int,
                            help='Specify the stroke_width of links in pixels')

        parser.add_argument('--version', action='version', version='%(prog)s 1.0')


        results = parser.parse_args()
        print 'Title     =', results.title
        if results.chart_type == "bar":
            if results.output_folder:
                if not os.path.exists(os.path.dirname(results.output_folder+'/'+results.output_file)):
                    try:
                        os.makedirs(os.path.dirname(results.output_folder+'/'+results.output_file))
                        os.system("cp d3.v4.min.js ./"+results.output_folder+"/")
                        os.system("cp "+results.file_name+" ./"+results.output_folder+"/")
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                op = open(results.output_folder+"/"+results.output_file, "wb")
            else:
                op = open(results.output_file, "w")
            skeleton += graphmod.genhead(results.title)
            skeleton += graphmod.genbar(results.width, results.height, results.file_name)
            op.write(skeleton)
            op.close()
        elif results.chart_type == "forced":
            if results.output_folder:
                if not os.path.exists(os.path.dirname(results.output_folder+'/'+results.output_file)):
                    try:
                        os.makedirs(os.path.dirname(results.output_folder+'/'+results.output_file))
                        os.system("cp d3.v3.min.js ./"+results.output_folder+"/")
                        os.system("cp "+results.file_name+" ./"+results.output_folder+"/")
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(results.output_folder+"/graph.json", "wb") as js:
                    json.dump(graphmod.csvtojson(results.file_name), js)
                op = open(results.output_folder+"/"+results.output_file, "wb")
            else:
                with open("graph.json", "wb") as js:
                    json.dump(graphmod.csvtojson(results.file_name), js)
                op = open(results.output_file, "w")
            skeleton += graphmod.genhead(results.title)
            skeleton += graphmod.genforced_layout(results.width, results.height, results.file_name, results.stroke_width)
            op.write(skeleton)
            op.close()
        else:
            print "chart_type not supported yet!"
