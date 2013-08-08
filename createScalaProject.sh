#!/bin/bash

function Usage {
  echo $0 "<project name>"
  exit 1
}

DIR="`pwd`"

if [[ $# -lt 1 ]]
then
  echo "Project Name:"
  read projectName
  if [[ "$projectName" -eq "" ]]
  then
    projectName="test"
  fi
else
  projectName="$1"
fi


mkdir -p "$projectName"/src/main/scala
mkdir -p "$projectName"/src/main/java
mkdir -p "$projectName"/src/test/scala
mkdir -p "$projectName"/src/test/java

mkdir -p "$projectName"/build
mkdir -p "$projectName"/lib

function writeSbtFile {
  dirname=$1
  projectName=`basename $1`
  targetSbt="$dirname"/build.sbt
  echo -e "name := \"$projectName\"\n" >"$targetSbt"
  echo -e "version := \"0.1\"\n" >>"$targetSbt"
  echo -e "scalaVersion := \"2.10.2\"\n" >>"$targetSbt"
}

writeSbtFile "$DIR/$projectName"
