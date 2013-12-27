# Python script to create barebone sbt/Scala project

###Usage

* type below for usage:

```python
./createScalaProject.py --help 
```
    usage: createScalaProject.py [-h] [-n NAME] -o ORGANIZATION [-s SCALAVERSION]
                                 [-v VERSION] [-p PATH]

    This program will generate the barebone sbt project directories based on you
    specified options.

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --name NAME  the name of your project
      -o ORGANIZATION, --organization ORGANIZATION
                            the project organization, e.g. com.onescreen.tools,
                            bio.scala
      -s SCALAVERSION, --scalaVersion SCALAVERSION
                            the scalaVersion, default=[2.10.3]
      -v VERSION, --version VERSION
                            the scalaVersion, default=[0.10-SNAPSHOT]
      -p PATH, --path PATH  the path that you wanna current project resides on. By
                            default, this is "."
    above will generate output like below:

* Example Usage:

```python
./createScalaProject.py --name hello --organization com.onescreen.tools 
```

Above step will create a directory structure like below:

    hello/
    |-- build
    |-- build.sbt
    |-- lib
    |-- project
    |   `-- plugins.sbt
    `-- src
        |-- main
        |   `-- scala
        |       `-- com
        |           `-- onescreen
        |               `-- tools
        `-- test
            `-- scala
                `-- com
                    `-- onescreen
                        `-- tools

###LISCENSE

  MIT
