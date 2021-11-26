#!/usr/bin/env python
# -*- coding: utf-8 -*-

plik = 'forerunner-activity_7863152973_mod.tcx'

import xml.etree.ElementTree as ET
import re
import argparse


parser = argparse.ArgumentParser(description='Process tcx data')
parser.add_argument('--tcx', dest='tcxFile', required=True,
                   help='input tcx file')

args = parser.parse_args()
tcxFile = args.tcxFile


print("time,dist,speed,cad")
with open(tcxFile) as xml_file:
    xml_str = xml_file.read()
    xml_str = re.sub(' xmlns="[^"]+"', '', xml_str, count=1)
    root = ET.fromstring(xml_str)
    activities = root.findall('.//Activity')
    for activity in activities:
        #print('-- {} --'.format(activity.attrib['Sport']))
        tracking_points = activity.findall('.//Trackpoint')
        for tracking_point in list(tracking_points):
            children = list(tracking_point)
            # garmin
            #[<Element 'Time' at 0x7feb6e908270>, <Element 'Position' at 0x7feb6e908310>, <Element 'AltitudeMeters' at 0x7feb6e9084f0>, 
            # <Element 'DistanceMeters' at 0x7feb6e908590>, <Element 'HeartRateBpm' at 0x7feb6e908630>, <Element 'Extensions' at 0x7feb6e9086d0>]
            # polar
            #[<Element 'Time' at 0x7fba2bcc8c70>, <Element 'Position' at 0x7fba2bcc8d10>, 
            # <Element 'DistanceMeters' at 0x7fba2bcc8e50>, <Element 'Cadence' at 0x7fba2bcc8ef0>, <Element 'SensorState' at 0x7fba2bcc8f40>]
            print(children)
            print(children['Position'])
            exit(1)
            print("%s,%s,%s,%s" % (children[0].text, children[3].text, list(children[5][0])[0].text, list(children[5][0])[1].text) )