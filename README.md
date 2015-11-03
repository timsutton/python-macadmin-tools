# Python Macadmin Tools

This repository aims to collect a list of open-source Python-based tools for Mac systems administration tasks.

Why is this list limited to Python? Why not include all projects in this space? Python is an especially popular language among Mac sysadmins; this restriction is partly so that those learning Python for Mac-specific tasks have a mostly-complete list of known code and approaches from which to learn. It's also to help those more experienced with Python to discover projects that they may be able to adapt, extend and/or contribute to.

See something missing or incorrect? Please feel free to [edit](https://github.com/timsutton/python-macadmin-tools/edit/master/README.md) or clone this file and [submit a pull request](https://github.com/timsutton/python-macadmin-tools/pulls). This repo was inspired by R.I. Pienaar's popular [free-for-dev](https://github.com/ripienaar/free-for-dev) repo.

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
* [BananaPeels](https://github.com/robperc/BananaPeels) - A framework for testing the deployement of packages via Munki wrapped in a CLI tool. Requires VMWare Fusion.
* [MunkiModulePackager](https://github.com/robperc/MunkiModulePackager) - CLI tool for downloading and packaging PyPi module sources for distribution via Munki.
* [Munki project](https://github.com/munki/munki) - Managed software installations for Mac clients. Supports all popular software distribution formats. This is the de facto project repository.
* [Munki Promote](https://github.com/joshua-d-miller/munki-promote) - Another script for promoting items from one catalog to another.
* [MunkiWebAdmin](https://github.com/munki/munkiwebadmin) - A Django-based reporting app for Munki - support for licensing, manifest editing.
* [munki-trello](https://github.com/pebbleit/munki-trello) - A script that utilises a Trello board to manage the promotion of Munki items through development to testing to production catalogs.
* [PrinterGenerator](https://github.com/nmcspadden/PrinterGenerator) - Generate specific 'nopkg' pkginfos for printer configurations.
* [printer-pkginfo](https://github.com/grahamgilbert/printer-pkginfo) - Another script for generating specific 'nopkg' pkginfos for printer configurations.
* [Sal](https://github.com/salsoftware/sal) - Another Django-based reporting app for Munki, integrates with Facter facts on clients.
* [Simian](https://github.com/google/simian) - Custom Munki service based on GAE, by Google.
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
* [first-boot-pkg](https://github.com/grahamgilbert/first-boot-pkg) - Tool for creating a single package that installs a series of packages automatically upon first boot.
* [JSSImporter](https://github.com/sheagcraig/JSSImporter) - Framework for connecting AutoPkg to JSS, for administrators running JAMF's Casper Suite.
* [JSSRecipeCreator](https://github.com/sheagcraig/JSSRecipeCreator) - Tool that enables Casper administrators to quickly create JSSImporter-compatbile AutoPkg recipes.
* [MacNamer](https://github.com/grahamgilbert/macnamer) - Combination of a Django web app and a companion script to run on client Macs for automatically setting computer names.
* [make-adobe-cc-license-pkg](https://github.com/timsutton/make-adobe-cc-license-pkg) - Tool for building packages and Munki pkginfos for CC for Teams device and Enterprise serial licenses.
* [make-profile-pkg](https://github.com/timsutton/make-profile-pkg) - Convert a Configuration Profile to an installer package that can be installed to both booted and non-booted volumes.
* [munkipkg](https://github.com/munki/munki-pkg) - Tool for building packages in a consistent, repeatable manner from source files and scripts in a project directory.
* [stew](https://github.com/chilcote/stew) - Creation of never-booted, restorable OS X system images with additional packages.
* [vfuse](https://github.com/chilcote/vfuse) - Tool for converting an OS X system DMG to a VMware Fusion VM.

## Client-side management: utilities

* [customdisplayprofiles](https://github.com/timsutton/customdisplayprofiles) - Programmatic configuration of display ColorSync profiles.
* [dockutil](https://github.com/kcrawford/dockutil) - Programmatic access to a user's dock.
* [LoginLog](https://github.com/MagerValp/LoginLog) - Cocoa/PyObjC app that display a log of your choice over the loginwindow, useful during deployment tasks.
* [NCUtil](https://github.com/jacobsalmela/NCutil) - Programmatic access to Notification Center via direct manipulation of the NC database.
* [outset](https://github.com/chilcote/outset) - Script and launchd combo for executing admin-defined scripts after logins and startup.
* [OutsetDockProfiler](https://github.com/nmcspadden/OutsetDockProfiler) - Script that creates a package to use with Outset that will install a user-level profile for a specific user of your choice.
* [PredicateInstaller](https://github.com/mkuron/PredicateInstaller) - Programmatic invocation of Software Update client tasks such as printer drivers, dictation voices, CLI tools, Boot Camp drivers, via the private SoftwareUpdate framework.
* [Privacy Services Manager](https://github.com/univ-of-utah-marriott-library-apple/privacy_services_manager) - Programmatic access to privacy, location, etc. services via direct manipulation of the TCC database.
* [pyLoginItems](https://github.com/pudquick/pyLoginItems) - Management of a user's login items list via PyObjC.
* [SafariBookmarkEditor](https://github.com/robperc/SafariBookmarkEditor) - CLI tool for adding and removing Safari bookmarks in the context of the currently logged in user. 

## Client-side management: libraries and modules

* [Facebook IT-CPE](https://github.com/facebook/IT-CPE) - A suite of tools that Facebook uses to manage their fleet of over 10,000 client machines.
* [gpymacutil](https://github.com/google/macops) - Vast library of Python modules and tools for client management developed by Google.
* [MacModelShelf](https://github.com/MagerValp/MacModelShelf) - Returns human-readable Mac model names when given a serial number or model code.
* [OSXcollector](https://github.com/Yelp/osxcollector) - A forensic evidence collection & analysis toolkit for OS X, developed by Yelp.
* [pyfacts](https://github.com/chilcote/pyfacts) - Returns various 'facts' about a Mac.
* [PyMacAdmin and crankd](https://github.com/nigelkersten/pymacadmin) - Collection of Python utilities for interfacing to directory services and system configuration state changes, Leopard-era, developed at Google.
* [SavingThrow](https://github.com/sheagcraig/SavingThrow) - Returns information on whether a Mac has adware/malware installed, and includes an option for automatic removal.
* [U. of Utah Marriott Library Management Tools](https://github.com/univ-of-utah-marriott-library-apple/management_tools) - Python module for client management.

## Mobile Device Management (MDM)

* [Commandment](https://github.com/jessepeterson/commandment) - MDM server with support for managing iOS and OS X devices implemented in Python.

## Misc. utilities and modules

* [appleseed](https://github.com/chilcote/appleseed) - Automate downloading os x seed packages.
* [edify](https://github.com/chilcote/edify) - Stores a customizable library of command line syntax examples, with short descriptions.
* [mcxToProfile](https://github.com/timsutton/mcxToProfile) - Convert preference plists and MCX nodes to Configuration Profiles for OS X management.
* [pyMacWarranty](https://github.com/pudquick/pyMacWarranty) - Retrieve warranty information given a Mac's serial number, estimates of manufacture date info and more.
* [pyMASreceipt](https://github.com/pudquick/pyMASreceipt) - Module for parsing Mac App Store receipts files.
* [Python-JSS](https://github.com/sheagcraig/python-jss) - Library that allows administrators to interact with a JSS using Python. Included with JSSImporter.
* [vserv](https://github.com/chilcote/vserv) - Service to monitor one or more vmx path[s] and restart the vmx[s] if necessary.
* [warranty](https://github.com/chilcote/warranty) - Another warranty information retrieval script.
* Xcode Cocoa-Python Templates - Xcode templates for Cocoa-Python development: [Xcode 6](https://github.com/gregneagle/Xcode6CocoaPythonTemplates), [Xcode 5](https://github.com/gregneagle/Xcode5CocoaPythonTemplates), [Xcode 4](https://github.com/gregneagle/Xcode4CocoaPythonTemplates).

## Scripts and gists

* [Graham Gilbert](https://github.com/grahamgilbert/macscripts) - Client management, Munki, Puppet server automation
* [Hannes Juutilainen](https://github.com/hjuutilainen/adminscripts) - Collection of client attributes, client management and meta-packaging admin tasks
* [Michael Lynn](https://gist.github.com/pudquick) - Many small scripts and modules demonstrating the use of PyObjC and ctypes for native use of OS X system frameworks within Python.

## Configuration management
* [salt-osx](https://github.com/mosen/salt-osx) - SaltStack grains, modules, and states to manage OS X, largely using PyObjC and ctypes.
