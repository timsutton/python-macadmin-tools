# Python Macadmin Tools

This repository aims to collect a list of open-source Python-based tools for Mac systems administration tasks.

Why is this list limited to Python? Why not include all projects in this space? Python is an especially popular language among Mac sysadmins; this restriction is partly so that those learning Python for Mac-specific tasks have a mostly-complete list of known code and approaches from which to learn. It's also to help those more experienced with Python to discover projects that they may be able to adapt, extend and/or contribute to.

See something missing or incorrect? Please feel free to [edit](https://github.com/timsutton/python-macadmin-tools/edit/master/README.md) or clone this file and [submit a pull request](https://github.com/timsutton/python-macadmin-tools/pulls). This repo was inspired by R.I. Pienaar's popular [free-for-dev](https://github.com/ripienaar/free-for-dev) repo.

Table of Contents
=================

* [Munki and ecosystem](#munki-and-ecosystem)
* [Servers](#servers)
* [Deployment automation, imaging, packaging](#deployment-automation-imaging-packaging)
* [Client-side management: utilities](#client-side-management-utilities)
* [Client-side management: libraries and modules](#client-side-management-libraries-and-modules)
* [Misc. utilities and modules](#misc-utilities-and-modules)
* [Scripts and gists](#scripts-and-gists)
* [Configuration Management](#configuration-management)

## Munki and ecosystem
* [Munki project](https://github.com/munki/munki) - Managed software installations for Mac clients. Supports all popular software distribution formats.
* [MunkiWebAdmin](https://github.com/munki/munkiwebadmin) - A Django-based reporting app for Munki - support for licensing, manifest editing.
* [Sal](https://github.com/salsoftware/sal) - Another Django-based reporting app for Munki, integrates with Facter facts on clients.
* [Simian](https://github.com/google/simian) - Custom Munki service based on GAE, by Google.

## Servers
* [Reposado](https://github.com/wdas/reposado) - Replacement for Apple's Software Update Service, supports multiple 'branches' of catalogs and offering cached updates no longer offered by Apple.
* [Margarita](https://github.com/jessepeterson/margarita) - Flask-based web interface for Reposado. 
* [bsdpy](https://bitbucket.org/bruienne/bsdpy) - BSDP server with support for multiple netboot images, model/MAC filtering and an API.
* [pybsdpy](https://github.com/cabal95/pybsdp) - Another BSDP server.
* [Crypt](https://github.com/grahamgilbert/Crypt) - Client and server for a Django-based Filevault key escrow solution.
* [Macnamer](https://github.com/grahamgilbert/macnamer) - Django-based solution for managing Mac computer names.

## Deployment automation, imaging, packaging
* [AutoDMG](https://github.com/MagerValp/AutoDMG) - Mac app to create never-booted, restorable OS X system images, optionally with system updates and additional packages/applications, built with PyObjC.
* [CreateUserPkg](https://github.com/MagerValp/CreateUserPkg) - Mac app to create a package that installs or updates a user on an OS X system, built with PyObjC.
* [createOSXInstallPkg](https://github.com/munki/createOSXInstallPkg) - Tool for converting an OS X installer app/ESD to a package that can trigger the OS X install on the next boot, optionally with additional packages added in the install.
* [AutoPkg](https://github.com/autopkg/autopkg) - Tool and community for automating common deployment tasks using sharable 'recipes', for example: discovering new application updates, preparing them for deployment, importing into popular management platforms.
* [vfuse](https://github.com/chilcote/vfuse) - Tool for converting an OS X system DMG to a VMware Fusion VM.
* [stew](https://github.com/chilcote/stew) - Creation of never-booted, restorable OS X system images with additional packages.
* [AutoNBI](https://bitbucket.org/bruienne/autonbi) - Tool for automated creation of Netboot image bundles using System Image Utility's automation tools.
* [Brigadier](https://github.com/timsutton/brigadier) - Tool for fetch and install model-specific Boot Camp images, can be used to bootstrap drivers during Windows deployment.
* [aamporter](https://github.com/timsutton/aamporter) - Tool for automating the download and importing of Adobe CS/CC updates into Munki.
* [can_haz_image](https://github.com/google/macops) - Tool for creating never-booted OS X system images with additional packages.
* [make-profile-pkg](https://github.com/timsutton/make-profile-pkg) - Convert a Configuration Profile to an installer package that can be installed to both booted and non-booted volumes.

## Client-side management: utilities

* [dockutil](https://github.com/kcrawford/dockutil) - Programmatic access to a user's dock.
* [outset](https://github.com/chilcote/outset) - Script and launchd combo for executing admin-defined scripts after logins and startup.
* [crankd](https://github.com/google/macops) - Tool for configuring hooks that fire under certain system configuration state changes.
* [customdisplayprofiles](https://github.com/timsutton/customdisplayprofiles) - Programmatic configuration of display ColorSync profiles.
* [Privacy Services Manager](https://github.com/univ-of-utah-marriott-library-apple/privacy_services_manager) - Programmatic access to privacy, location, etc. services via direct manipulation of the TCC database.
* [NCUtil](https://github.com/jacobsalmela/NCutil) - Programmatic access to Notification Center via direct manipulation of the NC database.
* [PredicateInstaller](https://github.com/mkuron/PredicateInstaller) - Programmatic invocation of Software Update client tasks such as printer drivers, dictation voices, CLI tools, Boot Camp drivers, via the private SoftwareUpdate framework.
* [pyLoginItems](https://github.com/pudquick/pyLoginItems) - Management of a user's login items list via PyObjC.
* [LoginLog](https://github.com/MagerValp/LoginLog) - Cocoa/PyObjC app that display a log of your choice over the loginwindow, useful during deployment tasks.

## Client-side management: libraries and modules
* [gpymacutil](https://github.com/google/macops) - Vast library of Python modules and tools for client management.
* [U. of Utah Marriott Library Management Tools](https://github.com/univ-of-utah-marriott-library-apple/management_tools) - Python module for client management.
* [pyfacts](https://github.com/chilcote/pyfacts) - Returns various 'facts' about a Mac.

## Misc. utilities and modules
* [mcxToProfile](https://github.com/timsutton/mcxToProfile) - Convert preference plists and MCX nodes to Configuration Profiles for OS X management.
* Xcode Cocoa-Python Templates - Xcode templates for Cocoa-Python development: [Xcode 6](https://github.com/gregneagle/Xcode6CocoaPythonTemplates), [Xcode 5](https://github.com/gregneagle/Xcode5CocoaPythonTemplates), [Xcode 4](https://github.com/gregneagle/Xcode4CocoaPythonTemplates).
* [pyMacWarranty](https://github.com/pudquick/pyMacWarranty) - Retrieve warranty information given a Mac's serial number, estimates of manufacture date info and more.
* [pyMASreceipt](https://github.com/pudquick/pyMASreceipt) - Module for parsing Mac App Store receipts files.

## Scripts and gists

* [Hannes Juutilainen](https://github.com/hjuutilainen/adminscripts) - Collection of client attributes, client management and meta-packaging admin tasks
* [Graham Gilbert](https://github.com/grahamgilbert/macscripts) - Client management, Munki, Puppet server automation
* [Michael Lynn](https://gist.github.com/pudquick) - Many small scripts and modules demonstrating the use of PyObjC and ctypes for native use of OS X system frameworks within Python.



## Configuration management
* [salt-osx](https://github.com/mosen/salt-osx) - SaltStack grains, modules, and states to manage OS X, largely using PyObjC and ctypes.
