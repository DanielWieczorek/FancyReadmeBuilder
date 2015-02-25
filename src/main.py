"""
This is a nifty little tool to create really cool looking Readme files.
Its essentially a templating tool for such. The initial steps to create a template are the following:
- create a super cool ANSI Art design for your readme.
- create a template that uses this image and defines fields where text can be inserted.

After that you can create fill this template with life with another file defining the actions, e.g. inserting text.

Parameters:
templatedir:
 desc: this parameter defines where to load the templates from
 type: str
 is_required: True
actions:
 desc: path to the file containing the actions
 type: str
 is_required: True
template:
 desc: name of the template to use
 type: str
 is_required: True

"""
from src.business.FancyReadmeBuilder import FancyReadmeBuilder
from src.ui.TerminalParser import TerminalParser

__author__ = 'DWI'


def main():
    parser = TerminalParser()
    args = parser.get_values(__doc__)

    readme_builder = FancyReadmeBuilder.get_instance()
    print(args.templatedir)
    readme_builder.load_templates(args.templatedir)
    print(args.actions)
    print(args.template)
    rendered = readme_builder.apply_actions_and_render(args.actions, args.template)
    print(rendered)


if __name__ == "__main__":
    main()

