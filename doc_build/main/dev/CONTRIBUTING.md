### Contributing
#### Setup
To set up a development install, please:
* Fork this repository
* Clone your fork

    `git clone https://github.com/YOUR_USERNAME/amap-python`
    
    `cd amap-python`
* Add this repository as the upstream

    `git remote add upstream https://github.com/SainsburyWellcomeCentre/amap-python`
    
* Install an editable, development version of `amap`. 

    `pip install -e .[dev]`

* To keep your fork up to date:

    `git fetch upstream`
    
    `git merge upstream/master`
    
#### Pull requests
In all cases, please submit code to the main repository via a pull request. 
Upon approval, please merge via "Squash and Merge" on Github to maintain a 
clean commit history.

#### Formatting
`amap` uses [Black](https://github.com/python/black) to ensure a consistent 
code style. Please run `black ./ -l 79 --target-version py37` before making 
any commits. To prevent any errors, it is easier to add a formatting check 
as a [pre-commit hook](https://www.atlassian.com/git/tutorials/git-hooks). 
E.g. on linux by adding this to your `.git/hooks/pre-commit`:

    black ./ -l 79 --target-version py37 --check || exit 1
    
#### Testing
`amap` uses [pytest](https://docs.pytest.org/en/latest/) for testing. Please 
try to ensure that all functions are tested in `tests/tests/test_unit` and 
all workflows/command-line tools are tested in `tests/tests/test_integration`.


#### Travis
All commits & pull requests will be build by [Travis](https://travis-ci.com). 
To ensure there are no issues, please check that it builds: `pip install .` 
and run all of the tests: `pytest` before commiting changes. 


#### Releases
Travis will automatically release any tagged commit on the master branch. 
Hence to release a new version of amap, use either GitHub, or the git 
CLI to tag the relevant commit and push to master.


#### Documentation
Documentation is built using Sphinx with Markdown (rather than 
reStructuredText). Please edit (or create new) `.md` files in the appropriate 
directory in `amap-python/doc_build`. The organisation of these files is then 
defined in `index.rst`.

Please ensure that:
* Any new changes are added to the release notes
(`doc_build/main/about/release_notes.md`)
* All command-line functions are fully documented, including an explanation 
of all arguments, and example syntax.

To build the documentation (assuming you installed amap with 
`pip install -e .[dev]` to install the dependencies):

```bash
cd doc_build
make html
```

Prior to commmiting to master, ensure that contents of 
`doc_build/_build/html/` is copied to `amap-python/docs` for 
hosting with [github pages](https://adamltyson.github.io/amap-python/index.html).

This can be done automatically with a 
[pre-commit hook](https://www.atlassian.com/git/tutorials/git-hooks). An 
example is 
[here](https://raw.githubusercontent.com/SainsburyWellcomeCentre/amap-python/master/doc_build/examples/pre-commit). 


#### Dependencies
The code in the amap repo should be primarily for registration. Any 
visualisation should be added to 
[neuro](https://github.com/sainsburywellcomecentre/neuro) and any general 
tools to [imlib](https://github.com/adamltyson/imlib).


#### Conventions
amap has recently (2019-08-02) dropped support for Python 3.5. Following 
this, a number of new python features will be adopted throughout.

* [pathlib](https://realpython.com/python-pathlib/) conventions 
(rather then `os.path`).
* [f-strings](https://realpython.com/python-f-strings/) 
(rather than `.format()` or using the old `%` operator). 

In all cases, please aim to replace old calls to `os.path` or `.format()` 
with pathlib object methods and f-strings.
