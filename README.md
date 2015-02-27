# Build Fancy Readmes

This is going to be a little tool to build cool Readme, NFO or similar files. 

# How is it going to work?

The user can create Templates for his Readme files. These templates are described in YAML.
Its description contain the background image (ANSI Art) and a set of named fields with coordinates (like a text box, really).

To fill these fields with life create a description of the Readme you want in yaml. There is for a set of templated defined what text should be inserted into the fields.

# Defining Templates

Templates are currently defined in YAML like this:
```
test:
 background: ./templates/img/nfo1.ans

 fields:
  author:
   start_coord: (20,47)
   end_coord: (60,47)
   type: rect
```
"test" is the name of the template, background is path to the ANSI art that acts as base for the readme file.
the next part is the definition of fileds. In this case there is a rectagular field defined that has the name "author". The start coord is the upper left corner and the end coord is the bottom right corner.

# Defining Actions

At the moment the only format in which the actions can be defined is YAML. E.g. such an action definition file contains entries like this:
```
author:
 type: update
 value: "Daniel Wieczorek"
```

the field updated is author, the action is an updated and the value that is written to the field is my name :). There can be numerous entries like this in the file

# Run the sample
To run the sample just execute the the following command:
```
python3 src/main.py --templatedir ./templates --actions ./config/actions.yaml --template test
```

To show what the tool does heres the 'before':
```



                                  ▄▄    ▄▄███▄▄
                                █████▓▄████████▓
                              ▄▄▀████████████▓▀
                      ▄▄████ ██▓▒ █████████▓▀▀▒▓███▄
                     ▐██████ ██▓▒▀▄██████▄ ▄▒▒▓██████
                     ████████ ▓▒ ████████▓▓ ▒▓██▀████▓
                     ▐████ ██▄▀▓▒▄ █████▓ ▄▒▓██ █████▓▌
                      █████ ███▓▒ ██████▓ ▒▓██▄█████▓█
                       █████▄▀██▓▒▄▀███▀ ▒▓███████▓▓▀
                        ▀█████▄▀█▓▒▀ ▀    ▀▀▀███▓▀▀
                          ▀███▀


                           D E S C R I P T I O N                               ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                               U S A G E                                      ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                             A U T H O R S                                    ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
```
and heres the 'after':




                                  ▄▄    ▄▄███▄▄
                                █████▓▄████████▓
                              ▄▄▀████████████▓▀
                      ▄▄████ ██▓▒ █████████▓▀▀▒▓███▄
                     ▐██████ ██▓▒▀▄██████▄ ▄▒▒▓██████
                     ████████ ▓▒ ████████▓▓ ▒▓██▀████▓
                     ▐████ ██▄▀▓▒▄ █████▓ ▄▒▓██ █████▓▌
                      █████ ███▓▒ ██████▓ ▒▓██▄█████▓█
                       █████▄▀██▓▒▄▀███▀ ▒▓███████▓▓▀
                        ▀█████▄▀█▓▒▀ ▀    ▀▀▀███▓▀▀
                          ▀███▀


                           D E S C R I P T I O N                               ▐
▌                                                                              ▐
▌         Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo H        ▐
▌         allo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Ha        ▐
▌         llo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hal        ▐
▌         lo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hall        ▐
▌         o Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo        ▐
▌          Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo         ▐
▌         Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo H        ▐
▌         allo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Ha        ▐
▌         llo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hal        ▐
▌                                                                              ▐
▌                               U S A G E                                      ▐
▌                                                                              ▐
▌         foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo b        ▐
▌         ar foo bar foo bar foo bar foo bar foo bar foo bar foo bar fo        ▐
▌         o bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar        ▐
▌          foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo         ▐
▌         bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar f        ▐
▌         oo bar foo bar foo bar foo bar foo bar foo bar foo bar foo ba        ▐
▌         r foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo        ▐
▌          bar foo bar foo bar foo bar foo bar foo bar foo bar                 ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                             A U T H O R S                                    ▐
▌                                                                              ▐
▌                                                                              ▐
▌                   Daniel Wieczorek                                           ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
▌                                                                              ▐
