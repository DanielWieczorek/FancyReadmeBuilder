from src.business.FancyReadmeBuilder import FancyReadmeBuilder
from src.business.TemplateManager import TemplateManager
from src.data.action.TemplateActionReaderFactory import TemplateActionReaderFactory
from src.data.template.TemplateReaderFactory import TemplateReaderFactory

__author__ = 'DWI'




def main():
    template_manager = TemplateManager(TemplateReaderFactory())
    readme_builder = FancyReadmeBuilder(template_manager,TemplateActionReaderFactory())

    readme_builder.load_templates("./templates")

    rendered = readme_builder.apply_actions_and_render("./config/actions.yaml", "test")
    print(rendered)


if __name__ == "__main__":
    main()

