# Chunky Documentation

This is a clone of the repository for the old Chunky documentation that was previously hosted at [https://chunky.llbit.se](https://chunky.llbit.se). The original repository for the old Chunky documentation is located at [https://github.com/llbit/chunky-docs](https://github.com/llbit/chunky-docs).

The current Chunky documentation is hosted at [https://chunky-dev.github.io/docs/](https://chunky-dev.github.io/docs/). As 'https://chunky.llbit.se' now redirects to 'https://chunky-dev.github.io/docs/', this repository exists to keep the old documentation website easily accessible, as the web archive version is slow to access, and not all resources may be completely saved there.

## Editing

You can edit any file easily right here on GitHub. All you need is a GitHub
account. You can navigate to a file you want to edit via the file tree and
click the `Edit` button after selecting a file. We use [Markdown syntax][3] for
all documentation pages.

## Dependencies

* Python
    * Python-Markdown
    * PIL

## Testing

The HTML pages can be generated in the local directory `out` using the
[Gradle][1] build script in the project root. Re-generate the HTML with
this command in a terminal: `./gradlew` (use just `gradle` on Windows).

The build script runs a Python script named `tools/mdwrapper.py` on all
Markdown files (`*.md`) in the `docs` directory. Before the python script is
run some special tokens such as `%VERSION%` are replaced with the values listed
in the `version.properties` file. The build script then creates thumbnails for
the gallery and finally copies all files in the `images` and `style`
directories into the output directory.

After you have run the build script you will need a web server to serve the
pages in the `out` directory in order to get them to render correctly in the
web browser. One of the simplest ways to set this up, if you have NodeJS and
NPM installed, is to run the following commands:

    $ npm install http-server -g
    $ cd out
    $ http-server -o --cors

Another way to do this with nodejs is with your own [small nodejs web server
script][2].


## Requirements

Python and python-markdown are required to generate the documentation pages.

    pip install markdown

The Python Imaging Library (PIL) is required to create thumbnail images for
the gallery. PIL can be installed by the command

    pip install pil

Alternatively, for Windows users, you can download Pillow from [here][4].


[0]:http://chunky.llbit.se/
[1]:http://gradle.org/
[2]:http://stackoverflow.com/a/13635318
[3]:http://daringfireball.net/projects/markdown/syntax
[4]:http://www.lfd.uci.edu/~gohlke/pythonlibs/
[5]:http://chunky.llbit.se/contributing.html#documentation
