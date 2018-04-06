# Original Author: Shubhangi Tandon
# Modified By: Zhichao Hu
# Modified to download the webpage files to local storage. Edit "filePath" and "fileName" to fit your needs. This script
# downloads the files to the directory from where you RUN this script (because of wget).

import csv
import os
import sys

from subprocess import call


def download_html(filename):
    path = os.getcwd()
    dirname = filename.split(".")[0]
    call(["mkdir", dirname])
    os.chdir(dirname)
    # filePath = '/afs/cats.ucsc.edu/class/cmps012b-pt.w18/bin/moss/result_upload/' + filename
    filePath = '/Users/zhichaohu/Downloads/cmps12a_ptantalo_w18/' + filename
    with open(filePath, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            html_link = row[3]
            # print html_link
            # call(["wget", html_link])
            html_top = html_link.replace(".html", "-top.html")
            html_0 = html_link.replace(".html", "-0.html")
            html_1 = html_link.replace(".html", "-1.html")
            html_list = [html_link, html_top, html_0, html_1]
            tempdir = html_link.split('/')[-1].split('.')[0]
            call(["mkdir", tempdir])
            # call(["cd", tempdir])
            prev = os.getcwd()
            os.chdir(os.getcwd() + "/" + tempdir)
            for html in html_list:
                call(["wget", html])
            # call(["cd", ".."])
            os.chdir(prev)


# filename = sys.argv[1]
filename = "pa6_MT_20180319_Java.csv"
download_html(filename)
