import copy

from templer.plonebuildout import abstract_buildout
from templer.core.vars import StringVar

LATEST_PLONE_VERSIONS = ['4.0.10','4.1.6','4.2.1']

VAR_PLONEVER = StringVar(
    'plone_version',
    title='Plone Version',
    description='Plone version # to install, latest are %s.' %' '.join(LATEST_PLONE_VERSIONS),
    default=LATEST_PLONE_VERSIONS[-1],
    page='Main',
    help="""
This is the version of Plone that will be used for this buildout.
You should enter the version number you wish to use.
"""
    )

class Plone4Buildout(abstract_buildout.AbstractBuildout):
    _template_dir = 'templates/plone4_buildout'
    summary = "A buildout for Plone 4 developer installation"
    help = """This template creates a Plone 4 buildout for development purposes.
It uses Zope in debug mode and sets a default password.
"""
    pre_run_msg = ""

    post_run_msg = """
Generation finished.

Now run bootstrap and buildout:

python bootstrap.by

bin/buildout

See Templer add-on page for more details:

http://templer-manual.readthedocs.org

"""

    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(abstract_buildout.AbstractBuildout.vars)
    
    # remove easy/expert mode (for now)
    vars = vars[1:]
    
    vars.extend(
           [ VAR_PLONEVER,           
        ]
    )

    def pre(self, command, output_dir, vars):
        
        # For easy mode (don't ask stupid questions)
        vars['expert_mode'] = 'easy' 
        vars['eggifiedzope'] = True
        vars['zope2_install'] = True
        super(Plone4Buildout, self).pre(command, output_dir, vars)



