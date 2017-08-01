# Python Macadmin Tools

This repository aims to collect a list of open-source Python-based tools for Mac systems administration tasks.

Why is this list limited to Python? Why not include all projects in this space? Python is an especially popular language among Mac sysadmins; this restriction is partly so that those learning Python for Mac-specific tasks have a mostly-complete list of known code and approaches from which to learn. It's also to help those more experienced with Python to discover projects that they may be able to adapt, extend and/or contribute to.

See something missing or incorrect? Please feel frede to [edit](https://github.com/timsutton/python-macadmin-tools/edit/master/README.md) or clone this file and [submit a pull request](https://github.com/timsutton/python-macadmin-tools/pulls). This repo was inspired by R.I. Pienaar's popular [free-for-dev](https://github.com/ripienaar/free-for-dev) repo.

Table of Contents
=================

* [Munki](#munki)
* [Imagr](#imagr)
* [Servers](#servers)
* [Deployment automation, imaging, packaging](#deployment-automation-imaging-packaging)
* [Client-side management: utilities](#client-side-management-utilities)
* [Client-side management: libraries and modules](#client-side-management-libraries-and-modules)
* [Mobile Device Management (MDM)](#mobile-device-management-mdm)
* [Misc. utilities and modules](#misc-utilities-and-modules)
* [Scripts and gists](#scripts-and-gists)
* [Configuration management](#configuration-management)

## Munki

* [autopromoter](https://github.com/jessepeterson/autopromoter) - Automatically promote (or demote) Munki pkginfo catalogs.
* [BananaEndocarp](https://github.com/clburlison/BananaEndocarp) - BananaEndocarp is a scripted GUI for interacting with MunkiWebAdmin2's API, for creating per-machine manifests.
* [BananaPeels](https://github.com/robperc/BananaPeels) - A framework for testing the deployement of packages via Munki wrapped in a CLI tool. Requires VMWare Fusion.
* [CloudFront-Middleware](https://github.com/AaronBurchfield/CloudFront-Middleware) - Securely access a munki repo with Amazon CloudFront.
* [Moscargo](https://github.com/arubdesu/Moscargo) - Flask-based Munki repo browser used for listing and downloading current versions of curated packages.
* [MunkiCatalogPromote](https://github.com/aysiu/MunkiCatalogPromote) - Promotes Munki pkginfo catalogs that haven't been promoted in X number of days.
* [MunkiGenericIcons](https://github.com/aysiu/MunkiGenericIcons) - Copies your own custom Generic.png to any Munki items missing a corresponding icon.
* [MunkiModulePackager](https://github.com/robperc/MunkiModulePackager) - CLI tool for downloading and packaging PyPi module sources for distribution via Munki.
* [Munki Enrollment Server](https://github.com/gerritdewitt/munki-enrollment-server) - A server that works in coordination with a [GUI client](https://github.com/gerritdewitt/munki-enrollment-client) that provides a method of enrolling a Mac with Munki for certificate-based communication and a custom manifest.
* [Munki project](https://github.com/munki/munki) - Managed software installations for Mac clients. Supports all popular software distribution formats. This is the de facto project repository.
* [Munki Promote](https://github.com/joshua-d-miller/munki-promote) - Another script for promoting items from one catalog to another.
* [Munki Sysadmin Usability Improvement Toolkit](https://github.com/velotraveler/munkisuit) - CLI tools for maintaining workflows for managing Munki catalogs along with AutoPkg.
* [MunkiWebAdmin](https://github.com/munki/munkiwebadmin) - A Django-based reporting app for Munki - support for licensing, manifest editing.
* [Munki-Do](https://github.com/grahampugh/munki-do) - A fork of MunkiWebAdmin with many new repo-editing features.
* [munki-facts](https://github.com/munki/munki-facts) - A framework for "admin-provided conditionals" for Munki.
* [munki-rebrand](https://github.com/ox-it/munki-rebrand) - Scripts used by University of Oxford IT Services to rebrand Munki.
* [munki-staging](https://github.com/ox-it/munki-staging) - A fork of the munki-trello project with several additional major features.
* [munki-trello](https://github.com/pebbleit/munki-trello) - A script that utilises a Trello board to manage the promotion of Munki items through development to testing to production catalogs.
* [OldMunkiPackages](https://github.com/aysiu/OldMunkiPackages) - Script to automatically remove older versions of packages that share the same catalogs.
* [PrinterGenerator](https://github.com/nmcspadden/PrinterGenerator) - Generate specific 'nopkg' pkginfos for printer configurations.
* [printer-pkginfo](https://github.com/grahamgilbert/printer-pkginfo) - Another script for generating specific 'nopkg' pkginfos for printer configurations.
* [Sal](https://github.com/salsoftware/sal) - Another Django-based reporting app for Munki, integrates with Facter facts on clients.
* [Simian](https://github.com/google/simian) - Custom Munki service based on GAE, by Google.
* [Spruce for Munki](https://github.com/sheagcraig/Spruce-for-Munki) - Generates lists/reports, including orphaned icons or unused products.
* [TweetCatalogUpdates](https://github.com/binkleybloom/tweetCatalogUpdates) - Python script that watches for catalog changes in your munki respository, and tweets them.

## Imagr

* [Imagr](https://github.com/grahamgilbert/imagr) - Mac app that performs imaging and deployment workflows fetched from a remote server, built with PyObjC.
* [Imagr Server](https://github.com/grahamgilbert/imagr_server) - Imagr reporting server built on Django.
* [ImagrConfigCreator](https://github.com/nmcspadden/ImagrConfigCreator) - Interactive script for generating or editing Imagr workflow plists.

## Servers

* [bsdpy](https://bitbucket.org/bruienne/bsdpy) - BSDP server with support for multiple netboot images, model/MAC filtering and an API.
* [Crypt](https://github.com/grahamgilbert/Crypt) - Client and server for a Django-based Filevault key escrow solution.
* [Macnamer](https://github.com/grahamgilbert/macnamer) - Django-based solution for managing Mac computer names.
* [Margarita](https://github.com/jessepeterson/margarita) - Flask-based web interface for Reposado.
* [pybsdpy](https://github.com/cabal95/pybsdp) - Another BSDP server.
* [Reposado](https://github.com/wdas/reposado) - Replacement for Apple's Software Update Service, supports multiple 'branches' of catalogs and offering cached updates no longer offered by Apple.

## Deployment automation, imaging, packaging

* [aamporter](https://github.com/timsutton/aamporter) - Tool for automating the download and importing of Adobe CS/CC updates into Munki.
* [AutoDMG](https://github.com/MagerValp/AutoDMG) - Mac app to create never-booted, restorable OS X system images, optionally with system updates and additional packages/applications, built with PyObjC.
* [AutoNBI](https://bitbucket.org/bruienne/autonbi) - Tool for automated creation of Netboot image bundles using System Image Utility's automation tools.
* [AutoPkg](https://github.com/autopkg/autopkg) - Tool and community for automating common deployment tasks using sharable 'recipes', for example: discovering new application updates, preparing them for deployment, importing into popular management platforms.
* [Brigadier](https://github.com/timsutton/brigadier) - Tool for fetch and install model-specific Boot Camp images, can be used to bootstrap drivers during Windows deployment.
* [can_haz_image](https://github.com/google/macops) - Tool for creating never-booted OS X system images with additional packages.
* [createOSXInstallPkg](https://github.com/munki/createOSXInstallPkg) - Tool for converting an OS X installer app/ESD to a package that can trigger the OS X install on the next boot, optionally with additional packages added in the install.
* [CreateUserPkg](https://github.com/MagerValp/CreateUserPkg) - Mac app to create a package that installs or updates a user on an OS X system, built with PyObjC.
* [easy_rider](https://github.com/sheagcraig/easy_rider) - Automatically create overrides for a list of AutoPkg recipes, using current production Munki pkginfo and templates to override final recipe.
* [first-boot-pkg](https://github.com/grahamgilbert/first-boot-pkg) - Tool for creating a single package that installs a series of packages automatically upon first boot.
* [appleLoops](https://github.com/carlashley/appleLoops) - Utility for downloading essential and optional audio content for Apple GarageBand, Logic Pro X, and MainStage 3.
* [JSSImporter](https://github.com/sheagcraig/JSSImporter) - Framework for connecting AutoPkg to JSS, for administrators running JAMF's Casper Suite.
* [JSSRecipeCreator](https://github.com/sheagcraig/JSSRecipeCreator) - Tool that enables Casper administrators to quickly create JSSImporter-compatbile AutoPkg recipes.
* [MacNamer](https://github.com/grahamgilbert/macnamer) - Combination of a Django web app and a companion script to run on client Macs for automatically setting computer names.
* [make-adobe-cc-license-pkg](https://github.com/timsutton/make-adobe-cc-license-pkg) - Tool for building packages and Munki pkginfos for CC for Teams device and Enterprise serial licenses.
* [make-profile-pkg](https://github.com/timsutton/make-profile-pkg) - Convert a Configuration Profile to an installer package that can be installed to both booted and non-booted volumes.
* [munkipkg](https://github.com/munki/munki-pkg) - Tool for building packages in a consistent, repeatable manner from source files and scripts in a project directory.
* [quickpkg](https://github.com/scriptingosx/quickpkg) - Quickly and easily builds a one-off package from an installed application, a disk image, or a zip file.
* [Recipe Robot](https://github.com/homebysix/recipe-robot) - A Python script and companion Mac app that is able to automatically generate AutoPkg recipes.
* [stew](https://github.com/chilcote/stew) - Creation of never-booted, restorable OS X system images with additional packages.
* [vfuse](https://github.com/chilcote/vfuse) - Tool for converting an OS X system DMG to a VMware Fusion VM.

## Client-side management: utilities

* [auto_logout](https://github.com/sheagcraig/auto_logout) - PyObjC app to automatically log out users, designed for Mac computer labs.
* [customdisplayprofiles](https://github.com/timsutton/customdisplayprofiles) - Programmatic configuration of display ColorSync profiles.
* [dockutil](https://github.com/kcrawford/dockutil) - Programmatic access to a user's dock.
* [Extinguish](https://github.com/arubdesu/Extinguish) - Generates profiles that disable Sparkle updates for specified apps.
* [installapplications](https://github.com/erikng/installapplications) - A tool for dynamic use of `InstallApplication` with DEP.
* [LoginLog](https://github.com/MagerValp/LoginLog) - Cocoa/PyObjC app that display a log of your choice over the loginwindow, useful during deployment tasks.
* [NCUtil](https://github.com/jacobsalmela/NCutil) - Programmatic access to Notification Center via direct manipulation of the NC database.
* [Nomadize](https://github.com/tburgin/Nomadize) - Tool to help move a local account or home folder to an Active Directory Mobile account.
* [offset](https://github.com/aysiu/offset) - Script and launchd combo for executing admin-defined scripts at logout (based on Outset).
* [outset](https://github.com/chilcote/outset) - Script and launchd combo for executing admin-defined scripts after logins and startup.
* [OutsetDockProfiler](https://github.com/nmcspadden/OutsetDockProfiler) - Script that creates a package to use with Outset that will install a user-level profile for a specific user of your choice.
* [PredicateInstaller](https://github.com/mkuron/PredicateInstaller) - Programmatic invocation of Software Update client tasks such as printer drivers, dictation voices, CLI tools, Boot Camp drivers, via the private SoftwareUpdate framework.
* [Privacy Services Manager](https://github.com/univ-of-utah-marriott-library-apple/privacy_services_manager) - Programmatic access to privacy, location, etc. services via direct manipulation of the TCC database.
* [pyLoginItems](https://github.com/pudquick/pyLoginItems) - Management of a user's login items list via PyObjC.
* [Service Discovery Tool](https://github.com/CLCMacTeam/sdt) - CLI diagnostics tool for reporting DHCP and NetBoot services.

## Client-side management: libraries and modules

* [ChromeBookmarkEditor](https://github.com/robperc/ChromeBookmarkEditor) - Python module for easily adding, removing, and moving positions of bookmarks on the Chrome bookmark menu in the context of the logged in user.
* [DockEditor](https://github.com/robperc/DockEditor) - Python module for easily adding, removing, and moving positions of Dock items in the context of the logged in user.
* [Facebook IT-CPE](https://github.com/facebook/IT-CPE) - A suite of tools that Facebook uses to manage their fleet of over 10,000 client machines.
* [FinderSidebarEditor](https://github.com/robperc/FinderSidebarEditor) - Python module for programmatically editing the Favorites entries of the Finder sidebar.
* [gpymacutil](https://github.com/google/macops) - Vast library of Python modules and tools for client management developed by Google.
* [MacModelShelf](https://github.com/MagerValp/MacModelShelf) - Returns human-readable Mac model names when given a serial number or model code.
* [OSXcollector](https://github.com/Yelp/osxcollector) - A forensic evidence collection & analysis toolkit for OS X, developed by Yelp.
* [pinpoint](https://github.com/clburlison/pinpoint) - A python script for finding Macs using the CoreLocation framework.
* [pyfacts](https://github.com/chilcote/pyfacts) - Returns various 'facts' about a Mac.
* [PyMacAdmin and crankd](https://github.com/nigelkersten/pymacadmin) - Collection of Python utilities for interfacing to directory services and system configuration state changes, Leopard-era, developed at Google.
* [SavingThrow](https://github.com/sheagcraig/SavingThrow) - Returns information on whether a Mac has adware/malware installed, and includes an option for automatic removal.
* [SafariBookmarkEditor](https://github.com/robperc/SafariBookmarkEditor) - Python module for easily adding, removing, and moving positions of Safari bookmarks in the context of the currently logged in user.
* [Stethoscope](https://github.com/Netflix/Stethoscope) - Web application that collects information for a given user's devices and gives them clear and specific recommendations for securing their systems.
* [U. of Utah Marriott Library Management Tools](https://github.com/univ-of-utah-marriott-library-apple/management_tools) - Python module for client management.
* [Zentral](https://github.com/zentralopensource/zentral) - Framework that allows administrators to configure automatic actions based on changes detected by [osquery](https://osquery.io/).

## Mobile Device Management (MDM)

* [Commandment](https://github.com/jessepeterson/commandment) - MDM server with support for managing iOS and OS X devices implemented in Python.
* [DEPy](https://github.com/bruienne/depy) - Python module for interacting with Apple's DEP service.
* [mdmvendorsign](https://github.com/grinich/mdmvendorsign) - Create a CSR as a "vendor" of Apple's MDM push notification service.
* [mk_pkg_manifest.py](https://gist.github.com/jessepeterson/d9d1f592a8c54395827f73dc60b3a0f3) - Script for creating an Apple software distribution manifest for an Apple pkg installer.

## Misc. utilities and modules

* [APInfo)(https://github.com/erikng/scripts/tree/master/APInfo) - Obtain information about iOS/macOS applications and optionally output the results to Slack.
* [appleseed](https://github.com/chilcote/appleseed) - Automate downloading os x seed packages.
* [edify](https://github.com/chilcote/edify) - Stores a customizable library of command line syntax examples, with short descriptions.
* [JSS Import](https://github.com/nmcspadden/JSSImport) - Pulls data from Casper 9 to a Postgres database for purpose of importing into WebHelpDesk. (Not to be confused with [JSSImporter](https://github.com/sheagcraig/JSSImporter).)
* [JSS Asset Tag Importer](https://github.com/bradschm/jss-assettag-importer) - Allows Casper administrators to quickly import asset tags into their JSS inventory.
* [mcxToProfile](https://github.com/timsutton/mcxToProfile) - Convert preference plists and MCX nodes to Configuration Profiles for OS X management.
* [ProfileSigner](https://github.com/nmcspadden/ProfileSigner) - A script that will encrypt and/or sign a .mobileconfig profile.
* [pyMacWarranty](https://github.com/pudquick/pyMacWarranty) - Retrieve warranty information given a Mac's serial number, estimates of manufacture date info and more.
* [pyMASreceipt](https://github.com/pudquick/pyMASreceipt) - Module for parsing Mac App Store receipts files.
* [Python-JSS](https://github.com/sheagcraig/python-jss) - Library that allows administrators to interact with a JSS using Python. Included with JSSImporter.
* [Serveralerts](https://github.com/hunty1/Serveralerts) - Manage the Server alerts DB of Server.app.
* [Service Discovery Tool](https://git.psu.edu/sysman/ServiceDiscoveryTool) - Broadcasts DHCP Request and BSDP Inform packets on the local network and reports reponses for NetBoot/DHCP diagnostics.
* [vserv](https://github.com/chilcote/vserv) - Service to monitor one or more vmx path[s] and restart the vmx[s] if necessary.
* [warranty](https://github.com/chilcote/warranty) - Another warranty information retrieval script.
* [Xcode Cocoa-Python Templates](https://github.com/gregneagle/Xcode6CocoaPythonTemplates) - Xcode 6 templates for Cocoa-Python development: Also [Xcode 5](https://github.com/gregneagle/Xcode5CocoaPythonTemplates), [Xcode 4](https://github.com/gregneagle/Xcode4CocoaPythonTemplates).
* [py-gsxws](https://github.com/filipp/py-gsxws) - Library for communicating with Apple's GSX API
* [SimplePySSH](https://github.com/robperc/SimplePySSH) - Module for executing and reading output from simple shell commands on remote machines via SSH using only built-in modules.
* [precache](https://github.com/krypted/precache) - Used to cache available Apple updates into an OS X Server running the Caching Service.
* [xcode_tools](https://github.com/carlashley/xcode_tools) - Grabs the XCode CLI tools and SDK packages from the Mac software update catalog and stores them in `~/Desktop` - avoids GUI prompts.

## Scripts and gists

* [Graham Gilbert](https://github.com/grahamgilbert/macscripts) - Client management, Munki, Puppet server automation
* [Hannes Juutilainen](https://github.com/hjuutilainen/adminscripts) - Collection of client attributes, client management and meta-packaging admin tasks
* [Michael Lynn](https://gist.github.com/pudquick) - Many small scripts and modules demonstrating the use of PyObjC and ctypes for native use of OS X system frameworks within Python.

## Configuration management

* [salt-osx](https://github.com/mosen/salt-osx) - SaltStack grains, modules, and states to manage OS X, largely using PyObjC and ctypes.
* [U. of Utah Marriott Library Firmware Password Manager](https://github.com/univ-of-utah-marriott-library-apple/firmware_password_manager) - Python script to automate the management of firmware passwords.
