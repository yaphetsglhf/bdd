Feature:
    Scenario Outline: Blenders
        Given I put <thing> in a blender
        When I switch the blender on
        Then it should transform into <otherthing>

    Examples: Amphibians
    | thing         | otherthing |
    | Red Tree Frog | mush        |
    | iPhone        | toxic waste |
    | Galaxy Nexus  | Korea phone |
