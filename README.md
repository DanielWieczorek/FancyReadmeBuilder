# Build Fancy Readmes

This is going to be a little tool to build cool Readme, NFO or similar files. 

# How is it going to work?

The user can create Templates for his Readme files. These templates are described in YAML.
Its description contain the background image (ANSI Art) and a set of named fields with coordinates (like a text box, really).

To fill these fields with life create a description of the Readme you want in yaml. There is for a set of templated defined what text should be inserted into the fields.


python3 src/main.py --templatedir ./templates --actions ./config/actions.yaml --template test