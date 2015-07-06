from sixfeetup.utils import helpers as sfutils


def importVariousInitial(context):
    """Run the setup handlers for the initial profile"""
    if context.readDataFile('rspe_policy-initial.txt') is None:
        return


def importVarious(context):
    """Run the setup handlers for the default profile"""
    if context.readDataFile('rspe_policy-default.txt') is None:
        return
    # automagically run a plone migration if needed
    sfutils.runPortalMigration()
    # automagically run the upgrade steps for this package
    sfutils.runUpgradeSteps(u'rspe.policy:default')
    sfutils.refreshAssetRegistry()
