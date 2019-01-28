from abc import ABCMeta, abstractmethod
from typing import List, Optional

GITHUB = 1
TRAVIS = 2
HEROKU = 3
CODECOV = 4


class Hint(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, hint_id: int, type: str) -> None:
        self.id = hint_id
        self.type = type


class TextHint(Hint):
    def __init__(self, hint_id: int, text: str) -> None:
        super().__init__(hint_id, "text")
        self.text = text


class ScreenshotHint(Hint):
    def __init__(self, hint_id: int, image: str, alt: str, caption: Optional[str] = "") -> None:
        super().__init__(hint_id, "screenshot")
        self.image = image
        self.alt = alt
        self.caption = caption


class CodeHint(Hint):
    def __init__(self, hint_id: int, code: List[str]) -> None:
        super().__init__(hint_id, "code")
        self.code = code


class WorkshopHints:
    def __init__(self, hints: Optional[dict] = None) -> None:
        if hints:
            self.__hints = hints
        else:
            self.__hints = {
                GITHUB: [
                    TextHint(1, "The Fork button can be found on the top right of the page."),
                    ScreenshotHint(2, "img/github/fork.png", "Fork me!"),
                    ScreenshotHint(3, "img/github/forked.png", "Forked", "Once the forking process is complete you are owner of this fork.")
                ],
                CODECOV: [
                    ScreenshotHint(4, "img/codecov/authorize.png", "Allow Codecov access to your GitHub account", "Codecov needs access to your GitHub account in order to work properly."),
                    ScreenshotHint(5, "img/codecov/app-install.png", "Codecov suggests to install the app", "Codecov will by default suggest to also enable the app for better integration."),
                    ScreenshotHint(6, "img/codecov/app-install2.png", "Allow the Codecov app access to your GitHub account", "The Codecov app needs access to some features of your GitHub account in order to be able to better integrate.")
                ],
                TRAVIS: [
                    ScreenshotHint(7, "img/heroku/create-new-app.png", "Create New App", "A new app and pipeline are created at the same time."),
                    ScreenshotHint(8, "img/heroku/connect-app-github.png", "Connect to GitHub", "The app is now linked to the GitHub repository."),
                    ScreenshotHint(9, "img/heroku/add-postgres.png", "Add free add-on", "Heroku Postgres offers a free data plan which can be used."),
                    ScreenshotHint(10, "img/heroku/connect-pipeline-github.png", "Connect to GitHub", "Connecting the pipeline to the same GitHub repository as the app will allow us to enable review apps in a later step."),
                    ScreenshotHint(11, "img/heroku/final-result.png", "Pipeline overview", "The pipeline now should look like this."),
                    ScreenshotHint(12, "img/heroku/pipeline-overview.png", "Pipeline overview", "Heroku provides a shortcut on how to enable the review apps on their site"),
                    ScreenshotHint(13, "img/heroku/enable-review-apps.png", "", "Once all settings are filled in (by default you don't need to change anything), you can just have Heroku commit the file to your repository."),
                    ScreenshotHint(14, "img/heroku/retrieve-api-key.png", "The API key", "This API key is needed to ensure that Travis can deploy to Heroku.")
                ],
                HEROKU: [
                    ScreenshotHint(15, "img/travis/sign-up.png", "Sign up on Travis CI", "The home page lists a nice big green button that wants to be clicked"),
                    ScreenshotHint(16, "img/travis/authorize.png", "Allow Travis access to your GitHub account", "Travis needs access to your GitHub account in order to work properly."),
                    ScreenshotHint(17, "img/travis/enable.png", "Flip the switch", "Enabling Travis CI for a repository is as \"easy\" as toggling a switch."),
                    ScreenshotHint(18, "img/travis/secure-encrypt.png", "Securely encrypted API key", "Using the python tool you get a securely encrypted key that can be worrilessly pasted in the Travis configuration file."),
                    CodeHint(19, code=[
                        "language: python",
                        "python:",
                        "  - 3.6",
                        "  - nightly",
                        "install:",
                        "  - pip install -r requirements/dev.txt",
                        "script:",
                        "  - nosetests --with-cov --cov-config .coveragerc",
                        "after_success:",
                        "  - codecov",
                        "jobs:",
                        "  include:",
                        "    - stage: Deploy",
                        "      script: skip",
                        "      deploy:",
                        "        provider: heroku",
                        "        api_key:",
                        "          secure: {insert secret here}",
                        "        app: {your-app-name-here}",
                        "        on:",
                        "          repo: {gh_username}/ci_workshop"
                    ]),
                    ScreenshotHint(20, "img/travis/failed-build.png", "Failed build", "Even when you are experienced with software, things sometimes take some trial and error...")
                ]
            }

    def get_hints_for_step(self, step: int) -> List[Hint]:
        return self.__hints[step] if step in self.__hints else []
