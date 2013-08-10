#!/usr/bin/env python2.7
import sys
import pdb
import argparse
import os
import shutil


def createDir(args):
  cwd = os.getcwd()
  if os.path.exists(args.title):
    res = raw_input('%s direcotry exists. Type Y to replace, N to exit' % args.title)
    if res.lower() == 'y':
#      os.removedirs(args.title)
      shutil.rmtree(args.title)
      create(args)
  else:
    create(args)

def writeSbtFile(args):
  cwd = os.getcwd()
  project = os.path.join(cwd, args.title)
  sbtfile = os.path.join(project, 'build.sbt')
  with open(sbtfile, 'w') as OUT:
    OUT.write("name           := %s\n\n" % args.title)
    OUT.write("version        := 0.1.0\n\n")
    OUT.write("organization   := %s\n\n" % args.organization)
  

def create(args):
  cwd = os.getcwd()
  project = os.path.join(cwd, args.title)
  os.mkdir(project)
  
  orgString = ""
  for i in args.organization.split('.'):
    orgString = os.path.join(orgString, i)

  main = os.path.join('src', os.path.join('main', 
    os.path.join('scala', orgString)))
  test = os.path.join('src', os.path.join('test', 
    os.path.join('scala', orgString)))

  for folder in ['project', 'build', 'lib', main, test]:
    try:
      os.makedirs(os.path.join(project, folder))
    except:
      pdb.set_trace()
  writeSbtFile(args)

if __name__ == '__main__': 
  o = sys.stdout
  e = sys.stderr
  parser= argparse.ArgumentParser(
      description="This program will generate the barebone sbt project directories " + 
      "based on you specified options.")
  parser.add_argument('-t', "--title", help="the title of your project", default ="test")
  parser.add_argument('-o', "--organization", help="the project organization, e.g. com.onescreen.tools",
      default="com.onescreen.tools")
  args = parser.parse_args()
  createDir(args) 
