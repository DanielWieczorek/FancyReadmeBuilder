from src.business.FancyReadmeBuilder import FancyReadmeBuilder

__author__ = 'DWI'


def main():
    readme_builder = FancyReadmeBuilder.get_instance()

    readme_builder.load_templates("./templates")

    rendered = readme_builder.apply_actions_and_render("./config/actions.yaml", "test")
    print(rendered)


if __name__ == "__main__":
    main()

