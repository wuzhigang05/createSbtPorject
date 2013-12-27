# Python script to create barebone sbt/Scala project

###Usage

* type below for usage:

```python
  ./createScalaProject.py --help 
```

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
