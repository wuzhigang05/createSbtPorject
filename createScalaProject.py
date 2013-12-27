#!/usr/bin/env python2.7
import sys
import argparse
import os
import shutil


def createDir(args):
  cwd = os.getcwd()
  if os.path.exists(args.title):
    res = raw_input('%s direcotry exists. Type Y to replace, N to exit\n' % args.title)
    if res.lower() == 'y':
      shutil.rmtree(args.title)
      create(args)
  else:
    create(args)

def writeSbtFile(args):
  cwd = os.getcwd()
  project = os.path.join(cwd, args.title)
  sbtfile = os.path.join(project, 'build.sbt')
  with open(sbtfile, 'w') as OUT:
    OUT.write('''name           := "%s"\n\n''' % args.title)
    OUT.write('''version        := "0.1.0"\n\n''')
    OUT.write('''organization   := "%s"\n\n''' % args.organization)
    OUT.write('''scalaVersion   := "%s"\n\n''' % args.scalaVersion)
    OUT.write('''unmanagedBase  := baseDirecotry.value / "custom_lib"\n\n''')
  
def writePluginsFile(args):
  cwd = os.getcwd()
  project = os.path.join(cwd, args.title)
  project = os.path.join(project, 'project')
  pluginsFile = os.path.join(project, 'plugins.sbt')
  with open(pluginsFile, 'w') as OUT:
    OUT.write('''addSbtPlugin("com.typesafe.sbteclipse" % "sbteclipse-plugin" % "2.2.0")\n\n''')
    OUT.write('''addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.9.1") \n\n''')

def create(args):
  cwd = os.getcwd()
  if args.path != ".":
    if not os.path.exists(args.path):
      os.mkdirs(args.path)
    cwd = args.path
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
  writePluginsFile(args)

if __name__ == '__main__': 
  o = sys.stdout
  e = sys.stderr
  parser= argparse.ArgumentParser(
      description="This program will generate the barebone sbt project directories " + 
      "based on you specified options.")
  parser.add_argument('-n', "--name", help="the name of your project", default ="test")
  parser.add_argument('-o', "--organization", required=True, 
      help="the project organization, e.g. com.onescreen.tools, bio.scala")
  parser.add_argument('-s', "--scalaVersion", help="the scalaVersion, default=[2.10.3]",
      default="2.10.3")
  parser.add_argument('-v', "--version", help="the scalaVersion, default=[0.10-SNAPSHOT]",
      default="0.10-SNAPSHOT")
  parser.add_argument("-p", "--path", 
      help="the path that you wanna current project resides on. By default, this is \".\"",
      default = ".")
  args = parser.parse_args()
  createDir(args) 
