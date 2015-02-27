'''
Created on 16.12.2013

@author: Daniel Wieczorek


'''
import argparse

import yaml


class TerminalParser(object):
    """
    Extension of argparse to configure the options by the comment added to the main python file. There are 3 Ways to specify the
    parameter, depending on the number of settings you need. YAML is used as format. The general syntax is as
    follows:
    <some text>
    Parameters:
    option1: 
    option2: desc
    option3:
     desc: my description
     is_required: True
     type: str
     values: [value1, value2]
    """
    def get_program_description(self,comment):
        """
        Reads lines until the end of the comment was reached or a line that starts with "Parameters:"
        :param comment: full comment that is being read
        :type comment: str
        """
        result = ""
        for line in comment.splitlines(True):
            if not line.startswith("Parameters:"):
                result += line
            else: 
                break
        return result
    
    def get_parameters(self,comment):
        """
        Extracts the substring that contains the parameters in YAML notation 
        :param comment: full comment that is being read
        :type comment: str
        """
        parameter_marker_line = comment.find("Parameters:\n")
        if parameter_marker_line > -1:
            yaml_string = comment[parameter_marker_line+len("Parameters:\n"):]
            return yaml.load(yaml_string)
        else:
            return None
        
    def parse_comment(self,comment):
        """
        Parses the full comment and extracts the parameters and description + adds the parameters to an ArgumentParser
        :param comment: full comment that is being read
        :type comment: str
        """
        program_description = self.get_program_description(comment)
        parameters = self.get_parameters(comment)
        parser = argparse.ArgumentParser(description=program_description)
        if parameters:
            self.add_parameters(parser,parameters)
        return parser
        
    
    def add_parameters(self,parser, yaml_dict):
        """
        Adds all parameters from the dictionary to the ArgumentParser
        :param yaml_dict: the dict that was generated by the YAML lib
        :type yaml_dict: dict
        :param parser: the Argparser, that is filled with data
        :type parser: ArgumentParser
        """
        for key in yaml_dict.keys():
            self.add_parameter(parser, yaml_dict.get(key),key)
    
    def add_parameter(self, parser, yaml_entry, name):
        """
        Adds the parameter from the yaml entry to the ArgumentParser
        :param yaml_entry: the dict that was generated by the YAML lib
        :type yaml_entry: dict
        :param parser: the Argparser, that is filled with data
        :type parser: ArgumentParser
        :param parser: name of the yaml entry. got lost when doing get() on a list
        :type parser: str
        """
        param_name = "--"+name
        param_value = name
        if type(yaml_entry) is type(""):
            param_desc = yaml_entry
            parser.add_argument(param_name, dest=param_value, help=param_desc)
        else:
            param_choices = yaml_entry.get("choices")
            param_type = yaml_entry.get("type") or "str"
            param_desc = yaml_entry.get("desc")
            is_required = bool(yaml_entry.get("is_required"))
            parser.add_argument(param_name, type=eval(param_type), choices=param_choices, required=is_required, dest=param_value, help=param_desc)
        
    def get_values(self, comment):
        """
        parses the string and returns the parameters of the Program as Namespace object (as argparse does)
        :param comment: full comment of the main file
        :type comment: str

        """
        return self.parse_comment(comment).parse_args()