from src.business.TemplateManager import TemplateManager
from src.data.InputFileType import InputFileType
from src.data.action.TemplateActionReaderFactory import TemplateActionReaderFactory
from src.data.template.TemplateReaderFactory import TemplateReaderFactory

__author__ = 'DWI'




def main():
    template_manager = TemplateManager(TemplateReaderFactory())

    template_manager.load_templates("./templates")
    template = template_manager.get_template("test")

    actions = TemplateActionReaderFactory().build_for_type(InputFileType.yaml).read("./config/actions.yaml")

    for action in actions:
        action.apply_to(template)

    print(template.render())


if __name__ == "__main__":
    main()

